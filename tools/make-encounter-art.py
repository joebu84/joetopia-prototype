#!/usr/bin/env python3
"""Web copies of the six road-encounter pictures (source: joetopia-art-src/encounters/enc_*.jpg).
  portraits/<id>.webp  whole picture, 512px long side (tap-to-enlarge)
  faces/<id>.webp      160px square crop on the head(s)   (talk-menu thumbnail)
  busts/<id>.webp      256px square crop                  (battle picture)
  events/<id>.webp     512px-wide landscape banner        (shown when the encounter starts)
Crop boxes are fractions of the source (x0, y0, x1, y1). The wide goblin/fan shots keep the
whole scene for portrait/event and centre the square crops on the middle of the group."""
from PIL import Image
import os, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else '/workspace/joetopia-art-src/encounters'
ART = os.path.join(os.path.dirname(__file__), '..', 'art')
CROPS = {  # face, bust, event
    'enc_guard':    ((180/538, 70/800, 350/538, 240/800), (70/538, 50/800, 470/538, 450/800), (0, 50/800, 1, 352/800)),
    'enc_preacher': ((165/538, 115/800, 365/538, 315/800), (30/538, 120/800, 510/538, 600/800), (0, 140/800, 1, 442/800)),
    'enc_egirl':    ((180/537, 115/800, 390/537, 325/800), (25/537, 100/800, 505/537, 580/800), (0, 105/800, 1, 407/800)),
    'enc_trader':   ((70/537, 70/800, 230/537, 230/800), (0, 75/800, 1, 75/800 + 537/800), (0, 90/800, 1, 392/800)),
    'enc_goblins':  ((295/800, 140/537, 525/800, 370/537), (131/800, 0, 668/800, 1), (0, 0, 1, 1)),
    'enc_fans':     ((420/800, 190/537, 600/800, 370/537), (131/800, 0, 668/800, 1), (0, 0, 1, 1)),
}
def box(im, f):
    w, h = im.size; return im.crop((round(f[0]*w), round(f[1]*h), round(f[2]*w), round(f[3]*h)))
def save(im, sub, name, q=82):
    d = os.path.join(ART, sub); os.makedirs(d, exist_ok=True); im.save(os.path.join(d, name + '.webp'), 'WEBP', quality=q, method=6)
for name, (face, bust, ev) in CROPS.items():
    im = Image.open(os.path.join(SRC, name + '.jpg')).convert('RGB')
    p = im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
    save(box(im, face).resize((160, 160), Image.LANCZOS), 'faces', name)
    save(box(im, bust).resize((256, 256), Image.LANCZOS), 'busts', name)
    e = box(im, ev); e = e.resize((512, round(512 * e.size[1] / e.size[0])), Image.LANCZOS); save(e, 'events', name, 80)
    print(name, p.size, e.size)
