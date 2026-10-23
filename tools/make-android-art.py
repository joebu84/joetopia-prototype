#!/usr/bin/env python3
"""Art for the ORIGINAL text-adventure APK (com.grokbot.joetopia): the same pictures and the same PG-13 crops as the web
build (this reruns make-encounter-art.py with every output size scaled 512 -> 800), written as WebP into
android-text-rpg/app/src/main/assets/art/{portraits,events}/<id>.webp. Character portraits come straight from
joetopia-art-src/<name>.jpg (whole picture, as on the web). Faces/busts/sprites are web-only and not bundled."""
import os, re, shutil, subprocess, sys, tempfile
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else '/workspace/android-text-rpg/app/src/main/assets/art'
SRC = '/workspace/joetopia-art-src'
LONG = 800
tmp = tempfile.mkdtemp()
code = open(os.path.join(HERE, 'make-encounter-art.py')).read()
code = code.replace("ART = os.path.join(os.path.dirname(__file__), '..', 'art')", "ART = %r" % tmp)
code = re.sub(r'\b512\b', '800', code); code = re.sub(r'\b288\b', '450', code); code = code.replace('card(384,', 'card(600,')
# the placeholder cards draw the web's 32x48 sprites: point them at the web art folder
code = code.replace("os.path.join(ART, 'npcs'", "os.path.join(%r, 'npcs'" % os.path.join(HERE, '..', 'art'))
script = os.path.join(tmp, 'gen.py'); open(script, 'w').write(code)
subprocess.run([sys.executable, script], check=True, cwd=HERE, stdout=subprocess.DEVNULL)
if os.path.exists(OUT): shutil.rmtree(OUT)
for sub in ('portraits', 'events'):
    os.makedirs(os.path.join(OUT, sub))
    for f in os.listdir(os.path.join(tmp, sub)):
        im = Image.open(os.path.join(tmp, sub, f)); im.load()
        im.save(os.path.join(OUT, sub, f), 'WEBP', quality=72, method=6)
CHARS = {'miranda': 'miranda', 'alex': 'alex', 'sean': 'sean', 'alec': 'alec', 'ramirez': 'ramirez', 'joseph': 'joseph',
         'robert': 'robert', 'rob': 'rob', 'lydia': 'elder_lydia'}
for cid, jpg in CHARS.items():
    im = Image.open(os.path.join(SRC, jpg + '.jpg')).convert('RGB'); im.thumbnail((LONG, LONG), Image.LANCZOS)
    im.save(os.path.join(OUT, 'portraits', cid + '.webp'), 'WEBP', quality=72, method=6)
shutil.rmtree(tmp)
n = sum(len(fs) for _, _, fs in os.walk(OUT)); size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs)
print('wrote %d pictures, %.1f MB to %s' % (n, size / 1e6, OUT))
