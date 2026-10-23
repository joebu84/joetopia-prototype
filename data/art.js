// ART MANIFEST — every picture in the game is looked up here.
// Set any entry to a PNG path (relative to index.html). Leave it null and the game draws a
// built-in placeholder instead, so you can swap art in one file at a time.
// Sizes: tiles 32x32, map sprites 32x32 (tall NPCs may be 32x48), battle enemies ~128x128,
// battle backgrounds 640x220, portraits 96x96. Pixel art is drawn without smoothing.
(function () {
  const biomes = ['city', 'club', 'village', 'farm', 'forest', 'cave', 'cavern_club', 'wilds', 'castle', 'interior', 'interior_city'];
  const tiles = {};
  for (const b of biomes) tiles[b] = {
    floor: `art/tiles/${b}_floor.png`, wall: `art/tiles/${b}_wall.png`,
    decor: `art/tiles/${b}_decor.png`, door: `art/tiles/${b}_door.png`,
  };
  window.JOETOPIA_ART = {
    tileSize: 32,
    tiles,                 // tiles.city.floor = 'art/tiles/my_better_pavement.png' to override one
    // Colours used by the placeholders (and by the map when a tile image is missing).
    palette: {
      city:          { floor: '#2b2e3d', floor2: '#333749', wall: '#1a1030', trim: '#ff4fd8', light: '#4fe3ff', decor: '#8a8fa8' },
      club:          { floor: '#140c24', floor2: '#1d1234', wall: '#0a0614', trim: '#ff2fb3', light: '#7cf7ff', decor: '#5c2d91' },
      village:       { floor: '#4f6b3a', floor2: '#57753f', wall: '#6b4a2f', trim: '#c9a06a', light: '#ffd27a', decor: '#8b5a2b' },
      farm:          { floor: '#6f7f3a', floor2: '#7a8a40', wall: '#4a5d2a', trim: '#c9b26a', light: '#e8d27a', decor: '#a07a3a' },
      forest:        { floor: '#2f4a2a', floor2: '#36552f', wall: '#183018', trim: '#5f8f3f', light: '#ff5a5a', decor: '#d93a3a' },
      cave:          { floor: '#3a3644', floor2: '#423d4e', wall: '#1d1a24', trim: '#6a6478', light: '#7cf7ff', decor: '#5a5468' },
      cavern_club:   { floor: '#1f1a2e', floor2: '#272038', wall: '#12101a', trim: '#7cff6a', light: '#ff4fd8', decor: '#4fe3ff' },
      wilds:         { floor: '#5a5552', floor2: '#625c58', wall: '#2e2a28', trim: '#8a8480', light: '#6ab0ff', decor: '#3a3532' },
      castle:        { floor: '#4a4a5a', floor2: '#525266', wall: '#24243a', trim: '#6ab0ff', light: '#9fd0ff', decor: '#3a3a52' },
      interior:      { floor: '#6b4a32', floor2: '#75513a', wall: '#3e2a1c', trim: '#a8784a', light: '#ffd27a', decor: '#8b5a2b' },
      interior_city: { floor: '#2a2438', floor2: '#322a44', wall: '#17122a', trim: '#4fe3ff', light: '#ff4fd8', decor: '#6a5a9a' },
    },
    player: null,            // one sprite for everyone, e.g. 'art/sprites/player.png'
    playerByClass: {},       // or per class: { BOUNCER: 'art/sprites/player_bouncer.png' }
    // NAMED CHARACTERS. Keyed by the NPC id from the Kotlin engine; the value is the file stem
    // used for every picture of that character (lydia_talk is Elder Lydia).
    //   npcs       map sprite, 32x48 pixel art      art/npcs/<stem>.png
    //   faces      talk-menu / menu thumbnail       art/faces/<stem>.webp   (square, 160px)
    //   portraits  full picture, tap the face       art/portraits/<stem>.webp (512px long side)
    //   busts      battle picture vs. that person   art/busts/<stem>.webp   (square, 256px)
    // Add a character: drop the four files in, add a line here. Override one picture by setting
    // e.g. npcs.robert = 'art/npcs/robert_v2.png' after the loop below.
    characters: { robert: 'robert', ramirez: 'ramirez', rob: 'rob', joseph: 'joseph', miranda: 'miranda',
      alex: 'alex', sean: 'sean', alec: 'alec', lydia_talk: 'lydia',
      // road / travel encounters (WorldNpcs.kt): same four pictures, plus a wide event picture
      //   events     shown when the encounter starts  art/events/<stem>.webp  (512px wide)
      enc_guard: 'enc_guard', enc_preacher: 'enc_preacher', enc_egirl: 'enc_egirl',
      enc_trader: 'enc_trader', enc_goblins: 'enc_goblins', enc_fans: 'enc_fans',
      // Babylon street encounters (Street.kt Kind ids, art in joetopia-art-src/street/<kind>.jpg): street_<kind>
      street_punks: 'street_punks', street_drunk: 'street_drunk', street_party_girls: 'street_party_girls',
      street_beggar: 'street_beggar', street_geneticist: 'street_geneticist', street_preacher: 'street_preacher',
      street_drone: 'street_drone', street_pickpocket: 'street_pickpocket', street_megaphone: 'street_megaphone',
      street_tourist: 'street_tourist', street_stranger: 'street_stranger', street_noble: 'street_noble',
      street_creep: 'street_creep',
      // country 'TEMPTRESS!' ban (GameEngine.temptress): the furious church lady
      street_temptress: 'street_temptress',
      // Undercroft encounters (GameEngine.maybeUndercroft) + THE KRAKEN, from joetopia-art-src/undercroft/<pirate|rats|sailor|streetwalker|kraken>.jpg:
      // replace a jpg and rerun tools/make-encounter-art.py (crops in UNDER_CROP) and tools/make-npc-sprites.py to swap.
      street_pirates: 'street_pirates', street_rats: 'street_rats', street_sailor: 'street_sailor',
      street_streetwalker: 'street_streetwalker', street_kraken: 'street_kraken',
      // Scalegate encounters (GameEngine.maybeScalegate), from joetopia-art-src/scalegate/<duelist|angry_local|parade|bald_fight|fireworks>.jpg.
      // TO SWAP: replace a jpg, rerun tools/make-encounter-art.py (crops in SCALE_CROP) and restyle the sprite in tools/make-npc-sprites.py.
      street_duel: 'street_duel', street_angry_local: 'street_angry_local', street_parade: 'street_parade',
      street_fireworks: 'street_fireworks', street_bald_brawl: 'street_bald_brawl',
      // Lantern Row encounters (GameEngine.maybeLantern): real art from joetopia-art-src/lantern/<id>.jpg (tools/make-encounter-art.py; the Tipsy Muse is cropped head-to-waist for PG-13).
      // TO SWAP: drop joetopia-art-src/lantern/<starving_artist|tipsy_muse|acrobats>.jpg, rerun tools/make-encounter-art.py
      // (crops in LANTERN_CROP) and restyle the sprite in tools/make-npc-sprites.py. No change needed here.
      street_starving_artist: 'street_starving_artist', street_tipsy_muse: 'street_tipsy_muse', street_acrobats: 'street_acrobats',
      // Chrome Quarter encounters (GameEngine.maybeChrome): PLACEHOLDER art drawn from the map sprites.
      // TO SWAP: drop joetopia-art-src/chrome/<courier|public_pooper|discarded_tech|toll_path>.jpg, rerun tools/make-encounter-art.py
      // (crops in CHROME_CROP) and restyle the sprite in tools/make-npc-sprites.py. No change needed here.
      street_courier: 'street_courier', street_public_pooper: 'street_public_pooper', street_discarded_tech: 'street_discarded_tech', street_toll_path: 'street_toll_path' },
    // Street kinds without their own picture borrow one: kind id -> character id.
    streetArt: { offduty: 'enc_guard' },
    // Pictures shown on the map message box when the log matches (things that happen outside a scene).
    logArt: [
      { re: /TEMPTRESS!|Temptress[,!.]|show your face here for/, id: 'street_temptress', sprite: true },
      { re: /man in a dark toga watches you|Same dark toga/, id: 'street_creep', small: true },
    ],
    npcs: {}, faces: {}, portraits: {}, busts: {}, events: {},
    enemies: {},             // battle sprite per enemy id, e.g. wolf: 'art/enemies/wolf.png'
    // Fights whose enemy is one of the characters above: enemy id (or street-event name) -> character id.
    // Its bust is the enemy picture. Fights that start from a road encounter use that encounter's bust too.
    enemyArt: { city_guard: 'enc_guard', goblin: 'enc_goblins', 'off-duty city guard': 'enc_guard',
      street_punk: 'street_punks', angry_drunk: 'street_drunk', mad_geneticist: 'street_geneticist',
      rogue_drone: 'street_drone', noble: 'street_noble', creep: 'street_creep',
      undercroft_pirates: 'street_pirates', sewer_rats: 'street_rats', drunken_sailor: 'street_sailor', kraken: 'street_kraken',
      scale_duelist: 'street_duel', bald_brawlers: 'street_bald_brawl', toll_guard: 'street_toll_path' },
    objects: {               // map markers for shops, crowds and things to do
      shop: 'art/sprites/shop.png', crowd: 'art/sprites/crowd.png', fight: 'art/sprites/fight.png',
      event: 'art/sprites/event.png', drink: 'art/sprites/drink.png', dance: 'art/sprites/dance.png',
      rest: 'art/sprites/rest.png', pray: 'art/sprites/pray.png', forage: 'art/sprites/forage.png',
      explore: 'art/sprites/explore.png', books: 'art/sprites/books.png', lab: 'art/sprites/lab.png',
      spot: 'art/sprites/spot.png',
    },
    battleBg: {},            // per biome, e.g. forest: 'art/battle/forest.png'
    title: null,             // title-screen banner, e.g. 'art/title.png'
  };
  const A = window.JOETOPIA_ART;
  // ?v=<build> makes every release fetch fresh pictures instead of a stale cached copy.
  const v = window.JOETOPIA_BUILD ? `?v=${window.JOETOPIA_BUILD}` : '';
  for (const [id, stem] of Object.entries(A.characters)) {
    A.npcs[id] = A.npcs[id] || `art/npcs/${stem}.png${v}`; A.faces[id] = A.faces[id] || `art/faces/${stem}.webp${v}`;
    A.portraits[id] = A.portraits[id] || `art/portraits/${stem}.webp${v}`; A.busts[id] = A.busts[id] || `art/busts/${stem}.webp${v}`;
    if (/^(enc|street)_/.test(id)) A.events[id] = A.events[id] || `art/events/${stem}.webp${v}`;
  }
})();
