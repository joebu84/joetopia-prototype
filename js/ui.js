// HTML UI: menu overlay (engine scenes as dropdown groups), battle screen, menu bar, HUD, messages.
(function () {
  const UI = window.JOETOPIA_UI, $ = s => document.querySelector(s);
  const el = (tag, cls, txt) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; };
  // Auto-scroll: a story/log panel follows its bottom so the newest text is visible, also after later layout changes
  // (pictures loading, the panel resizing), until the player scrolls it by hand.
  function stickBottom(node) {
    let follow = true; const go = () => { if (follow) node.scrollTop = node.scrollHeight; };
    ['wheel', 'touchmove', 'keydown'].forEach(ev => node.addEventListener(ev, () => { follow = false; }, { passive: true }));
    node.dataset.autoscroll = '1';
    requestAnimationFrame(() => { go(); requestAnimationFrame(go); });
    if (window.ResizeObserver) { const ro = new ResizeObserver(go); ro.observe(node); setTimeout(() => ro.disconnect(), 4000); }
    return node;
  }
  const esc = s => String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const pct = (a, b) => Math.max(0, Math.min(100, b ? a / b * 100 : 0));
  const COMBAT_MODES = { COMBAT: 1, COMBAT_ITEMS: 1, ENCOUNTER: 1 };

  function choiceBtn(c, onPick) {
    const b = el('button', 'ch' + (c.watch ? ' watch' : ''), c.label); b.disabled = !c.enabled; b.dataset.i = c.i;
    b.addEventListener('click', () => onPick(c.i)); return b;
  }
  function groupTalk(choices) {
    const groups = UI.talkGroups.map(([name]) => ({ name, items: [] })); const other = { name: UI.otherGroup, items: [] }; const tail = [];
    for (const c of choices) {
      if (/^(Leave|Back|Done|Goodbye|Walk away)\b/i.test(c.label)) { tail.push(c); continue; }
      const gi = UI.talkGroups.findIndex(([, re]) => re.test(c.label)); (gi >= 0 ? groups[gi] : other).items.push(c);
    }
    return { groups: groups.concat([other]).filter(g => g.items.length), tail };
  }

  function lightbox(src, cap) {
    const lb = el('div', 'lightbox'); const im = el('img'); im.src = src; im.alt = cap || ''; lb.appendChild(im);
    if (cap) lb.appendChild(el('div', 'cap', cap));
    const k = e => { if (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ') { e.stopPropagation(); e.preventDefault(); close(); } };
    const close = () => { lb.remove(); document.removeEventListener('keydown', k, true); };
    lb.addEventListener('click', close); document.addEventListener('keydown', k, true);
    document.body.appendChild(lb);
  }
  // Index of the choice that closes/backs out of a scene (Close beats Back so menus exit fully).
  function closeIndex(scene) {
    const res = [/^Close\b/i, /^(Leave|Done|Walk away|Goodbye)\b/i, /^(Back|Return)\b/i, /^Continue\b/i];
    for (const re of res) { const i = scene.choices.findIndex(c => c.enabled && re.test(c.label)); if (i >= 0) return i; }
    return -1;
  }
  // Wide event picture (road / street encounters); tap for the full portrait.
  function eventPic(p, who, cap) {
    const A = JOETOPIA_ART; if (!A.events || !A.events[who]) return null;
    const ev = el('img', 'evpic'); ev.src = A.events[who]; ev.alt = cap; ev.title = 'Tap to enlarge'; ev.dataset.art = who;
    ev.onerror = () => ev.remove();
    ev.addEventListener('click', () => lightbox(A.portraits[who] || ev.src, cap));
    p.appendChild(ev); p.classList.add('has-event'); return ev;
  }
  // Generic engine-scene panel. opts: {onPick, nameInput, kind}
  function showScene(scene, st, opts) {
    const ov = $('#overlay'), p = $('#panel'); ov.classList.remove('hidden'); p.className = ''; p.innerHTML = '';
    const isBattle = COMBAT_MODES[scene.mode] || (scene.mode === 'STREET' && scene.choices.some(c => /⚔/.test(c.label)));
    if (isBattle) return showBattle(scene, st, opts);
    const head = el('div', 'ph'); head.appendChild(el('span', null, scene.title)); p.appendChild(head);
    const ci = closeIndex(scene);
    if (ci >= 0 && !/^Continue/i.test(scene.choices[ci].label)) { const x = el('button', 'x', '✕'); x.title = scene.choices[ci].label + ' (Esc)'; x.setAttribute('aria-label', scene.choices[ci].label); x.addEventListener('click', () => opts.onPick(ci, '')); head.appendChild(x); }
    if (scene.mode === 'TITLE' && JOETOPIA_ART.title) { const im = el('img', 'title-art'); im.src = JOETOPIA_ART.title; im.alt = ''; p.insertBefore(im, head); }
    const who = scene.mode === 'TALK' ? st.talk : scene.mode === 'STREET' ? JArt.streetArtId(st.streetArt || st.street) : null; // talk partner / street encounter
    if (who && JOETOPIA_ART.faces[who]) {
      const im = el('img', 'face'); im.src = JOETOPIA_ART.faces[who]; im.alt = 'Portrait'; im.title = 'Tap to enlarge';
      im.onerror = () => im.remove();
      if (JOETOPIA_ART.portraits[who]) im.addEventListener('click', () => lightbox(JOETOPIA_ART.portraits[who], scene.title.split(':')[0]));
      head.prepend(im); p.classList.add('talk-face');
    }
    if (who) eventPic(p, who, scene.title.split(':')[0]); // road / street encounter: event picture
    const text = el('div', 'pt', scene.text); p.appendChild(text); stickBottom(text);
    let input = null;
    if (scene.mode === 'CREATE_NAME') {
      input = el('input', 'nameinput'); input.id = 'nameInput'; input.maxLength = 20; input.placeholder = 'Your name'; input.value = opts.lastName || '';
      input.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); opts.onPick(0, input.value.trim()); } });
      p.appendChild(input);
    }
    const list = el('div', 'pc' + (scene.mode.startsWith('CREATE') || scene.mode === 'TITLE' ? ' big' : ''));
    const choices = scene.choices.map((c, i) => Object.assign({ i }, c));
    const pick = i => opts.onPick(i, input ? input.value.trim() : '');
    if ((scene.mode === 'TALK' || scene.mode === 'MINGLE') && choices.length > 7) {
      const { groups, tail } = groupTalk(choices);
      groups.forEach((g, gi) => {
        const d = el('details', 'grp'); if (gi === 0) d.open = true;
        const s = el('summary', null); s.innerHTML = `<span>${esc(g.name)}</span><small style="color:var(--dim)">${g.items.length}</small>`; d.appendChild(s);
        const gl = el('div', 'gl'); g.items.forEach(c => gl.appendChild(choiceBtn(c, pick))); d.appendChild(gl); list.appendChild(d);
      });
      tail.forEach(c => list.appendChild(choiceBtn(c, pick)));
    } else choices.forEach(c => list.appendChild(choiceBtn(c, pick)));
    p.appendChild(list);
    setTimeout(() => { (input || list.querySelector('button:not(:disabled),summary') || p).focus(); }, 0);
  }

  // ---------- battle ----------
  let battleSub = null; let battleAnim = null;
  function categorize(scene) {
    const B = UI.battle, cats = { attack: [], skill: [], item: [], talk: [], flee: [] };
    scene.choices.forEach((c, i) => {
      const o = Object.assign({ i }, c);
      if (scene.mode === 'COMBAT_ITEMS') { cats.item.push(o); return; }
      if (B.flee.test(c.label)) cats.flee.push(o);
      else if (B.item.test(c.label)) cats.item.push(o);
      else if (B.skill.test(c.label)) cats.skill.push(o);
      else if (B.attack.test(c.label)) cats.attack.push(o);
      else cats.talk.push(o);
    });
    return cats;
  }
  function chips(st) {
    const out = []; const c = st.combat;
    if (c) {
      if (c.stunned > 0) out.push(['Stunned ' + c.stunned, 'good']); if (c.dazzled > 0) out.push(['Dazzled ' + c.dazzled, 'good']);
      if (c.blinded > 0) out.push(['Blinded ' + c.blinded, 'good']); if (c.defDown > 0) out.push(['DEF down ' + c.defDown, 'good']);
      if (c.enraged) out.push(['Enraged', 'bad']); if (c.guards > 0) out.push(['+' + c.guards + ' guards', 'bad']);
      if (c.spar) out.push(['Sparring', '']); if (c.ramirez > 0) out.push(['Ramirez ' + c.ramirez, 'good']);
    }
    return out;
  }
  function showBattle(scene, st, opts) {
    const p = $('#panel'); p.className = 'battle'; p.innerHTML = '';
    const c = st.combat, enc = st.encounter;
    const ename = c ? c.enemy : enc ? enc.enemy : scene.title.replace(/^(Battle|Encounter):\s*/, '').replace(/\s+—.*$/, '');
    const eid = c ? c.enemyId : enc ? enc.enemyId : ename.toLowerCase();
    const artId = JArt.enemyArtId(eid, ename, opts.encArt);
    const head = el('div', 'ph'); head.textContent = scene.mode === 'ENCOUNTER' || scene.mode === 'STREET' ? '⚠ ' + scene.title : '⚔ ' + scene.title + (c ? '  · Round ' + (c.turn + 1) : ''); p.appendChild(head);
    if (opts.encArt && (scene.mode === 'STREET' || (c && c.turn === 0 && /^street_/.test(opts.encArt)))) { const ev = eventPic(p, opts.encArt, scene.title.split(':')[0]); if (ev) ev.classList.add('short'); }
    const arena = el('div', 'arena'); const cv = el('canvas'); cv.width = 640; cv.height = 220; arena.appendChild(cv);
    if (artId && JOETOPIA_ART.portraits[artId]) { cv.dataset.art = artId; cv.title = 'Tap the enemy to enlarge'; cv.style.cursor = 'zoom-in'; cv.addEventListener('click', () => lightbox(JOETOPIA_ART.portraits[artId], ename)); }
    const eb = el('div', 'ebox'); eb.innerHTML = `<b>${esc(ename)}</b>` + (c ? `<br><span class="bar hp"><i style="width:${pct(c.hp, c.maxHp)}%"></i></span> ${c.hp}/${c.maxHp}` : '');
    const ch = el('div', 'chips'); chips(st).forEach(([t, k]) => ch.appendChild(el('span', 'chip ' + k, t))); eb.appendChild(ch);
    const pb = el('div', 'pbox'); pb.innerHTML = `<b>${esc(st.name)}</b> Lv${st.level}<br>HP <span class="bar hp"><i style="width:${pct(st.hp, st.maxHp)}%"></i></span> ${st.hp}/${st.maxHp}<br>MP <span class="bar mp"><i style="width:${pct(st.mp, st.maxMp)}%"></i></span> ${st.mp}/${st.maxMp}`;
    const pc = el('div', 'chips'); (st.effects || []).forEach(e => pc.appendChild(el('span', 'chip ' + (e.poison ? 'bad' : e.regen ? 'good' : ''), e.name + ' ' + e.left))); if (c && c.defending) pc.appendChild(el('span', 'chip good', 'Defending')); pb.appendChild(pc);
    arena.appendChild(eb); arena.appendChild(pb); p.appendChild(arena);
    const text = scene.text.split('\n').filter(l => !/^(.*: HP \d+\/\d+|You: HP|HP \d+\/\d+\s+MP)/.test(l.trim())).join('\n').replace(/^\n+/, '');
    p.appendChild(stickBottom(el('div', 'pt', text)));
    const cats = categorize(scene);
    const defs = [['attack', '⚔ Attack'], ['skill', '✦ Skills'], ['item', '🎒 Items'], ['talk', '💬 Talk'], ['flee', '🏃 Flee']];
    const cmds = el('div', 'cmds'); const sub = el('div', 'sub');
    if (scene.mode === 'COMBAT_ITEMS') battleSub = 'item';
    else if (battleSub === 'item') battleSub = null;
    const openSub = (k) => {
      battleSub = k; sub.innerHTML = ''; cmds.querySelectorAll('.cmd').forEach(b => b.classList.toggle('sel', b.dataset.k === k));
      cats[k].forEach(o => sub.appendChild(choiceBtn(o, i => opts.onPick(i, ''))));
      const f = sub.querySelector('button:not(:disabled)'); if (f) f.focus();
    };
    defs.forEach(([k, name], idx) => {
      const b = el('button', 'cmd', name + (cats[k].length > 1 ? ' ▾' : '')); b.dataset.k = k; b.disabled = !cats[k].length || !cats[k].some(o => o.enabled);
      b.title = (idx + 1) + ': ' + cats[k].map(o => o.label).join(' / ');
      b.addEventListener('click', () => {
        const only = cats[k].length === 1 ? cats[k][0] : null;
        if (only && scene.mode !== 'COMBAT_ITEMS' && (k === 'flee' || k === 'item' || scene.mode !== 'COMBAT')) { opts.onPick(only.i, ''); return; } // one option: act immediately (e.g. Flee, Use item)
        openSub(k);
      });
      cmds.appendChild(b);
    });
    p.appendChild(cmds); p.appendChild(sub);
    if (battleSub && cats[battleSub] && cats[battleSub].length) openSub(battleSub); else setTimeout(() => { const f = cmds.querySelector('.cmd:not(:disabled)'); if (f) f.focus(); }, 0);
    // animate arena
    const g = cv.getContext('2d'); const biome = (JMap.info(st.node) || {}).biome || 'forest';
    cancelAnimationFrame(battleAnim);
    // draw the player bigger
    const pframe = (t) => { if (!cv.isConnected) return; JArt.battleBg(g, biome, 640, 220); JArt.enemySprite(g, eid, ename, 640, 220, t, opts.encArt); g.save(); g.translate(70, 60); g.scale(3, 3); JArt.playerSprite(g, 0, 10, 'right', st); g.restore(); if (c && c.ramirez > 0 && !c.spar) { g.save(); g.translate(160, 50); g.scale(2.6, 2.6); JArt.npcSprite(g, 'ramirez', 0, 10, 'right'); g.restore(); } battleAnim = requestAnimationFrame(pframe); };
    battleAnim = requestAnimationFrame(pframe);
  }
  function hideOverlay() { $('#overlay').classList.add('hidden'); $('#panel').innerHTML = ''; cancelAnimationFrame(battleAnim); }
  function overlayOpen() { return !$('#overlay').classList.contains('hidden'); }

  // ---------- dropdowns ----------
  function closeDD() { document.querySelectorAll('.dd.open').forEach(d => d.classList.remove('open')); }
  function fillDD(menu, items) { // items: [{label, on, disabled, info, hr}]
    menu.innerHTML = '';
    for (const it of items) {
      if (it.hr) { menu.appendChild(el('hr')); continue; }
      if (it.info) { menu.appendChild(el('div', 'info', it.info)); continue; }
      const b = el('button', 'item', it.label);
      if (it.img) { const im = el('img', 'ico'); im.src = it.img; im.alt = ''; im.onerror = () => im.remove(); b.prepend(im); } b.disabled = !!it.disabled; b.addEventListener('click', () => { closeDD(); it.on(); }); menu.appendChild(b);
    }
  }
  document.addEventListener('click', e => { if (!e.target.closest('.dd')) closeDD(); });

  // ---------- HUD / messages ----------
  function hud(st) {
    const h = $('#hud');
    if (!st || !st.name || st.mode === 'TITLE' || st.mode.startsWith('CREATE')) { h.innerHTML = '<b>Joetopia: Ashes of Canaan</b>'; return; }
    h.innerHTML = `<span><b>${esc(st.name)}</b> Lv${st.level} ${esc(st.cls)}</span>` +
      `<span>HP <span class="bar hp"><i style="width:${pct(st.hp, st.maxHp)}%"></i></span> ${st.hp}/${st.maxHp}</span>` +
      `<span>MP <span class="bar mp"><i style="width:${pct(st.mp, st.maxMp)}%"></i></span> ${st.mp}/${st.maxMp}</span>` +
      `<span>💰 ${st.credits}</span><span>👁 ${st.views} <small>${esc(st.viewsTier)}</small>${st.streaming ? ' <span class="livebadge">LIVE</span>' : ''}</span>` +
      `<span>📍 ${esc(JMap.placeName(st.node))} <small>· ${esc(st.region)} (${esc(st.regionKind)})</small></span>` + (st.points ? `<span style="color:var(--ok)">+${st.points} stat pts</span>` : '');
  }
  let msgQueue = [], msgDone = null;
  // pic (optional): an entry of JOETOPIA_ART.logArt, shown above the text; tap it to enlarge.
  function showMsg(text, done, pic) { if (!text) return; msgQueue.push({ text, pic }); if (done) msgDone = done; if (msgQueue.length === 1) renderMsg(); }
  function renderMsg() {
    const m = $('#msg'); m.querySelectorAll('img.msgpic').forEach(i => i.remove());
    if (!msgQueue.length) { m.classList.add('hidden'); const d = msgDone; msgDone = null; if (d) d(); return; }
    const { text, pic } = msgQueue[0]; $('#msgText').textContent = text;
    const A = JOETOPIA_ART;
    if (pic && A.events[pic.id]) {
      const im = el('img', 'msgpic' + (pic.small ? ' small' : '')); im.src = pic.small ? A.faces[pic.id] : A.events[pic.id]; im.dataset.art = pic.id; im.alt = ''; im.title = 'Tap to enlarge';
      im.onerror = () => im.remove();
      im.addEventListener('click', e => { e.stopPropagation(); lightbox(A.portraits[pic.id], ''); });
      m.insertBefore(im, $('#msgText'));
    }
    m.classList.remove('hidden'); m.scrollTop = 0;
  }
  function msgPic() { return msgQueue.length && msgQueue[0].pic || null; }
  function nextMsg() { msgQueue.shift(); renderMsg(); }
  function clearMsg() { msgQueue = []; msgDone = null; $('#msg').classList.add('hidden'); }
  function msgOpen() { return msgQueue.length > 0; }
  $('#msg').addEventListener('click', nextMsg);
  function toast(t) { const d = el('div', null, t); $('#toast').appendChild(d); setTimeout(() => d.remove(), 2700); }
  function banner(title, sub) { const b = $('#banner'); b.innerHTML = esc(title) + (sub ? `<small>${esc(sub)}</small>` : ''); b.classList.add('show'); clearTimeout(banner.t); banner.t = setTimeout(() => b.classList.remove('show'), 2600); }
  function prompt(t) { $('#prompt').textContent = t || ''; }

  window.JUI = { lightbox, closeIndex, showScene, hideOverlay, overlayOpen, fillDD, closeDD, hud, showMsg, nextMsg, msgOpen, msgPic, clearMsg, toast, banner, prompt, categorize, groupTalk };
})();
