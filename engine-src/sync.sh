#!/bin/bash
# Copies the Android game engine (source of truth) into this Kotlin/JS build, untouched except for
# widening a few private fields the web facade reads. The APK project itself is never modified.
set -e
SRC=/workspace/android-text-rpg/app/src/main/java/com/grokbot/joetopia/game
DST=$(dirname "$0")/src/jsMain/kotlin/com/grokbot/joetopia/game
for f in $SRC/*.kt; do cp "$f" "$DST/"; done
sed -i -E 's/private (var talkNpc|var talkReturn|val log =|var shopId|var resultTitle|var mingleNode|var locals|var gameOverText|var endingText|var menuReturn|fun placeName|var lastStreet|var moveCount|fun npcById)/internal \1/' "$DST/GameEngine.kt"
cp $(dirname "$0")/api/*.kt "$DST/"
