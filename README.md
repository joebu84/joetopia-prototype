# Joetopia: web prototype

A small Zelda-style top-down walkabout set in Babylon's town square. Walk around, talk to Ramirez, Robert, Joseph, Rob and a City Guard, and step on tiles to trigger street events. It's plain HTML, canvas and vanilla JS: no build step, no backend, no login.

**Play locally:** run `python3 -m http.server` in this folder, then open http://localhost:8000. (Opening `index.html` straight from disk also works, but some browsers block local images that way.)

**Controls:** Arrows or WASD to walk. Space, Enter or Z to talk and advance. On a phone, use the D-pad or swipe to walk, and the A button (or a tap on the map) to talk.

## Files
| File | What it is |
|---|---|
| `index.html` | The engine. You normally don't need to edit it. |
| `data.js` | **All content:** map, tile legend, player, NPCs, events. |
| `art/tiles/*.png` | 16x16 tiles, one per legend entry. |
| `art/sprites/*.png` | Character sheets for the player and NPCs. |
| `art/portraits/*.png` | Dialogue portraits, 48x48 (any square size works). |
| `art/events/*.png` | Event pictures, 96x72 (any 4:3 size works). |

## Swapping art
The PNGs that ship in `art/` are generated placeholders. Save your own pixel art **at the same path** and reload; you don't need to change any code. If a file is missing, the game draws a coloured placeholder from the `colors` field in `data.js`, so nothing breaks.

- **Tiles:** 16x16 PNG (`tileSize` in `data.js`).
- **Character sprite sheet:** 32x64, which is 2 walk frames across by 4 rows down. Row order: **down, left, right, up**. A single 16x16 image also works; it just won't animate.
- To point a character at a different file, change its `sprite` or `portrait` path in `data.js`.

## Changing the map
In `data.js`, `map` is a list of strings with one character per tile, and every row must be the same length. Each character is defined in `tiles`:
```js
"F": { name: "fountain", solid: true, color: "#3f8fd8", image: "art/tiles/fountain.png" },
```
To add a new tile type, add a new character to `tiles` and use it in `map`. `solid: true` blocks walking.

## Adding an NPC
Add an object to `npcs` in `data.js`:
```js
{ id: "miranda", name: "Miranda", title: "Dancer", x: 12, y: 6, facing: "down",
  sprite: "art/sprites/miranda.png", portrait: "art/portraits/miranda.png",
  colors: { body: "#c0397b", hair: "#e8c56a", skin: "#e8b48a", trim: "#ffffff" },
  lines: ["First line.", "Second line."],
  randomLines: ["optional: one of these is added at the end of each talk"] }
```
Put the NPC on a walkable tile. Optional placeholder looks in `colors` are `longHair`, `beard`, `big`, `tall`, `skinny` and `helmet`.

## Adding an event
Add an object to `events`:
```js
{ id: "shrine", x: 2, y: 7, once: false, tags: ["wacky"], title: "Roadside Shrine",
  image: "art/events/shrine.png", text: ["Page one.", "Page two."] }
```
The event fires when the player steps onto tile `(x, y)`. With `once: true` it fires only once per visit to the page. `tags` (violent, wacky or sexy, as in the Android game) appear under the title.

Coordinates are zero-based: `x` counts columns from the left and `y` counts rows from the top.
