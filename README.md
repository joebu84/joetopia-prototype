# Joetopia: web edition

The full Joetopia RPG as a top-down walk-around game, played in the browser. It has drop-down menus and turn-based combat. There's no backend, login or build step; the game is static files.

**Play:** https://joebu84.github.io/joetopia-prototype/
**Locally:** run `python3 -m http.server` in this folder, then open http://localhost:8000.

## Controls
| | Desktop | Phone |
|---|---|---|
| Walk | Arrows / WASD, or click a tile (click-to-walk) | D-pad, or tap a tile |
| Talk / use / advance | Enter, Space, E or Z | **A** button, or tap the person |
| Back / close | Esc or X | **B** button, or the ✕ in a menu |
| Menus | I gear, C stats, J quests, M mushrooms, V stream, H "here" | Menu bar at the top |
| Battle | Click a command, or press 1–5; arrow keys move focus | Tap a command |

Walk into an arrow at the edge of the screen, or into a door, to change places. **Here ▾** lists everything at your location. **Save ▾** has Save / Load / Delete. The game autosaves to `localStorage` whenever you are exploring, the same as the APK, and remembers your exact tile on every step. **Settings ▾** has text size, map labels (all, or only nearby) and walk speed.

## How it works
The game logic is **the real Kotlin engine from the Android APK**, compiled to JavaScript (`engine/joetopia-engine.js`), so every NPC, stat check, quest, enemy, status effect, event and ending matches the APK. The web layer only draws it:

| File | What it does |
|---|---|
| `index.html`, `css/style.css` | Page, menu bar, panels, battle screen, phone controls |
| `js/map.js` | Turns each engine location into a 20×15 tile room: exits become doors/edge arrows, NPCs/shops/activities become people and markers |
| `js/ui.js` | Pop-up menus (talk options grouped into drop-downs), HUD, battle screen, messages |
| `js/game.js` | Movement, input, menus, save/load, glue to the engine |
| `js/art.js` | Loads art from the manifest; draws placeholders for anything missing |
| `data/art.js` | **Art manifest**: every image path |
| `data/maps.js` | Optional hand-drawn room layouts (any room without one gets a generated layout) |
| `data/ui.js` | How engine options are sorted into talk groups, battle commands and map icons |
| `data/world.js` | Generated: location → name, region, city/country/wilds tier, biome, parent |
| `engine-src/` | Build scaffolding to recompile the engine from the APK sources |
| `tools/` | `gen-world.js` (regenerates `data/world.js`), `export-placeholders.js` (writes placeholder PNGs) |

## Adding / swapping art
Every picture is listed in **`data/art.js`**. To replace one, save a PNG and point its entry at that file (or just overwrite the existing file at the same path). If an entry is `null` or the file is missing, a placeholder is drawn, so nothing breaks. Pixel art is drawn unsmoothed.

- **Tiles**, 32×32: `tiles.<biome>.{floor,wall,decor,door}`. The biomes are city, club, village, farm, forest, cave, cavern_club, wilds, castle, interior and interior_city.
- **Player**, 32×32 (or 32×48): `player`, or `playerByClass.BOUNCER` etc.
- **NPCs on the map**: `npcs.<npc id>`, e.g. `robert: 'art/npcs/robert.png'`.
- **Talk portraits** (any square size): `portraits.<npc id>`.
- **Battle enemies** (~128×128): `enemies.<enemy id>`. Enemy ids include wolf, goblin, bandit, spider, cultist, thug, guard, skeleton, wraith, alpha, matriarch, morvane, rave_bouncer, city_guard, noble, creep, and more.
- **Battle backgrounds**, 640×220: `battleBg.<biome>`.
- **Map markers** (shops, crowds, things to do): `objects.*`.
- **Title banner**: `title`.

To regenerate the placeholder PNGs, run `node tools/export-placeholders.js` (needs Playwright). Add `--force` to overwrite existing files.

## Custom room layouts
Add an entry to `data/maps.js` keyed by the location id (see `data/world.js` for the ids). It's 20 strings of 20 characters (15 rows): `#` wall, `.`/`,` floor, `D` decor, `~` water. Optional `exits` and `slots` lists set where doors and people go. `village` is a worked example. To change a room's look without drawing a layout, change its `biome` in `data/world.js`.

## Adding or changing content (NPCs, quests, enemies, dialogue)
Content lives in the Kotlin engine in the Android project (`app/src/main/java/com/grokbot/joetopia/game/`). Edit it there, then rebuild the web engine:
1. Copy `engine-src/` somewhere as a Kotlin Multiplatform JS project. Set `SRC` in `sync.sh` to your Android `game/` folder.
2. Run `./sync.sh && gradle jsBrowserProductionWebpack`. This needs JDK 17 and Gradle 8.x. `sync.sh` copies the engine sources and the small web API (`api/Api.kt`, `api/Shim.kt`).
3. Copy the built `joetopia-engine.js` (from `build/kotlin-webpack/js/productionExecutable/`) to `engine/`.
4. Run `node tools/gen-world.js` so new locations get names, biomes and doors.

New NPCs and options appear automatically in the talk menus. If one lands in "✨ Other", add a regex to `data/ui.js`.

## Differences from the APK
- Room layouts are generated from each location's exits and contents. Only the village square is hand-drawn so far.
- Most art is placeholder: generic people sprites, coloured-shape enemies and simple tiles. Portraits exist for Robert, Ramirez, Rob and Joseph only.
- Web saves are separate from APK saves; they can't be transferred.
- There's no gamepad support or sound (the APK has no sound either).
