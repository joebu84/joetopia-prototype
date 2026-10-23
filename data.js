/* =====================================================================
   JOETOPIA WEB PROTOTYPE: ALL CONTENT LIVES IN THIS FILE.
   Edit freely: map, tiles, NPCs, events. No code changes needed.

   ART: every "image"/"sprite"/"portrait" field is a path relative to
   index.html. If the file exists it is used; if it is missing, the game
   draws a coloured placeholder instead. Drop your own PNGs over the
   placeholder files in art/ and reload. (Sizes: see README.md.)
   ===================================================================== */

window.JOETOPIA = {

  title: "Joetopia: Babylon Town Square",
  tileSize: 16,            // pixels per tile (art is drawn at this size)

  /* ---------------- MAP ----------------
     One character per tile. Every row must be the same length.
     The legend below says what each character is.                     */
  map: [
    "####################",
    "#BBBBB.t....t.BBBBB#",
    "#BBBBB........BBBBB#",
    "#BBDBB........BBDBB#",
    "#..=............=..#",
    "#..==============..#",
    "#..=....gggg....=..#",
    "#t.=...g.FF.g...=.t#",
    "#..=...g.FF.g...=..#",
    "#..=....gggg....=..#",
    "#..==============..#",
    "#........==........#",
    "#t.BBB...==...BBB.t#",
    "#..BDB...==...BDB..#",
    "##########GG########",
  ],

  /* ---------------- TILE LEGEND ----------------
     solid: true  = you can't walk through it.
     color: placeholder colour.  image: optional 16x16 PNG.            */
  tiles: {
    "#": { name: "wall",     solid: true,  color: "#5b4b6b", image: "art/tiles/wall.png" },
    "B": { name: "building", solid: true,  color: "#a8577e", image: "art/tiles/building.png" },
    "D": { name: "door",     solid: true,  color: "#3b2a1a", image: "art/tiles/door.png" },
    ".": { name: "cobble",   solid: false, color: "#c9b48a", image: "art/tiles/cobble.png" },
    "=": { name: "path",     solid: false, color: "#e3cf9f", image: "art/tiles/path.png" },
    "g": { name: "grass",    solid: false, color: "#5f9e4f", image: "art/tiles/grass.png" },
    "t": { name: "tree",     solid: true,  color: "#2f6b34", image: "art/tiles/tree.png" },
    "F": { name: "fountain", solid: true,  color: "#3f8fd8", image: "art/tiles/fountain.png" },
    "G": { name: "gate",     solid: true,  color: "#8a8a8a", image: "art/tiles/gate.png" },
  },

  /* ---------------- PLAYER ---------------- */
  player: {
    name: "You",
    x: 10, y: 11,           // starting tile
    facing: "up",
    sprite: "art/sprites/player.png",
    // placeholder colours (used when the sprite file is missing)
    colors: { body: "#f2f2f2", hair: "#6b3e1f", skin: "#e8b48a", trim: "#d4a017" },
  },

  /* ---------------- NPCs ----------------
     id, name, title, x/y tile, facing, sprite, portrait,
     lines: shown in order, one per tap/key.
     randomLines (optional): one of these is added at the end each talk,
       never the same twice in a row (used for Robert's dad jokes).
     colors: placeholder colours.                                       */
  npcs: [
    {
      id: "ramirez", name: "Ramirez", title: "Captain of the Brute Squad",
      x: 16, y: 4, facing: "down",
      sprite: "art/sprites/ramirez.png", portrait: "art/portraits/ramirez.png",
      colors: { body: "#3d5a80", hair: "#111111", skin: "#b9805a", trim: "#9aa5b1", longHair: true, big: true },
      lines: [
        "Big, really big, long black hair down past his shoulder blades. A sledgehammer leans against the Undercroft door beside him.",
        "\"ID. Now.\"",
        "\"You start trouble in my club, you leave through the wall.\"",
        "\"The hammer? Forged it myself. Days I hammer steel, nights I hammer drunks. Steel complains less.\"",
        "He stares at you. Sighs like you asked for a kidney. Then he wraps you in a crushing bear hug. \"Tell no one.\"",
      ],
    },
    {
      id: "robert", name: "Robert", title: "Brute Squad, VIP door of the Gilded Spire",
      x: 3, y: 4, facing: "down",
      sprite: "art/sprites/robert.png", portrait: "art/portraits/robert.png",
      colors: { body: "#1b1b1b", hair: "#3b2a1a", skin: "#d9a074", trim: "#d4a017", tall: true },
      lines: [
        "Robert is super tall, so tall the velvet rope comes up to his knee. He looks down at you from somewhere near the ceiling.",
        "\"Name's not on the list.\"",
        "\"...You want a joke? Fine. One joke.\"",
      ],
      randomLines: [
        "\"I'm reading a book about anti-gravity. Can't put it down.\"",
        "\"Why don't skeletons fight each other? They don't have the guts.\"",
        "\"I used to hate facial hair. Then it grew on me.\"",
        "\"What do you call a fake noodle? An impasta.\"",
        "\"Why did the scarecrow win an award? He was outstanding in his field.\"",
        "\"I only know twenty-five letters of the alphabet. I don't know Y.\"",
        "\"What do you call a bear with no teeth? A gummy bear.\"",
        "\"Why can't you trust stairs? They're always up to something.\"",
        "\"I told my wall a joke once. It cracked up.\"",
        "\"What's a bouncer's favourite drink? Punch.\"",
      ],
    },
    {
      id: "joseph", name: "Joseph", title: "Fire-and-brimstone TikTok Pastor",
      x: 6, y: 8, facing: "right",
      sprite: "art/sprites/joseph.png", portrait: "art/portraits/joseph.png",
      colors: { body: "#7a1f1f", hair: "#111111", skin: "#c98f63", trim: "#f2f2f2", beard: true },
      lines: [
        "A magnificent bushy black beard, burning dark eyes, a battered Bible in one hand and a phone on a selfie-stick in the other.",
        "\"REPENT, SINNER! ...Oh, hello. Have you been saved yet?\"",
        "\"The fire is COMING, and it is NOT a laser show!\"",
        "You confess a small sin. He listens, beard trembling. \"Go and sin no more.\" You feel lighter.",
      ],
    },
    {
      id: "rob", name: "Rob", title: "Chrome Quarter tinkerer (Technomancer)",
      x: 15, y: 11, facing: "left",
      sprite: "art/sprites/rob.png", portrait: "art/portraits/rob.png",
      colors: { body: "#4a4a4a", hair: "#c8a165", skin: "#efc9a6", trim: "#3fd0ff", skinny: true },
      lines: [
        "Skinny and wiry, startlingly bright blue eyes behind cracked AR glasses. Drones the size of beetles orbit his head.",
        "\"Hold this. Don't touch that. Actually don't hold this either.\"",
        "\"Your phone's listening. So's mine. Mine's on our side.\"",
        "\"Firmware is just spells that crash.\"",
      ],
    },
    {
      id: "guard", name: "City Guard", title: "Babylon City Guard",
      x: 9, y: 13, facing: "up",
      sprite: "art/sprites/guard.png", portrait: "art/portraits/guard.png",
      colors: { body: "#2e4a2e", hair: "#555555", skin: "#d8a57c", trim: "#d4a017", helmet: true },
      lines: [
        "\"Evening, citizen. The gate's closed tonight. Lord's orders.\"",
        "\"Ramirez? Down by the Undercroft door.\"",
        "\"On the Brute Squad? Ramirez IS the Brute Squad!\"",
      ],
    },
  ],

  /* ---------------- LOCATION EVENTS ----------------
     Step on tile (x, y) to trigger. Shows an image (or placeholder) plus
     text pages. once: true = only the first time this session.
     tags: violent / wacky / sexy, as in the main game (flavour only here). */
  events: [
    {
      id: "tourist", x: 13, y: 11, once: true, tags: ["wacky"],
      title: "Lost Tourist",
      image: "art/events/tourist.png",
      colors: { sky: "#f6c177", ground: "#c9b48a", figure: "#ffffff" },
      text: [
        "A tourist in a brand-new toga, still with the tag on, turns a map upside down.",
        "\"Excuse me, which way to the Neon Abyss?\"",
        "You point the way. They press a sticker into your hand: I \u2665 BABYLON.",
      ],
    },
    {
      id: "preacher", x: 4, y: 10, once: false, tags: ["wacky"],
      title: "Busking Street Preacher",
      image: "art/events/preacher.png",
      colors: { sky: "#9ccfd8", ground: "#e3cf9f", figure: "#7a1f1f" },
      text: [
        "A street preacher with a hard-light lute sings hymns at full volume, a hat at his feet.",
        "\"Repent, and tip generously!\"",
        "You sing the chorus with a stranger and feel briefly, ridiculously happy.",
      ],
    },
    {
      id: "fountain", x: 10, y: 9, once: false, tags: ["wacky"],
      title: "The Fountain of Babylon",
      image: "art/events/fountain.png",
      colors: { sky: "#31748f", ground: "#5f9e4f", figure: "#3f8fd8" },
      text: [
        "Glow-coins shimmer at the bottom of the old fountain. Somebody has wished for \"more followers\" on a napkin.",
        "You flip a coin in. It sinks, flickers blue, and for a moment the water hums like a bass line.",
      ],
    },
  ],
};
