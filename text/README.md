# Joetopia text RPG (browser)

The same game as **Joetopia.apk** (text 2.7.7, vc25), in the browser. It does not use the top-down World version.

- `joetopia-engine.js` is the Android `game/*.kt` engine compiled with Kotlin/JS, unchanged (see `../engine-src`, `sync.sh`). The page calls it through the small `JoetopiaText` facade (`engine-src/api/TextApi.kt`). Story, encounters, odds, classes and choices all come from the APK code.
- `art/` holds the same portrait and event pictures the APK bundles. They are chosen by the APK's own `Pictures.idFor`.
- `app.js` and `style.css` copy MainActivity: the status bar, LIVE and Gear/Stats/Myco/Save/Menu buttons, the picture panel (tap for fullscreen), the auto-scrolling story and the choice list.
- The game saves to `localStorage["joetopia-text-save"]`, separate from the World save. Like the APK going to the background, it autosaves when you hide or leave the tab (if saving is allowed there).

To rebuild: run `engine-src/sync.sh && gradle jsBrowserProductionWebpack`, then copy `joetopia-engine.js` here.
