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
      alex: 'alex', sean: 'sean', alec: 'alec', lydia_talk: 'lydia' },
    npcs: {}, faces: {}, portraits: {}, busts: {},
    enemies: {},             // battle sprite per enemy id, e.g. wolf: 'art/enemies/wolf.png'
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
  }
})();
