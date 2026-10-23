// Map layer: turns an engine place + its probed choices into a walkable 20x15 tile room.
(function () {
  const W = 20, H = 15, T = JArt.T;
  const WORLD = window.JOETOPIA_WORLD, MAPS = window.JOETOPIA_MAPS || {}, UI = window.JOETOPIA_UI;
  const TOP = [2, 4, 6, 8, 11, 13, 15, 17], SIDE = [4, 6, 8, 10, 12];
  const SLOTS = []; for (const y of [4, 7, 10]) for (const x of [3, 6, 9, 12, 15]) SLOTS.push([x, y]);
  SLOTS.sort((a, b) => Math.abs(a[0] - 9.5) - Math.abs(b[0] - 9.5) || a[1] - b[1]);
  const OUTDOOR = { city: 1, village: 1, farm: 1, forest: 1, wilds: 1, cave: 1 };

  function info(node) { return WORLD[node] || { name: node, biome: 'interior', parent: null, region: '', tier: 1, kind: 'country' }; }
  function placeName(node) { return info(node).name; }

  function defaultExitSlots() {
    const s = []; TOP.forEach(x => s.push([x, 1, 'N']));
    SIDE.forEach(y => { s.push([0, y, 'W']); s.push([W - 1, y, 'E']); });
    return s;
  }
  function inward(x, y, side) { return side === 'N' ? [x, y + 1] : side === 'S' ? [x, y - 1] : side === 'W' ? [x + 1, y] : [x - 1, y]; }

  function spotKind(label) { for (const [k, re] of UI.spotIcons) if (re.test(label)) return k; return 'spot'; }

  function build(node, probe, choices) {
    const inf = info(node), biome = inf.biome, custom = MAPS[node];
    const grid = []; // 'wall','floor','floor2','decor','water','door'
    const seed = JArt.hash(node);
    const rand = JArt.rng(seed);
    if (custom && custom.rows) {
      for (let y = 0; y < H; y++) { grid.push([]); for (let x = 0; x < W; x++) { const ch = (custom.rows[y] || '')[x] || '#'; grid[y].push(ch === '#' ? 'wall' : ch === 'D' ? 'decor' : ch === '~' ? 'water' : ch === ',' ? 'floor2' : 'floor'); } }
    } else {
      for (let y = 0; y < H; y++) { grid.push([]); for (let x = 0; x < W; x++) {
        const edge = y <= 1 || y === H - 1 || x === 0 || x === W - 1;
        grid[y].push(edge ? 'wall' : (rand() < 0.18 ? 'floor2' : 'floor'));
      } }
    }
    const objs = [];
    const moves = probe.filter(p => p.kind === 'move');
    const rest = probe.filter(p => p.kind !== 'move');
    // choose which exit is "back" (bottom door)
    let back = moves.find(m => m.target === inf.parent) || moves.find(m => /back|leave|return|retreat|climb back|down the|out to the plaza/i.test(m.label)) || moves[moves.length - 1];
    const exitSlots = (custom && custom.exits) ? custom.exits.slice() : defaultExitSlots();
    const backSlot = (custom && custom.back) || [9, H - 1, 'S'];
    const reserved = new Set();
    const key = (x, y) => x + ',' + y;
    for (const m of moves) {
      let slot = m === back ? backSlot : exitSlots.shift();
      if (!slot) continue; // more exits than doors: still listed in the Here menu
      const [x, y, side] = slot; grid[y][x] = 'door';
      const [ix, iy] = inward(x, y, side); if (grid[iy][ix] === 'wall' || grid[iy][ix] === 'decor' || grid[iy][ix] === 'water') grid[iy][ix] = 'floor';
      reserved.add(key(ix, iy));
      objs.push({ type: 'exit', x, y, side, i: m.i, target: m.target, label: m.label, name: placeName(m.target), spawn: [ix, iy] });
    }
    const slots = (custom && custom.slots) ? custom.slots.slice() : SLOTS.slice();
    const order = { talk: 0, shop: 1, fight: 2, event: 3, local: 4, mingle: 5 };
    rest.slice().sort((a, b) => (order[a.kind] - order[b.kind]) || a.i - b.i).forEach(p => {
      const s = slots.shift(); if (!s) return;
      const [x, y] = s; grid[y][x] = 'floor';
      const o = { type: p.kind, x, y, i: p.i, target: p.target, label: p.label, name: p.name || p.label };
      if (p.kind === 'local') { o.icon = spotKind(p.label); const ns = (JOETOPIA_UI.npcSpots || []).find(([re]) => re.test(p.label)); if (ns) o.npc = ns[1]; }
      objs.push(o);
      for (const [dx, dy] of [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) reserved.add(key(x + dx, y + dy));
    });
    // generated decor, kept out of the way of doors and people
    if (!(custom && custom.rows)) {
      const n = OUTDOOR[biome] ? 12 : 7;
      for (let k = 0; k < n * 3 && n > 0; k++) {
        const x = 1 + (rand() * (W - 2) | 0), y = 3 + (rand() * (H - 5) | 0);
        if (reserved.has(key(x, y)) || objs.some(o => Math.abs(o.x - x) <= 1 && Math.abs(o.y - y) <= 1)) continue;
        if (x === 9 || x === 10 || y === 2 || y === H - 2 || x === 1 || x === W - 2) continue;
        grid[y][x] = 'decor';
      }
    }
    const map = { node, biome, inf, grid, objs, W, H, variant: [] };
    for (let y = 0; y < H; y++) { map.variant.push([]); for (let x = 0; x < W; x++) map.variant[y].push(JArt.hash(node + x + ':' + y) % 97); }
    // guarantee everything is reachable from the bottom door
    const start = (objs.find(o => o.type === 'exit' && o.x === backSlot[0] && o.y === backSlot[1]) || {}).spawn || [9, H - 2];
    if (!allReachable(map, start)) { for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (grid[y][x] === 'decor' && !(custom && custom.rows)) grid[y][x] = 'floor'; }
    map.start = start;
    return map;
  }
  function objAt(map, x, y) { return map.objs.find(o => o.x === x && o.y === y); }
  function walkable(map, x, y) {
    if (x < 0 || y < 0 || x >= W || y >= H) return false;
    const t = map.grid[y][x]; if (t !== 'floor' && t !== 'floor2' && t !== 'door') return false;
    const o = objAt(map, x, y); return !o || o.type === 'exit';
  }
  function bfs(map, sx, sy, goal) {
    const prev = {}, q = [[sx, sy]], k = (x, y) => x + ',' + y; prev[k(sx, sy)] = null;
    while (q.length) {
      const [x, y] = q.shift(); if (goal(x, y)) { const path = []; let c = k(x, y); while (c && prev[c] !== undefined) { const [a, b] = c.split(',').map(Number); path.unshift([a, b]); c = prev[c]; } path.shift(); return path; }
      for (const [dx, dy] of [[0, -1], [1, 0], [0, 1], [-1, 0]]) {
        const nx = x + dx, ny = y + dy, nk = k(nx, ny); if (nk in prev) continue;
        const t = map.grid[ny] && map.grid[ny][nx];
        if (t === 'door') { if (goal(nx, ny)) { prev[nk] = k(x, y); q.push([nx, ny]); } continue; }
        if (!walkable(map, nx, ny)) continue; prev[nk] = k(x, y); q.push([nx, ny]);
      }
    }
    return null;
  }
  function allReachable(map, start) {
    for (const o of map.objs) {
      const goal = o.type === 'exit' ? ((x, y) => x === o.spawn[0] && y === o.spawn[1]) : ((x, y) => Math.abs(x - o.x) + Math.abs(y - o.y) === 1);
      if (!bfs(map, start[0], start[1], goal)) return false;
    }
    return true;
  }

  function render(g, map, t, opts) {
    const { grid, biome, variant } = map;
    for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
      const ty = grid[y][x];
      JArt.drawTile(g, biome, ty === 'decor' ? 'decor' : ty, x * T, y * T, variant[y][x]);
    }
    // exits: arrows + labels
    for (const o of map.objs) if (o.type === 'exit') {
      const px = o.x * T, py = o.y * T, a = (Math.sin(t / 250) + 1) * 0.5;
      g.fillStyle = `rgba(255,255,255,${0.35 + a * 0.4})`; g.beginPath();
      const cx = px + 16, cy = py + 16;
      if (o.side === 'N') { g.moveTo(cx, cy - 8); g.lineTo(cx - 6, cy); g.lineTo(cx + 6, cy); }
      else if (o.side === 'S') { g.moveTo(cx, cy + 8); g.lineTo(cx - 6, cy); g.lineTo(cx + 6, cy); }
      else if (o.side === 'W') { g.moveTo(cx - 8, cy); g.lineTo(cx, cy - 6); g.lineTo(cx, cy + 6); }
      else { g.moveTo(cx + 8, cy); g.lineTo(cx, cy - 6); g.lineTo(cx, cy + 6); }
      g.fill();
    }
    // objects + player, sorted by y
    const draw = map.objs.filter(o => o.type !== 'exit').map(o => ({ y: o.y, f: () => drawObj(g, map, o, t) }));
    if (opts.player) draw.push({ y: opts.player.ry, f: () => JArt.playerSprite(g, opts.player.rx * T, opts.player.ry * T, opts.player.dir, opts.status) });
    if (opts.encounter && opts.player) { // road encounter: its sprite steps up beside you
      const ex = opts.player.rx + (opts.player.rx < W - 2 ? 1 : -1), ey = opts.player.ry;
      draw.push({ y: ey, f: () => JArt.npcSprite(g, opts.encounter, ex * T, ey * T, 'left') });
    }
    draw.sort((a, b) => a.y - b.y).forEach(d => d.f());
    if (opts.labels) for (const o of map.objs) label(g, o, opts.focus === o);
    else if (opts.focus) label(g, opts.focus, true);
    if (opts.target) { g.strokeStyle = '#ffffffaa'; g.lineWidth = 2; g.strokeRect(opts.target[0] * T + 2, opts.target[1] * T + 2, T - 4, T - 4); }
  }
  function drawObj(g, map, o, t) {
    const x = o.x * T, y = o.y * T;
    if (o.type === 'talk' || o.npc) JArt.npcSprite(g, o.npc || o.target, x, y, 'down');
    else if (o.type === 'shop') JArt.objectIcon(g, 'shop', x, y, map.biome);
    else if (o.type === 'mingle') JArt.objectIcon(g, 'crowd', x, y, map.biome);
    else if (o.type === 'fight') JArt.objectIcon(g, 'fight', x, y, map.biome);
    else if (o.type === 'event') JArt.objectIcon(g, 'event', x, y, map.biome);
    else JArt.objectIcon(g, o.icon || 'spot', x, y, map.biome);
    if (o.type === 'talk' || o.npc || o.type === 'fight') { const b = Math.sin(t / 300 + o.x) * 2; g.fillStyle = o.type !== 'fight' ? '#ffd1f5' : '#ff6b6b'; g.beginPath(); g.moveTo(x + 16, y - 2 + b); g.lineTo(x + 12, y - 7 + b); g.lineTo(x + 20, y - 7 + b); g.fill(); }
  }
  function shortName(o) {
    if (o.type === 'exit') return o.name;
    if (o.type === 'talk') return o.name;
    if (o.type === 'mingle') return 'Locals';
    return o.label.replace(/^[^\w(]+/u, '').replace(/\s*\(.*$/, '').replace(/:.*$/, '').slice(0, 26);
  }
  function label(g, o, hi) {
    const txt = shortName(o); if (!txt) return;
    g.font = (hi ? 'bold ' : '') + '11px system-ui,sans-serif'; const w = g.measureText(txt).width + 8;
    let x = o.x * T + 16 - w / 2, y = o.y * T - (o.type === 'talk' ? 20 : 12);
    if (o.type === 'exit') y = o.side === 'N' ? o.y * T + 34 : o.side === 'S' ? o.y * T - 14 : o.y * T - 12;
    if (o.type === 'exit' && o.side === 'W') x = 2; if (o.type === 'exit' && o.side === 'E') x = W * T - w - 2;
    x = Math.max(1, Math.min(W * T - w - 1, x)); y = Math.max(1, y);
    g.fillStyle = hi ? '#ff4fd8ee' : '#000000bb'; g.fillRect(x, y, w, 14); g.fillStyle = '#fff'; g.textAlign = 'left'; g.textBaseline = 'top'; g.fillText(txt, x + 4, y + 1.5);
  }
  window.JMap = { W, H, build, render, walkable, objAt, bfs, info, placeName, inward, shortName };
})();
