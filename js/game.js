// Joetopia web: glue between the compiled Kotlin engine (exact APK rules) and the walkable map + menus.
(function () {
  const K = JoetopiaKt.com.grokbot.joetopia.game.JoetopiaApi;
  const $ = s => document.querySelector(s), T = JArt.T;
  const cv = $('#cv'), g = cv.getContext('2d'); g.imageSmoothingEnabled = false;
  const POSKEY = 'joetopia-pos', SETKEY = 'joetopia-settings';
  const settings = Object.assign({ fs: 'm', labels: 'all', speed: 'normal' }, safeJSON(localStorage.getItem(SETKEY)) || {});
  function safeJSON(s) { try { return JSON.parse(s); } catch (e) { return null; } }
  function saveSettings() { localStorage.setItem(SETKEY, JSON.stringify(settings)); applySettings(); }
  function applySettings() { document.body.classList.remove('fs-s', 'fs-l', 'fs-xl'); if (settings.fs !== 'm') document.body.classList.add('fs-' + settings.fs); }
  applySettings();

  let encFrom = null; // road-encounter npc id while talking to it / fighting what came out of it
  let scene = null, st = null, map = null, probe = [], restorePending = false, lastName = '';
  const P = { x: 9, y: 12, rx: 9, ry: 12, dir: 'up' };
  let moving = null, path = [], pendingObj = null, clickTarget = null;
  const held = new Set(); let needRelease = false;

  // ---------- engine sync ----------
  function sync(log) {
    scene = JSON.parse(K.scene()); st = JSON.parse(K.status());
    JUI.hud(st); updateMenus();
    if (scene.mode === 'EXPLORE') {
      JUI.hideOverlay(); const prevNode = map && map.node; ensureMap();
      if (log) JUI.showMsg(log, null, JArt.logArt(log));
      else if (st.node === 'intro' && prevNode !== 'intro') JUI.showMsg(scene.text);
    } else {
      JUI.clearMsg();
      if (scene.mode === 'TALK') encFrom = /^enc_/.test(st.talk || '') ? st.talk : null;
      else if (scene.mode === 'STREET') encFrom = JArt.streetArtId(st.streetArt || st.street);
      else if (!/^COMBAT/.test(scene.mode)) encFrom = null;
      else if (st.combat) { const a = JArt.enemyArtId(st.combat.enemyId, st.combat.enemy); if (a && /^street_/.test(a)) encFrom = a; } // Undercroft ambush, Kraken
      JUI.showScene(scene, st, { onPick, lastName, encArt: /^COMBAT/.test(scene.mode) || scene.mode === 'STREET' ? encFrom : null });
    }
  }
  function onPick(i, name) {
    const from = scene.mode;
    if (from === 'CREATE_NAME') lastName = name || '';
    if (from === 'TITLE' && /^Continue/.test(scene.choices[i].label)) { map = null; restorePending = true; }
    if (from === 'GAME_OVER' && /load|continue|save/i.test(scene.choices[i].label)) { map = null; restorePending = true; }
    K.choose(i, name || '');
    const now = K.mode();
    const log = K.lastLog();
    sync(now === 'EXPLORE' && from !== 'TITLE' ? log : '');
  }
  function ensureMap() {
    probe = safeJSON(K.probe()) || [];
    const node = st.node;
    if (!map || map.node !== node) enterNode(node, map && map.node);
    else { map = JMap.build(node, probe, scene.choices); if (!JMap.walkable(map, P.x, P.y)) place(map.start); }
  }
  function enterNode(node, prev) {
    map = JMap.build(node, probe, scene.choices); path = []; moving = null; pendingObj = null;
    held.clear(); needRelease = true; document.querySelectorAll('#dpad .on').forEach(b => b.classList.remove('on'));
    let spot = null;
    if (restorePending) { const s = safeJSON(localStorage.getItem(POSKEY)); if (s && s.node === node && JMap.walkable(map, s.x, s.y)) { spot = [s.x, s.y]; P.dir = s.dir || 'down'; } }
    restorePending = false;
    if (!spot && prev) { const ex = map.objs.find(o => o.type === 'exit' && o.target === prev); if (ex) { spot = ex.spawn; P.dir = { N: 'down', S: 'up', W: 'right', E: 'left' }[ex.side]; } }
    if (!spot) { // arrived by teleport/story: nearest free tile to the lower middle of the room
      let best = null, bd = 1e9;
      for (let y = 2; y < JMap.H - 1; y++) for (let x = 1; x < JMap.W - 1; x++) if (JMap.walkable(map, x, y) && JMap.bfs(map, x, y, (a, b) => a === map.start[0] && b === map.start[1]) !== null) { const d = Math.abs(x - 9) + Math.abs(y - (JMap.H - 4)); if (d < bd) { bd = d; best = [x, y]; } }
      spot = best || map.start; P.dir = 'down';
    }
    place(spot);
    const inf = JMap.info(node); JUI.banner(inf.name, inf.region ? inf.region + ' · ' + st.regionKind : '');
  }
  function place([x, y]) { P.x = P.rx = x; P.y = P.ry = y; savePos(); }
  function savePos() { if (map) localStorage.setItem(POSKEY, JSON.stringify({ node: map.node, x: P.x, y: P.y, dir: P.dir })); }

  // ---------- movement ----------
  const DIRS = { up: [0, -1], down: [0, 1], left: [-1, 0], right: [1, 0] };
  function blocked() { return !map || !scene || scene.mode !== 'EXPLORE' || JUI.overlayOpen() || JUI.msgOpen(); }
  function step(dir) {
    if (blocked() || moving) return false;
    P.dir = dir; const [dx, dy] = DIRS[dir]; const nx = P.x + dx, ny = P.y + dy;
    const t = map.grid[ny] && map.grid[ny][nx];
    if (t === 'door' || JMap.walkable(map, nx, ny)) { moving = { fx: P.x, fy: P.y, tx: nx, ty: ny, t0: performance.now(), dur: settings.speed === 'fast' ? 85 : 140 }; return true; }
    return false;
  }
  function arrive() {
    P.x = moving.tx; P.y = moving.ty; P.rx = P.x; P.ry = P.y; moving = null; savePos();
    const ex = map.objs.find(o => o.type === 'exit' && o.x === P.x && o.y === P.y);
    if (ex) { path = []; pendingObj = null; useObj(ex); if (map && map.node === ex.node0) {} return; }
    if (path.length) { const [x, y] = path.shift(); const d = Object.keys(DIRS).find(k => DIRS[k][0] === x - P.x && DIRS[k][1] === y - P.y); if (!d || !step(d)) path = []; return; }
    if (pendingObj) { const o = pendingObj; pendingObj = null; if (Math.abs(o.x - P.x) + Math.abs(o.y - P.y) === 1) { face(o); useObj(o); } }
  }
  function face(o) { const dx = o.x - P.x, dy = o.y - P.y; P.dir = dx > 0 ? 'right' : dx < 0 ? 'left' : dy > 0 ? 'down' : 'up'; }
  function focusObj() {
    if (!map) return null; const [dx, dy] = DIRS[P.dir];
    const f = JMap.objAt(map, P.x + dx, P.y + dy); if (f) return f;
    return map.objs.find(o => o.type !== 'exit' && Math.abs(o.x - P.x) + Math.abs(o.y - P.y) === 1) || null;
  }
  function useObj(o) {
    const c = scene.choices[o.i];
    if (!c || c.label !== o.label) { sync(); return; }
    if (!c.enabled) { JUI.showMsg('Not right now: ' + c.label); if (o.type === 'exit') place(o.spawn); return; }
    const before = st.node;
    onPick(o.i, '');
    if (o.type === 'exit' && st && st.node === before && map && map.node === before) place(o.spawn);
  }
  function interact() {
    if (JUI.msgOpen()) { JUI.nextMsg(); return; }
    if (blocked() || moving) return;
    const o = focusObj(); if (o) { if (o.type !== 'exit') face(o); useObj(o); }
  }
  function goTo(tx, ty) {
    if (blocked()) return;
    const o = JMap.objAt(map, tx, ty);
    let goal, obj = null;
    if (o && o.type !== 'exit') { if (Math.abs(o.x - P.x) + Math.abs(o.y - P.y) === 1) { face(o); useObj(o); return; } goal = (x, y) => Math.abs(x - o.x) + Math.abs(y - o.y) === 1; obj = o; }
    else goal = (x, y) => x === tx && y === ty;
    const pth = JMap.bfs(map, P.x, P.y, goal); if (!pth || !pth.length) return;
    path = pth; pendingObj = obj; clickTarget = [tx, ty];
    if (!moving) { const [x, y] = path.shift(); const d = Object.keys(DIRS).find(k => DIRS[k][0] === x - P.x && DIRS[k][1] === y - P.y); step(d); }
  }

  // ---------- menus ----------
  function menuCall(which) { if (!st || !st.menus) { JUI.toast('Not now.'); return; } if (K.openMenu(which)) sync(); else JUI.toast('Not now.'); }
  $('#btnGear').onclick = () => menuCall('gear');
  $('#btnStats').onclick = () => menuCall('stats');
  $('#btnQuests').onclick = () => menuCall('journal');
  $('#btnMyco').onclick = () => menuCall('myco');
  document.querySelectorAll('.dd > .mb').forEach(b => b.addEventListener('click', e => {
    e.stopPropagation(); const dd = b.parentElement; const was = dd.classList.contains('open'); JUI.closeDD();
    if (!was) { fillMenu(dd.dataset.dd); dd.classList.add('open'); const f = dd.querySelector('.item:not(:disabled)'); if (f) f.focus(); }
  }));
  function toggleStream() { const ok = K.toggleStream(); const log = K.lastLog(); sync(log); if (!ok && !log) JUI.toast('No signal for streaming here.'); }
  function fillMenu(which) {
    const exploring = scene && scene.mode === 'EXPLORE';
    if (which === 'here') {
      const items = [];
      if (exploring) {
        items.push({ info: JMap.placeName(st.node) + ' — ' + st.region });
        items.push({ label: '👀 Look around', on: () => JUI.showMsg(scene.text) }); items.push({ hr: 1 });
        const faceOf = i => { const o = map && map.objs.find(o => o.i === i); const id = o && (o.npc || (o.type === 'talk' && o.target)); return id && JOETOPIA_ART.faces[id]; };
        scene.choices.forEach((c, i) => items.push({ label: c.label, img: faceOf(i), disabled: !c.enabled, on: () => onPick(i, '') }));
      } else items.push({ info: 'Finish what you are doing first.' });
      JUI.fillDD($('#ddHere'), items);
    } else if (which === 'stream') {
      JUI.fillDD($('#ddStream'), [
        { info: `👁 Views: ${st.views} (${st.viewsTier})` }, { info: `📶 Signal: ${st.signal}% · ${st.streaming ? '🔴 LIVE now' : 'offline'}` },
        { label: st.streaming ? '⏹ End the stream' : '🔴 Go LIVE', disabled: !exploring || (!st.streaming && !st.canStream), on: toggleStream },
        { info: 'Views grow from things you do on stream; new faces and new tricks pay best.' },
      ]);
    } else if (which === 'save') {
      JUI.fillDD($('#ddSave'), [
        { label: '💾 Save now', disabled: !st || !st.canSave, on: () => { if (K.save()) { savePos(); JUI.toast('Game saved'); } else JUI.toast("Can't save right now"); sync(); } },
        { label: '📂 Load last save', disabled: !K.hasSave(), on: () => { if (K.load()) { map = null; restorePending = true; JUI.toast('Loaded'); } sync(); } },
        { label: '🏠 Title screen', on: () => { K.toTitle(); map = null; sync(); } },
        { info: 'Autosaves to this browser after every step you take in the world.' },
      ]);
    } else if (which === 'settings') {
      const fsN = { s: 'Small', m: 'Medium', l: 'Large', xl: 'Extra large' }, fsNext = { s: 'm', m: 'l', l: 'xl', xl: 's' };
      JUI.fillDD($('#ddSettings'), [
        { label: '🔠 Text size: ' + fsN[settings.fs], on: () => { settings.fs = fsNext[settings.fs]; saveSettings(); } },
        { label: '🏷 Map labels: ' + (settings.labels === 'all' ? 'Everything' : 'Nearby only'), on: () => { settings.labels = settings.labels === 'all' ? 'near' : 'all'; saveSettings(); } },
        { label: '🚶 Walk speed: ' + (settings.speed === 'fast' ? 'Fast' : 'Normal'), on: () => { settings.speed = settings.speed === 'fast' ? 'normal' : 'fast'; saveSettings(); } },
        { hr: 1 },
        { label: '🗑 Delete save & start over', on: () => { if (confirm('Delete your saved game?')) { localStorage.removeItem('joetopia-save'); localStorage.removeItem(POSKEY); K.reset(-1); map = null; sync(); } } },
        { info: 'Keys: arrows/WASD move · Enter/Space act · Esc back · I gear · C stats · J quests · M mushrooms · V stream · H here' },
      ]);
    }
  }
  function updateMenus() {
    const m = !!(st && st.menus);
    ['#btnGear', '#btnStats', '#btnQuests', '#btnMyco'].forEach(s => $(s).disabled = !m);
    $('#btnStream').classList.toggle('live', !!(st && st.streaming));
    $('#btnHere').disabled = !(scene && scene.mode === 'EXPLORE');
  }

  // ---------- input ----------
  const KEYDIR = { ArrowUp: 'up', ArrowDown: 'down', ArrowLeft: 'left', ArrowRight: 'right', w: 'up', s: 'down', a: 'left', d: 'right', W: 'up', S: 'down', A: 'left', D: 'right' };
  function escape() {
    if (JUI.msgOpen()) { JUI.nextMsg(); return; }
    if (document.querySelector('.dd.open')) { JUI.closeDD(); return; }
    if (JUI.overlayOpen() && scene) {
      if (scene.mode === 'COMBAT_ITEMS') { const bi = scene.choices.findIndex(c => /^Back/i.test(c.label)); if (bi >= 0) { onPick(bi, ''); return; } }
      const i = JUI.closeIndex(scene);
      if (i >= 0) onPick(i, '');
      return;
    }
    const dd = document.querySelector('[data-dd=here]'); fillMenu('here'); dd.classList.add('open'); const f = dd.querySelector('.item:not(:disabled)'); if (f) f.focus();
  }
  document.addEventListener('keydown', e => {
    if (e.target.tagName === 'INPUT') return;
    const inDD = e.target.closest && e.target.closest('.dd-menu');
    if (JUI.overlayOpen() || inDD) {
      if (e.key === 'Escape') { e.preventDefault(); escape(); return; }
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp' || ((e.key === 'ArrowLeft' || e.key === 'ArrowRight') && e.target.classList.contains('cmd'))) {
        e.preventDefault(); const root = inDD ? e.target.closest('.dd-menu') : $('#panel');
        const list = [...root.querySelectorAll('button:not(:disabled), summary')].filter(b => b.offsetParent !== null);
        const k = list.indexOf(document.activeElement); const d = (e.key === 'ArrowDown' || e.key === 'ArrowRight') ? 1 : -1;
        const n = list[(k + d + list.length) % list.length]; if (n) n.focus(); return;
      }
      if (JUI.overlayOpen() && /^[1-5]$/.test(e.key)) { const b = document.querySelectorAll('#panel .cmd')[+e.key - 1]; if (b && !b.disabled) { e.preventDefault(); b.click(); } }
      return;
    }
    if (JUI.msgOpen()) { if ([' ', 'Enter', 'e', 'E', 'z', 'Z', 'Escape', 'x', 'X'].includes(e.key)) { e.preventDefault(); JUI.nextMsg(); } return; }
    if (KEYDIR[e.key] && e.repeat && needRelease) { e.preventDefault(); return; }
    if (KEYDIR[e.key]) { e.preventDefault(); needRelease = false; held.add(KEYDIR[e.key]); path = []; pendingObj = null; if (!moving) step(KEYDIR[e.key]); return; }
    if ([' ', 'Enter', 'e', 'E', 'z', 'Z'].includes(e.key)) { e.preventDefault(); interact(); return; }
    if (e.key === 'Escape' || e.key === 'x' || e.key === 'X') { e.preventDefault(); escape(); return; }
    const sc = { i: '#btnGear', I: '#btnGear', c: '#btnStats', C: '#btnStats', j: '#btnQuests', J: '#btnQuests', m: '#btnMyco', M: '#btnMyco' }[e.key];
    if (sc) { $(sc).click(); return; }
    if (e.key === 'v' || e.key === 'V') { if (st && (st.canStream || st.streaming)) toggleStream(); return; }
    if (e.key === 'h' || e.key === 'H') { e.stopPropagation(); escape(); }
  });
  document.addEventListener('keyup', e => { if (KEYDIR[e.key]) held.delete(KEYDIR[e.key]); });
  window.addEventListener('blur', () => held.clear());
  cv.addEventListener('pointerdown', e => {
    if (JUI.msgOpen()) { JUI.nextMsg(); return; }
    const r = cv.getBoundingClientRect(); const x = Math.floor((e.clientX - r.left) / r.width * JMap.W), y = Math.floor((e.clientY - r.top) / r.height * JMap.H);
    goTo(x, y);
  });
  document.querySelectorAll('#dpad button').forEach(b => {
    const d = b.dataset.dir;
    const on = e => { e.preventDefault(); held.add(d); b.classList.add('on'); path = []; pendingObj = null; if (JUI.msgOpen()) return; if (!moving) step(d); };
    const off = e => { e.preventDefault(); held.delete(d); b.classList.remove('on'); };
    b.addEventListener('pointerdown', on); b.addEventListener('pointerup', off); b.addEventListener('pointerleave', off); b.addEventListener('pointercancel', off);
  });
  $('#aBtn').addEventListener('pointerdown', e => { e.preventDefault(); if (JUI.overlayOpen()) { const f = document.activeElement; if (f && f.closest('#panel')) f.click(); return; } interact(); });
  $('#bBtn').addEventListener('pointerdown', e => { e.preventDefault(); e.stopPropagation(); escape(); });

  // ---------- loop ----------
  function loop(t) {
    if (moving) {
      const k = Math.min(1, (performance.now() - moving.t0) / moving.dur);
      P.rx = moving.fx + (moving.tx - moving.fx) * k; P.ry = moving.fy + (moving.ty - moving.fy) * k;
      if (k >= 1) arrive();
    } else if (!blocked() && held.size) { step([...held][held.size - 1]); }
    if (map) {
      const f = (!moving && scene && scene.mode === 'EXPLORE') ? focusObj() : null;
      JMap.render(g, map, t, { player: P, status: st, encounter: scene && scene.mode !== 'EXPLORE' ? encFrom : (JUI.msgPic() || {}).sprite ? JUI.msgPic().id : null, labels: settings.labels === 'all', focus: f, target: path.length ? clickTarget : null });
      JUI.prompt(f && !JUI.msgOpen() && !JUI.overlayOpen() ? 'Ⓐ ' + f.label + (scene.choices[f.i] && !scene.choices[f.i].enabled ? '  (unavailable)' : '') : '');
    } else { g.fillStyle = '#120b1f'; g.fillRect(0, 0, cv.width, cv.height); JUI.prompt(''); }
    requestAnimationFrame(loop);
  }

  // ---------- test / debug hook ----------
  window.__joetopia = {
    api: K, sync: l => sync(l), pick: (i, n) => onPick(i, n),
    state: () => ({ mode: scene && scene.mode, node: st && st.node, title: scene && scene.title, player: { x: P.x, y: P.y, dir: P.dir }, moving: !!moving,
      overlay: JUI.overlayOpen(), msg: JUI.msgOpen(), status: st, mapNpc: scene && scene.mode !== 'EXPLORE' ? encFrom : (JUI.msgPic() || {}).sprite ? JUI.msgPic().id : null, choices: scene ? scene.choices.map(c => c.label) : [],
      objs: map ? map.objs.map(o => ({ type: o.type, x: o.x, y: o.y, i: o.i, target: o.target, label: o.label, side: o.side, spawn: o.spawn })) : [] }),
    step, interact, goTo, escape, useObj: i => { const o = map.objs.find(o => o.i === i); if (o) useObj(o); },
    walkTo: (x, y) => goTo(x, y), placeholders: () => JArt.placeholders(),
    debug: (c, a, b) => { const r = K.debug(c, a || '', b || ''); sync(K.lastLog()); return r; },
  };

  K.reset(-1);
  sync();
  requestAnimationFrame(loop);
})();
