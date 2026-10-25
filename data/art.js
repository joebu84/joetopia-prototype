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
      // district hosts with real art (joetopia-art-src/npc/<file>.jpg, crops in tools/make-encounter-art.py NPC_ART)
      lantern_poet: 'lantern_poet',  // Miriam Inkwell, Lantern Row
      // 2.7.4 / World 1.5 portraits (art-src npc/, enemy/, boss/; see tools/make-encounter-art.py NPC_ART)
      dealer_tamar: 'dealer_tamar', shamgar: 'shamgar', priscilla_talk: 'priscilla_talk', barnabas_talk: 'barnabas_talk', under_boss: 'under_boss', scale_veteran: 'scale_veteran', thornback_alpha: 'thornback_alpha',
      // PLACEHOLDER art (v1.6): generated stand-ins, joetopia-art-src/placeholder/ + PLACEHOLDER_ART in tools/make-encounter-art.py.
      // Listed in placeholders below; swap a picture by replacing its source and rerunning the tools (same id). local = any generic loc_* local.
      spire_patron: 'spire_patron', chrome_broker: 'chrome_broker', zipporah: 'zipporah', ninsun: 'ninsun', methuselah: 'methuselah', jezebel: 'jezebel', ezra: 'ezra', grey_acolyte: 'grey_acolyte', hagar: 'hagar', asher: 'asher', dj_meph: 'dj_meph', dj_meph_back: 'dj_meph_back', keziah: 'keziah', boaz: 'boaz', lilith_spin: 'lilith_spin', delilah: 'delilah', jonah: 'jonah', salome: 'salome', gideon: 'gideon', naamah: 'naamah', jojo_neon: 'jojo_neon', princess_zillah: 'princess_zillah', doctor_conspiracy: 'doctor_conspiracy', azazel: 'azazel', vashti: 'vashti', local: 'local', enemy_wolf: 'enemy_wolf', enemy_bandit: 'enemy_bandit', enemy_spider: 'enemy_spider', enemy_guard: 'enemy_guard', enemy_skeleton: 'enemy_skeleton', enemy_wraith: 'enemy_wraith', enemy_matriarch: 'enemy_matriarch', enemy_morvane: 'enemy_morvane',
      // v1.7 / 2.7.6: Royal Crypt + Eden PLACEHOLDERS (tools/make-crypt-eden-art.py) and the flower girl / Ash Wolf REAL art (uncropped)
      enemy_evil_spirit: 'enemy_evil_spirit', enemy_zombie_goblin: 'enemy_zombie_goblin', enemy_graverobbers: 'enemy_graverobbers',
      enemy_possessed_man: 'enemy_possessed_man', enemy_necromancer: 'enemy_necromancer', enemy_vampire: 'enemy_vampire',
      royal_crypt: 'royal_crypt', thaddeus_tomb: 'thaddeus_tomb', crypt_grave: 'crypt_grave',
      enemy_flaming_sword: 'enemy_flaming_sword', enemy_serpent: 'enemy_serpent', eden_garden: 'eden_garden', tree_knowledge: 'tree_knowledge',
      tree_life: 'tree_life', ending_thaddeus: 'ending_thaddeus', draconian_true: 'draconian_true', ushapti_true: 'ushapti_true',
      street_flower_girl: 'street_flower_girl', street_flower_girl_blue: 'street_flower_girl_blue',
      enemy_ash_wolf_red_hood: 'enemy_ash_wolf_red_hood', enemy_ash_wolf_blue_hood: 'enemy_ash_wolf_blue_hood',
      // v1.8 / 2.7.7: Babylon district backdrop PLACEHOLDERS (scene banners, tools/make-crypt-eden-art.py)
      district_spire: 'district_spire', district_chrome: 'district_chrome', district_lantern: 'district_lantern', district_scale: 'district_scale', district_under: 'district_under', district_core: 'district_core', district_neon_abyss: 'district_neon_abyss', district_docks: 'district_docks',
      dr_spore: 'dr_spore',  // Dr. Nyxariel Spore's lab (a scene, placed by JOETOPIA_UI.npcSpots)
      ushapti_smuggler: 'ushapti_smuggler', draconian_bodyguard: 'draconian_bodyguard', ash_cultist: 'ash_cultist',
      enlil_ka: 'enlil_ka', marduk_ra: 'marduk_ra', inanna_shar: 'inanna_shar', ushapti_broker: 'ushapti_broker',
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
      // Chrome Quarter encounters (GameEngine.maybeChrome): all four use REAL art (courier.jpg, rude_worker.jpg,
      // broken_tech.jpg -> discarded tech, toll.jpg -> toll path). TO SWAP: replace joetopia-art-src/chrome/<file>.jpg, rerun tools/make-encounter-art.py
      // (crops in CHROME_CROP) and restyle the sprite in tools/make-npc-sprites.py. No change needed here.
      street_courier: 'street_courier', street_rude_worker: 'street_rude_worker', street_discarded_tech: 'street_discarded_tech', street_toll_path: 'street_toll_path',
      // Gilded Spire encounters (GameEngine.maybeSpire; the Reality Show also rolls in the megarave's Creator Corner): all four use REAL art
      // (chariot.jpg, reality_show.jpg = the fictional celebrity Valeria Kurigalzu, cropped head-to-hips for PG-13, jewelry.jpg, charity.jpg).
      // TO SWAP: replace joetopia-art-src/spire/<file>.jpg, rerun tools/make-encounter-art.py (crops in SPIRE_CROP) and restyle the sprite
      // in tools/make-npc-sprites.py. No change needed here.
      street_runaway_chariot: 'street_runaway_chariot', street_reality_show: 'street_reality_show', street_lost_jewelry: 'street_lost_jewelry',
      street_charity_gala: 'street_charity_gala',
      // Reality-show episodes (Street.EPISODES; status.streetArt names the one on air): togiru.jpg, blind_date_noble.jpg (PG-13 face +
      // camera composite), bathsheba.jpg (PG-13 face/shoulders), fletcher.jpg, petyr.jpg. Crops in SPIRE_CROP.
      street_reality_pushup: 'street_reality_pushup', street_reality_blind_date: 'street_reality_blind_date', street_reality_makeup: 'street_reality_makeup',
      street_reality_fletcher: 'street_reality_fletcher', street_reality_petyr: 'street_reality_petyr',
      // Wizard Couriers (Gilded Spire table): REAL art spire/wizard_courier.jpg (red-robed wizard offering an amber vial to a man in a toga).
      // The Amber Wizard fight reuses it (enemyArt.wizard). street_adrenochrome = the vial cropped from the same picture (item picture).
      // TO SWAP: replace joetopia-art-src/spire/wizard_courier.jpg (or add a separate vial jpg via SPIRE_FILE) and rerun tools/make-encounter-art.py.
      street_wizard_couriers: 'street_wizard_couriers', street_adrenochrome: 'street_adrenochrome',
      // Toadstool Forest (Forest.kt, ~20% per move in the forest): REAL art joetopia-art-src/forest/{troll,weirdo,trustworthy_human,unicorn,pixie}.jpg
      // (pixie = PG-13 crop: head, shoulders, upper wings only). The gnome is a PLACEHOLDER card. Item pictures: horn + wings cropped from the
      // jpgs, the rest are sprite cards. TO SWAP: drop joetopia-art-src/forest/<id>.jpg, tune FOREST_CROP, rerun tools/make-encounter-art.py.
      street_troll: 'street_troll', street_weirdo: 'street_weirdo', street_trustworthy_human: 'street_trustworthy_human', street_unicorn: 'street_unicorn', street_pixie: 'street_pixie', street_gnome: 'street_gnome', street_unicorn_horn: 'street_unicorn_horn', street_pixie_wings: 'street_pixie_wings', street_gnome_hat: 'street_gnome_hat', street_work_jeans: 'street_work_jeans', street_flannel_shirt: 'street_flannel_shirt', street_woodsman_axe: 'street_woodsman_axe', street_unicorn_wand: 'street_unicorn_wand', street_unicorn_sword: 'street_unicorn_sword', street_unicorn_heels: 'street_unicorn_heels',
      // Goblin Bangers: goblin_banger.jpg = RED crew (blue skin, red bandana, SMG); goblin_banger_blue.jpg = BLUE crew (red skin, blue bandana, revolver). Items = sprite cards.
      street_goblin_banger: 'street_goblin_banger', street_goblin_banger_blue: 'street_goblin_banger_blue', street_goblin_zapper: 'street_goblin_zapper', street_banger_bandana: 'street_banger_bandana', street_red_shiv: 'street_red_shiv', street_bike_chain: 'street_bike_chain', street_stem_bat: 'street_stem_bat', street_goblin_revolver: 'street_goblin_revolver', street_blue_bandana: 'street_blue_bandana', street_blue_shiv: 'street_blue_shiv', street_goblin_slingshot: 'street_goblin_slingshot', street_big_booma: 'street_big_booma', street_ballistic_hat: 'street_ballistic_hat',
      // goblin_unaffiliated.jpg = the three-goblin crew; bigfoot.jpg = mother Bigfoot + baby among giant mushrooms
      street_goblin_unaffiliated: 'street_goblin_unaffiliated', street_bigfoot: 'street_bigfoot',
      // Dance-floor table (Dance.kt, ~9% per move onto a dance floor): REAL art joetopia-art-src/dance/{water,dj,pickpocket,boyfriend,complimentary_drinks}.jpg
      // (PG-13 crops: pickpocket = face + shoulders, the girlfriend on the boyfriend card shaded below the face, server = head, shoulders and tray).
      // TO SWAP: replace the jpg and rerun tools/make-encounter-art.py (tune DANCE_CROP).
      street_dance_water: 'street_dance_water', street_dance_dj: 'street_dance_dj', street_dance_pickpocket: 'street_dance_pickpocket', street_dance_boyfriend: 'street_dance_boyfriend', street_dance_drinks: 'street_dance_drinks',
      // "A stranger asks you to dance" (most common dance-floor/bar encounter): joetopia-art-src/dance/stranger_1..5.jpg (stranger_3 = PG-13 face + shoulders crop).
      street_dance_stranger_1: 'street_dance_stranger_1', street_dance_stranger_2: 'street_dance_stranger_2', street_dance_stranger_3: 'street_dance_stranger_3', street_dance_stranger_4: 'street_dance_stranger_4', street_dance_stranger_5: 'street_dance_stranger_5',
      street_bar_drinker_1: 'street_bar_drinker_1', street_bar_drinker_2: 'street_bar_drinker_2', street_bar_drinker_3: 'street_bar_drinker_3', street_bar_drinker_4: 'street_bar_drinker_4', street_bar_drinker_5: 'street_bar_drinker_5', street_bar_drinker_6: 'street_bar_drinker_6' },
    // Street kinds without their own picture borrow one: kind id -> character id.
    streetArt: { offduty: 'enc_guard', red_goblin_spot: 'street_goblin_banger', blue_goblin_spot: 'street_goblin_banger_blue',
      crypt_spirit: 'enemy_evil_spirit', crypt_zombie_goblin: 'enemy_zombie_goblin', crypt_graverobbers: 'enemy_graverobbers', crypt_possessed: 'enemy_possessed_man',
      crypt_grave: 'crypt_grave', crypt_necromancer: 'enemy_necromancer', crypt_vampire: 'enemy_vampire',
      // the four flower girls: red / blue hood; the wolf hides behind the girl's picture until she shows her teeth
      flower_girl_wolf: 'street_flower_girl', flower_girl_wolf_blue: 'street_flower_girl_blue' },
    // Pictures shown on the map message box when the log matches (things that happen outside a scene).
    logArt: [
      { re: /the Ash Wolf in her little red hood\. She sniffs|Under the little red hood, something grins|sniffs your red colours and laughs|under the red hood studies you|leaving her little red hood behind/, id: 'enemy_ash_wolf_red_hood' },
      { re: /the Ash Wolf in her little blue hood\. She sniffs|Under the little blue hood, something grins|sniffs your blue colours and laughs|under the blue hood studies you|leaving her little blue hood behind/, id: 'enemy_ash_wolf_blue_hood' },
      { re: /TEMPTRESS!|Temptress[,!.]|show your face here for/, id: 'street_temptress', sprite: true },
      { re: /man in a dark toga watches you|Same dark toga/, id: 'street_creep', small: true },
      { re: /Adrenochrome Vial|ADRENOCHROME/, id: 'street_adrenochrome', small: true },
      { re: /Unicorn Horn/, id: 'street_unicorn_horn', small: true },
      { re: /Pixie Wings/, id: 'street_pixie_wings', small: true },
      { re: /Gnome Hat/, id: 'street_gnome_hat', small: true },
      { re: /Worker's Jeans/, id: 'street_work_jeans', small: true },
      { re: /Flannel Shirt/, id: 'street_flannel_shirt', small: true },
      { re: /Woodsman's Axe/, id: 'street_woodsman_axe', small: true },
      { re: /Unicorn Wand/, id: 'street_unicorn_wand', small: true },
      { re: /Unicorn Sword/, id: 'street_unicorn_sword', small: true },
      { re: /Unicorn Heels/, id: 'street_unicorn_heels', small: true },
      { re: /Goblin Zapper SMG/, id: 'street_goblin_zapper', small: true },
      { re: /Banger Bandana/, id: 'street_banger_bandana', small: true },
      { re: /Red-Taped Shiv/, id: 'street_red_shiv', small: true },
      { re: /Goblin Bike Chain/, id: 'street_bike_chain', small: true },
      { re: /Mushroom-Stem Bat/, id: 'street_stem_bat', small: true },
      { re: /Goblin Six-Shooter/, id: 'street_goblin_revolver', small: true },
      { re: /Da Big Booma/, id: 'street_big_booma', small: true },
      { re: /Ballistic Hat/, id: 'street_ballistic_hat', small: true },
      { re: /Blue Bandana/, id: 'street_blue_bandana', small: true },
      { re: /Blue-Taped Shiv/, id: 'street_blue_shiv', small: true },
      { re: /Goblin Slingshot/, id: 'street_goblin_slingshot', small: true },
    ],
    placeholderArt: ['spire_patron', 'chrome_broker', 'zipporah', 'ninsun', 'methuselah', 'jezebel', 'ezra', 'grey_acolyte', 'hagar', 'asher', 'dj_meph', 'dj_meph_back', 'keziah', 'boaz', 'lilith_spin', 'delilah', 'jonah', 'salome', 'gideon', 'naamah', 'jojo_neon', 'princess_zillah', 'doctor_conspiracy', 'azazel', 'vashti', 'local', 'enemy_wolf', 'enemy_bandit', 'enemy_spider', 'enemy_guard', 'enemy_skeleton', 'enemy_wraith', 'enemy_matriarch', 'enemy_morvane', 'street_gnome', 'enemy_evil_spirit', 'enemy_zombie_goblin', 'enemy_graverobbers', 'enemy_possessed_man', 'enemy_necromancer', 'enemy_vampire', 'royal_crypt', 'thaddeus_tomb', 'crypt_grave', 'enemy_flaming_sword', 'enemy_serpent', 'eden_garden', 'tree_knowledge', 'tree_life', 'ending_thaddeus', 'draconian_true', 'ushapti_true', 'district_spire', 'district_chrome', 'district_lantern', 'district_scale', 'district_under', 'district_core', 'district_neon_abyss', 'district_docks'],  // placeholder: true (generated art, swap any time)
    npcs: {}, faces: {}, portraits: {}, busts: {}, events: {},
    enemies: {},             // battle sprite per enemy id, e.g. wolf: 'art/enemies/wolf.png'
    // Fights whose enemy is one of the characters above: enemy id (or street-event name) -> character id.
    // Its bust is the enemy picture. Fights that start from a road encounter use that encounter's bust too.
    enemyArt: { city_guard: 'enc_guard', goblin: 'enc_goblins', 'off-duty city guard': 'enc_guard',
      street_punk: 'street_punks', angry_drunk: 'street_drunk', mad_geneticist: 'street_geneticist',
      rogue_drone: 'street_drone', noble: 'street_noble', creep: 'street_creep',
      undercroft_pirates: 'street_pirates', sewer_rats: 'street_rats', drunken_sailor: 'street_sailor', kraken: 'street_kraken',
      scale_duelist: 'street_duel', bald_brawlers: 'street_bald_brawl', toll_guard: 'street_toll_path', spire_guards: 'street_runaway_chariot', wizard: 'street_wizard_couriers',
      troll: 'street_troll', weirdo: 'street_weirdo', unicorn: 'street_unicorn', pixie: 'street_pixie', gnome: 'street_gnome',
      goblin_banger: 'street_goblin_banger', goblin_banger_blue: 'street_goblin_banger_blue',
      goblin_unaffiliated: 'street_goblin_unaffiliated', mother_bigfoot: 'street_bigfoot',
      dance_pickpocket: 'street_dance_pickpocket', dance_boyfriend: 'street_dance_boyfriend',
      rave_bouncer: 'shamgar', thug: 'ushapti_smuggler', draconian: 'draconian_bodyguard', cultist: 'ash_cultist',
      enlil: 'enlil_ka', marduk: 'marduk_ra', inanna: 'inanna_shar', ushapti: 'ushapti_broker', alpha: 'thornback_alpha',
      wolf: 'enemy_wolf', bandit: 'enemy_bandit', spider: 'enemy_spider', guard: 'enemy_guard', skeleton: 'enemy_skeleton', wraith: 'enemy_wraith', matriarch: 'enemy_matriarch', morvane: 'enemy_morvane',
      evil_spirit: 'enemy_evil_spirit', zombie_goblin: 'enemy_zombie_goblin', graverobbers: 'enemy_graverobbers', possessed_man: 'enemy_possessed_man', necromancer: 'enemy_necromancer', vampire: 'enemy_vampire',
      flaming_sword: 'enemy_flaming_sword', serpent: 'enemy_serpent', red_hood_wolf: 'enemy_ash_wolf_red_hood', blue_hood_wolf: 'enemy_ash_wolf_blue_hood' },  // the guards fight shows the chariot driver
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
    if (/^(enc|street)_/.test(id) || /^(royal_crypt|thaddeus_tomb|crypt_grave|eden_garden|tree_knowledge|tree_life|ending_thaddeus)$/.test(id) || /^district_/.test(id)) A.events[id] = A.events[id] || `art/events/${stem}.webp${v}`;
  }
})();
