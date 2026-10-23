// Art loader + procedural placeholders. Real PNGs from data/art.js win; null/missing -> drawn here.
(function () {
  const A = window.JOETOPIA_ART, T = A.tileSize || 32;
  const cache = {};
  function img(path) {
    if (!path) return null;
    let c = cache[path];
    if (!c) {
      c = cache[path] = { ok: false, im: new Image() };
      c.im.onload = () => { c.ok = true; };
      c.im.onerror = () => { c.ok = false; c.failed = true; };
      c.im.src = path;
    }
    return c.ok ? c.im : null;
  }
  function hash(s) { let h = 2166136261; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); } return h >>> 0; }
  function rng(seed) { let s = seed || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return ((s >>> 0) % 10000) / 10000; }; }
  function hsl(h, s, l) { return `hsl(${h % 360},${s}%,${l}%)`; }
  const pal = b => A.palette[b] || A.palette.interior;

  // ---------- tiles ----------
  function drawTile(g, biome, type, x, y, variant) {
    const t = A.tiles[biome] && A.tiles[biome][type === 'floor2' ? 'floor' : type === 'water' ? 'floor' : type];
    const im = type !== 'water' && img(t);
    if (im) { g.drawImage(im, x, y, T, T); if (type === 'floor2') { g.fillStyle = '#ffffff10'; g.fillRect(x, y, T, T); } return; }
    proceduralTile(g, biome, type, x, y, variant || 0);
  }
  function proceduralTile(g, biome, type, x, y, v) {
    const p = pal(biome); const r = rng(v * 7919 + 13);
    if (type === 'floor' || type === 'floor2') {
      g.fillStyle = type === 'floor2' ? p.floor2 : p.floor; g.fillRect(x, y, T, T);
      g.fillStyle = '#00000022';
      if (/city|castle|interior_city/.test(biome)) { g.fillRect(x, y + T - 1, T, 1); g.fillRect(x + T - 1, y, 1, T); }
      else if (biome === 'interior') { g.fillRect(x, y + 15, T, 1); g.fillRect(x, y + 31, T, 1); }
      else if (/club/.test(biome)) { if ((v & 1) === 0) { g.fillStyle = p.trim + '22'; g.fillRect(x + 2, y + 2, T - 4, T - 4); } }
      else { for (let i = 0; i < 4; i++) { g.fillStyle = i % 2 ? '#ffffff12' : '#00000020'; g.fillRect(x + (r() * 28 | 0), y + (r() * 28 | 0), 3, 2); } }
      return;
    }
    if (type === 'water') {
      g.fillStyle = biome === 'cave' ? '#1c3a5a' : '#2a5a8a'; g.fillRect(x, y, T, T);
      g.fillStyle = '#ffffff30'; g.fillRect(x + 4 + (v % 3) * 6, y + 10, 8, 2); g.fillRect(x + 14, y + 22, 9, 2); return;
    }
    if (type === 'wall') {
      g.fillStyle = p.wall; g.fillRect(x, y, T, T);
      if (biome === 'city' || biome === 'interior_city') {
        g.fillStyle = '#ffffff10'; g.fillRect(x, y, T, 2);
        for (let i = 0; i < 2; i++) for (let j = 0; j < 2; j++) { g.fillStyle = r() < 0.55 ? (r() < 0.5 ? p.light : p.trim) + 'aa' : '#00000055'; g.fillRect(x + 5 + i * 14, y + 5 + j * 14, 8, 8); }
      } else if (biome === 'club' || biome === 'cavern_club') {
        g.fillStyle = p.trim; g.fillRect(x, y + 26, T, 2); g.fillStyle = p.light + '55'; g.fillRect(x, y + 6, T, 1);
      } else if (biome === 'village' || biome === 'interior') {
        g.fillStyle = p.trim; for (let i = 0; i < 4; i++) g.fillRect(x, y + i * 8, T, 1);
        g.fillStyle = '#00000030'; g.fillRect(x + (v % 2 ? 0 : 16), y, 1, T);
      } else if (biome === 'forest' || biome === 'farm') {
        g.fillStyle = '#0d1f0d'; g.fillRect(x, y, T, T);
        g.fillStyle = biome === 'farm' ? '#5a7a2a' : '#2a5a22'; g.beginPath(); g.arc(x + 10, y + 12, 11, 0, 7); g.arc(x + 23, y + 18, 11, 0, 7); g.fill();
        g.fillStyle = '#ffffff10'; g.beginPath(); g.arc(x + 9, y + 9, 5, 0, 7); g.fill();
      } else {
        g.fillStyle = p.trim + '66'; g.fillRect(x + 2, y + 3, 12, 8); g.fillRect(x + 17, y + 14, 12, 8); g.fillRect(x + 4, y + 24, 10, 6);
      }
      return;
    }
    if (type === 'door') {
      proceduralTile(g, biome, 'floor', x, y, v);
      g.fillStyle = '#000000aa'; g.fillRect(x + 5, y + 3, 22, 27);
      g.fillStyle = p.light; g.fillRect(x + 5, y + 3, 22, 3); g.fillRect(x + 5, y + 3, 2, 27); g.fillRect(x + 25, y + 3, 2, 27);
      g.fillStyle = p.light + '55'; g.fillRect(x + 8, y + 8, 16, 20);
      return;
    }
    if (type === 'decor') {
      proceduralTile(g, biome, 'floor', x, y, v);
      decor(g, biome, x, y, v);
    }
  }
  function decor(g, b, x, y, v) {
    const p = pal(b); const k = v % 2;
    g.fillStyle = '#00000044'; g.beginPath(); g.ellipse(x + 16, y + 27, 11, 4, 0, 0, 7); g.fill();
    if (b === 'forest' || b === 'cavern_club') { // giant toadstool
      g.fillStyle = '#efe3c8'; g.fillRect(x + 13, y + 14, 6, 13);
      g.fillStyle = b === 'forest' ? (k ? '#d93a3a' : '#c05aff') : p.decor; g.beginPath(); g.ellipse(x + 16, y + 14, 13, 8, 0, Math.PI, 0); g.fill();
      g.fillStyle = '#fff'; g.fillRect(x + 9, y + 9, 3, 3); g.fillRect(x + 19, y + 8, 3, 3); g.fillRect(x + 15, y + 11, 2, 2);
    } else if (b === 'city') { // neon lamp post / bench
      if (k) { g.fillStyle = '#555a70'; g.fillRect(x + 15, y + 6, 3, 21); g.fillStyle = p.light; g.fillRect(x + 11, y + 3, 11, 4); g.fillStyle = p.light + '33'; g.beginPath(); g.arc(x + 16, y + 6, 10, 0, 7); g.fill(); }
      else { g.fillStyle = '#6a4a8a'; g.fillRect(x + 4, y + 16, 24, 5); g.fillStyle = '#3a2a5a'; g.fillRect(x + 6, y + 21, 3, 6); g.fillRect(x + 23, y + 21, 3, 6); g.fillStyle = p.trim; g.fillRect(x + 4, y + 11, 24, 3); }
    } else if (b === 'club') { // speaker stack
      g.fillStyle = '#111'; g.fillRect(x + 6, y + 4, 20, 24); g.fillStyle = '#333'; g.beginPath(); g.arc(x + 16, y + 11, 5, 0, 7); g.arc(x + 16, y + 21, 6, 0, 7); g.fill();
      g.fillStyle = p.trim; g.fillRect(x + 6, y + 4, 20, 2);
    } else if (b === 'village' || b === 'farm') { // barrel / hay
      if (k || b === 'farm') { g.fillStyle = '#d8b84a'; g.fillRect(x + 5, y + 10, 22, 16); g.fillStyle = '#b8983a'; g.fillRect(x + 5, y + 15, 22, 2); g.fillRect(x + 5, y + 21, 22, 2); }
      else { g.fillStyle = '#8b5a2b'; g.fillRect(x + 8, y + 8, 16, 19); g.fillStyle = '#5a3a1a'; g.fillRect(x + 8, y + 12, 16, 2); g.fillRect(x + 8, y + 21, 16, 2); }
    } else if (b === 'cave' || b === 'wilds') { // rock / dead tree
      if (b === 'wilds' && k) { g.strokeStyle = '#2a2420'; g.lineWidth = 3; g.beginPath(); g.moveTo(x + 16, y + 27); g.lineTo(x + 16, y + 8); g.lineTo(x + 9, y + 3); g.moveTo(x + 16, y + 13); g.lineTo(x + 24, y + 6); g.stroke(); }
      else { g.fillStyle = p.decor; g.beginPath(); g.moveTo(x + 4, y + 27); g.lineTo(x + 10, y + 10); g.lineTo(x + 20, y + 7); g.lineTo(x + 28, y + 27); g.fill(); g.fillStyle = b === 'cave' ? '#7cf7ff88' : '#ffffff22'; g.fillRect(x + 14, y + 12, 3, 6); }
    } else if (b === 'castle') { // pillar with blue flame
      g.fillStyle = '#6a6a80'; g.fillRect(x + 10, y + 8, 12, 19); g.fillStyle = '#4a4a60'; g.fillRect(x + 8, y + 5, 16, 4);
      g.fillStyle = '#6ab0ff'; g.beginPath(); g.ellipse(x + 16, y + 3, 4, 5, 0, 0, 7); g.fill();
    } else { // table / shelf
      if (k) { g.fillStyle = '#5a3a20'; g.fillRect(x + 3, y + 4, 26, 22); g.fillStyle = p.light; for (let i = 0; i < 3; i++) g.fillRect(x + 5, y + 7 + i * 7, 22, 2); }
      else { g.fillStyle = p.decor; g.beginPath(); g.ellipse(x + 16, y + 16, 12, 8, 0, 0, 7); g.fill(); g.fillStyle = '#ffffff33'; g.fillRect(x + 12, y + 12, 8, 3); }
    }
  }

  // ---------- people ----------
  const SKIN = ['#f1c9a5', '#d9a77e', '#b07a52', '#8a5a3a', '#6a4028', '#e8b890'];
  const HAIR = ['#2a1a10', '#5a3a1a', '#c9a040', '#111', '#a03020', '#e8e8e8', '#ff4fd8', '#4fe3ff'];
  function person(g, x, y, o) { // o: {toga, seed, dir, tall, cls, glow}
    const r = rng(o.seed || 1); const skin = SKIN[(r() * SKIN.length) | 0], hair = HAIR[(r() * HAIR.length) | 0];
    const s = o.tall ? 1.45 : 1; const top = y + T - 30 * s;
    g.save(); g.translate(x + 16, y + T); g.scale(1, s); g.translate(-16, -T);
    g.fillStyle = '#00000055'; g.beginPath(); g.ellipse(16, 29, 9, 3, 0, 0, 7); g.fill();
    g.fillStyle = '#8b5a2b'; g.fillRect(10, 27, 4, 3); g.fillRect(18, 27, 4, 3);
    g.fillStyle = skin; g.fillRect(11, 23, 3, 4); g.fillRect(18, 23, 3, 4);
    g.fillStyle = o.toga; g.beginPath(); g.moveTo(9, 12); g.lineTo(23, 12); g.lineTo(25, 25); g.lineTo(7, 25); g.fill();
    g.fillStyle = '#ffffff44'; g.beginPath(); g.moveTo(10, 12); g.lineTo(14, 12); g.lineTo(22, 24); g.lineTo(18, 24); g.fill();
    g.fillStyle = skin; g.fillRect(6, 14, 3, 7); g.fillRect(23, 14, 3, 7);
    g.beginPath(); g.arc(16, 8, 6, 0, 7); g.fill();
    g.fillStyle = hair; g.beginPath(); g.arc(16, 6, 6, Math.PI, 0); g.fill();
    if (o.dir !== 'up') { g.fillStyle = '#111'; const dx = o.dir === 'left' ? -2 : o.dir === 'right' ? 2 : 0; g.fillRect(13 + dx, 8, 2, 2); g.fillRect(17 + dx, 8, 2, 2); }
    if (o.glasses) { g.fillStyle = '#000'; g.fillRect(12, 7, 8, 3); }
    g.restore();
    if (o.glow) { g.strokeStyle = o.glow; g.lineWidth = 1; g.strokeRect(x + 1.5, top + 0.5, T - 3, 30 * s); }
  }
  function npcSprite(g, id, x, y, dir) {
    const im = img(A.npcs[id]);
    if (im) { const h = im.height / im.width * T; g.drawImage(im, x, y + T - h, T, h); return; }
    const h = hash(id || 'npc');
    person(g, x, y, { toga: hsl(h, 70, 55), seed: h, dir: dir || 'down', tall: /robert|shamgar|goliath|ramirez/.test(id || ''), glasses: /ramirez|shamgar/.test(id || '') });
  }
  function playerSprite(g, x, y, dir, st) {
    const im = img((A.playerByClass || {})[st && st.clsId]) || img(A.player);
    if (im) { g.drawImage(im, x, y, T, T); return; }
    const toga = (JOETOPIA_UI.togaColors[(st && st.toga || '').toLowerCase()]) || '#2f7bff';
    person(g, x, y, { toga, seed: hash((st && st.name || 'Joe') + 'p'), dir });
    g.fillStyle = '#fff'; g.beginPath(); g.moveTo(x + 16, y - 6); g.lineTo(x + 12, y - 11); g.lineTo(x + 20, y - 11); g.fill();
  }

  // ---------- object markers ----------
  function objectIcon(g, kind, x, y, biome) {
    const im = img(A.objects[kind]);
    if (im) { g.drawImage(im, x, y, T, T); return; }
    proceduralObject(g, kind, x, y, biome);
  }
  function proceduralObject(g, kind, x, y, biome) {
    const p = pal(biome || 'interior');
    g.fillStyle = '#00000055'; g.beginPath(); g.ellipse(x + 16, y + 28, 12, 4, 0, 0, 7); g.fill();
    const glow = (c) => { g.fillStyle = c + '33'; g.beginPath(); g.arc(x + 16, y + 16, 15, 0, 7); g.fill(); };
    switch (kind) {
      case 'shop': g.fillStyle = '#7a4a2a'; g.fillRect(x + 2, y + 14, 28, 14); g.fillStyle = '#ffcc33'; g.fillRect(x + 2, y + 12, 28, 3);
        g.fillStyle = '#e04a4a'; for (let i = 0; i < 4; i++) g.fillRect(x + 2 + i * 7, y + 3, 4, 9); g.fillStyle = '#fff'; for (let i = 0; i < 4; i++) g.fillRect(x + 5.5 + i * 7, y + 3, 3, 9);
        g.fillStyle = '#ffd27a'; g.fillRect(x + 7, y + 18, 5, 5); g.fillStyle = '#6dff9a'; g.fillRect(x + 15, y + 18, 5, 5); g.fillStyle = '#4fe3ff'; g.fillRect(x + 22, y + 18, 5, 5); break;
      case 'crowd': for (let i = 0; i < 3; i++) { const h = hash('c' + i + biome); g.fillStyle = hsl(h, 60, 55); g.fillRect(x + 3 + i * 9, y + 14 - (i % 2) * 3, 8, 13); g.fillStyle = SKIN[h % 6]; g.beginPath(); g.arc(x + 7 + i * 9, y + 10 - (i % 2) * 3, 4, 0, 7); g.fill(); }
        g.fillStyle = '#fff'; g.fillRect(x + 22, y + 0, 9, 6); g.fillStyle = '#000'; g.fillRect(x + 24, y + 2, 5, 1); break;
      case 'fight': glow('#ff3b3b'); g.strokeStyle = '#ddd'; g.lineWidth = 3; g.beginPath(); g.moveTo(x + 6, y + 6); g.lineTo(x + 26, y + 26); g.moveTo(x + 26, y + 6); g.lineTo(x + 6, y + 26); g.stroke();
        g.fillStyle = '#8b5a2b'; g.fillRect(x + 4, y + 22, 6, 6); g.fillRect(x + 22, y + 22, 6, 6); break;
      case 'event': glow('#ffcc33'); g.fillStyle = '#ffcc33'; g.font = 'bold 22px sans-serif'; g.textAlign = 'center'; g.fillText('!', x + 16, y + 24); break;
      case 'drink': g.fillStyle = '#5a3a20'; g.fillRect(x + 2, y + 18, 28, 10); g.fillStyle = p.light; g.beginPath(); g.moveTo(x + 9, y + 4); g.lineTo(x + 23, y + 4); g.lineTo(x + 16, y + 12); g.fill(); g.fillRect(x + 15, y + 12, 2, 6); g.fillRect(x + 11, y + 17, 10, 2); break;
      case 'dance': for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) { g.fillStyle = ['#ff4fd8', '#4fe3ff', '#ffcc33', '#6dff9a'][(i + j * 2) % 4]; g.fillRect(x + 2 + i * 10, y + 4 + j * 8, 9, 7); } break;
      case 'rest': g.fillStyle = '#5a3a20'; g.fillRect(x + 3, y + 10, 26, 16); g.fillStyle = '#e8e0d0'; g.fillRect(x + 5, y + 12, 22, 12); g.fillStyle = '#c04a4a'; g.fillRect(x + 12, y + 12, 15, 12); break;
      case 'pray': glow('#ffd27a'); g.fillStyle = '#9a9aaa'; g.fillRect(x + 8, y + 14, 16, 14); g.fillStyle = '#ffd27a'; g.fillRect(x + 15, y + 2, 3, 12); g.fillRect(x + 11, y + 6, 11, 3); break;
      case 'forage': g.fillStyle = '#2a6a2a'; g.beginPath(); g.arc(x + 10, y + 18, 8, 0, 7); g.arc(x + 22, y + 18, 8, 0, 7); g.arc(x + 16, y + 11, 8, 0, 7); g.fill(); g.fillStyle = '#d93a3a'; g.fillRect(x + 8, y + 14, 4, 4); g.fillRect(x + 20, y + 10, 4, 4); break;
      case 'explore': g.fillStyle = '#8b5a2b'; g.fillRect(x + 15, y + 6, 3, 22); g.fillStyle = '#c9a06a'; g.beginPath(); g.moveTo(x + 4, y + 6); g.lineTo(x + 24, y + 6); g.lineTo(x + 29, y + 10); g.lineTo(x + 24, y + 14); g.lineTo(x + 4, y + 14); g.fill(); break;
      case 'books': g.fillStyle = '#5a3a20'; g.fillRect(x + 3, y + 3, 26, 25); for (let i = 0; i < 3; i++) for (let j = 0; j < 6; j++) { g.fillStyle = hsl(j * 50 + i * 20, 55, 50); g.fillRect(x + 5 + j * 4, y + 5 + i * 8, 3, 6); } break;
      case 'lab': g.fillStyle = '#6a6a7a'; g.fillRect(x + 2, y + 18, 28, 10); g.fillStyle = '#6dff9a'; g.beginPath(); g.moveTo(x + 9, y + 4); g.lineTo(x + 13, y + 4); g.lineTo(x + 16, y + 17); g.lineTo(x + 6, y + 17); g.fill(); g.fillStyle = '#ff4fd8'; g.fillRect(x + 20, y + 8, 5, 10); break;
      default: glow('#4fe3ff'); g.fillStyle = '#4fe3ff'; g.beginPath(); for (let i = 0; i < 8; i++) { const a = i * Math.PI / 4, rr = i % 2 ? 4 : 11; g.lineTo(x + 16 + Math.cos(a) * rr, y + 16 + Math.sin(a) * rr); } g.fill();
    }
  }

  // ---------- battle ----------
  function enemySprite(g, id, name, w, h, t) {
    const im = img(A.enemies[id]);
    const cx = w * 0.7, cy = h * 0.52;
    if (im) { const s = Math.min(160 / im.width, 160 / im.height); g.drawImage(im, cx - im.width * s / 2, cy - im.height * s / 2, im.width * s, im.height * s); return; }
    const hh = hash(id || name || 'x'); const r = rng(hh); const col = hsl(hh, 55, 45), col2 = hsl(hh + 40, 60, 62);
    const bob = Math.sin(t / 300) * 4; const R = 46 + (hh % 20);
    g.fillStyle = '#00000066'; g.beginPath(); g.ellipse(cx, cy + R + 8, R, 10, 0, 0, 7); g.fill();
    const humanoid = /noble|guard|bouncer|thug|knight|priest|pastor|cult|draconian|robert|ramirez|morvane|king|bandit|punk|drunk|creep|pickpocket|sailor|brute|squad|dealer|witch|hag|tourist|man|girl|stranger/i.test(id + ' ' + name);
    g.save(); g.translate(cx, cy + bob);
    if (humanoid) {
      g.fillStyle = col; g.beginPath(); g.moveTo(-30, -20); g.lineTo(30, -20); g.lineTo(38, 52); g.lineTo(-38, 52); g.fill();
      g.fillStyle = col2; g.fillRect(-30, -20, 60, 8);
      g.fillStyle = SKIN[hh % 6]; g.beginPath(); g.arc(0, -42, 20, 0, 7); g.fill(); g.fillRect(-44, -14, 12, 40); g.fillRect(32, -14, 12, 40);
      g.fillStyle = /morvane|king/i.test(id + name) ? '#6ab0ff' : /noble/i.test(id + name) ? '#ff2040' : '#111';
      g.fillRect(-10, -46, 6, 6); g.fillRect(4, -46, 6, 6);
      if (/morvane|king|noble/i.test(id + name)) { g.fillStyle = '#ffcc33'; g.beginPath(); g.moveTo(-18, -58); g.lineTo(-12, -72); g.lineTo(-4, -60); g.lineTo(0, -74); g.lineTo(4, -60); g.lineTo(12, -72); g.lineTo(18, -58); g.fill(); }
    } else {
      g.fillStyle = col; g.beginPath();
      const n = 10 + (hh % 6); for (let i = 0; i <= n; i++) { const a = i / n * Math.PI * 2, rr = R * (0.8 + r() * 0.35); g.lineTo(Math.cos(a) * rr, Math.sin(a) * rr * 0.85); } g.fill();
      g.fillStyle = col2; g.beginPath(); g.ellipse(0, 12, R * 0.55, R * 0.35, 0, 0, 7); g.fill();
      g.fillStyle = '#fff'; g.beginPath(); g.arc(-14, -10, 9, 0, 7); g.arc(14, -10, 9, 0, 7); g.fill();
      g.fillStyle = /wolf|ash|ember|fire/i.test(id + name) ? '#ff5a1a' : '#111'; g.beginPath(); g.arc(-13, -9, 4, 0, 7); g.arc(15, -9, 4, 0, 7); g.fill();
      g.fillStyle = '#fff'; for (let i = -2; i <= 2; i++) { g.beginPath(); g.moveTo(i * 7 - 3, 18); g.lineTo(i * 7 + 3, 18); g.lineTo(i * 7, 25); g.fill(); }
    }
    g.restore();
  }
  function battleBg(g, biome, w, h) {
    const im = img(A.battleBg[biome]);
    if (im) { g.drawImage(im, 0, 0, w, h); return; }
    const p = pal(biome); const grd = g.createLinearGradient(0, 0, 0, h); grd.addColorStop(0, p.wall); grd.addColorStop(1, p.floor); g.fillStyle = grd; g.fillRect(0, 0, w, h);
    g.fillStyle = p.floor2; g.beginPath(); g.ellipse(w * 0.7, h * 0.82, w * 0.25, h * 0.1, 0, 0, 7); g.fill();
    g.fillStyle = p.light + '22'; for (let i = 0; i < 12; i++) { const r = rng(i + 3); g.fillRect(r() * w, r() * h * 0.5, 2, 2); }
  }

  // Placeholder export (used by tools/export-placeholders.js to write PNGs for every manifest path).
  function placeholders() {
    const out = {}; const c = document.createElement('canvas'); c.width = T; c.height = T; const g = c.getContext('2d');
    for (const b in A.tiles) for (const type in A.tiles[b]) { const p = A.tiles[b][type]; if (!p) continue; g.clearRect(0, 0, T, T); proceduralTile(g, b, type, 0, 0, type === 'decor' ? 1 : 0); out[p] = c.toDataURL('image/png'); }
    for (const k in A.objects) { const p = A.objects[k]; if (!p) continue; g.clearRect(0, 0, T, T); proceduralObject(g, k, 0, 0, 'interior'); out[p] = c.toDataURL('image/png'); }
    return out;
  }
  window.JArt = { T, img, hash, rng, drawTile, npcSprite, playerSprite, objectIcon, enemySprite, battleBg, person, placeholders, pal };
})();
