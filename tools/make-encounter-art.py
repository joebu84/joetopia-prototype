#!/usr/bin/env python3
"""Web copies of the road-encounter pictures (joetopia-art-src/encounters/enc_*.jpg) and the
Babylon street-encounter pictures (joetopia-art-src/street/<Street.Kind id>.jpg -> street_<id>).
  portraits/<id>.webp  whole picture, 512px long side (tap-to-enlarge)
  faces/<id>.webp      160px square crop on the head(s)   (talk-menu thumbnail)
  busts/<id>.webp      256px square crop                  (battle picture)
  events/<id>.webp     512px-wide landscape banner        (shown when the encounter starts)
Crop boxes are fractions of the source (x0, y0, x1, y1). The wide goblin/fan shots keep the
whole scene for portrait/event and centre the square crops on the middle of the group."""
from PIL import Image
import os, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else '/workspace/joetopia-art-src/encounters'
STREET_SRC = sys.argv[2] if len(sys.argv) > 2 else '/workspace/joetopia-art-src/street'
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

# Street encounters (all 784x1168 portrait). Per id: face centre (cx, cy) and face width s; bust centre-x,
# width and top; event-banner top (full width, 16:9). Fractions of the source. Kept PG-13: the party girls'
# and the stranger's face/bust/banner crops stop at the shoulders.
STREET = {  # id: (cx, cy, s,   bust_cx, bust_s, bust_top,   ev_top)
    'punks':       (.48, .33, .62,  .50, 1.0, .10,  .12),
    'drunk':       (.52, .30, .35,  .50, .90, .15,  .14),
    'party_girls': (.50, .26, .42,  .50, .50, .05,  .02),
    'beggar':      (.30, .39, .30,  .45, .85, .22,  .25),
    'geneticist':  (.46, .34, .38,  .50, .90, .17,  .16),
    'preacher':    (.43, .30, .33,  .45, .90, .15,  .15),
    'drone':       (.50, .27, .50,  .50, .90, .05,  .08),
    'pickpocket':  (.30, .39, .35,  .45, .90, .22,  .24),
    'megaphone':   (.39, .38, .35,  .45, .90, .22,  .22),
    'tourist':     (.42, .37, .33,  .50, .90, .20,  .20),
    'stranger':    (.32, .18, .36,  .35, .46, .03,  .00),
    'noble':       (.58, .18, .33,  .50, .95, .06,  .05),
    'creep':       (.38, .30, .34,  .45, .85, .14,  .15),
    'temptress':   (.50, .32, .58,  .50, .85, .06,  .22),
}
def sq(im, cx, top, s, cy=None):
    w, h = im.size; side = s * w; x0 = min(max(0, cx * w - side / 2), w - side)
    y0 = cy * h - side / 2 if cy is not None else top * h; y0 = min(max(0, y0), h - side)
    return im.crop((round(x0), round(y0), round(x0 + side), round(y0 + side)))
for sid, (cx, cy, s, bcx, bs, bt, et) in STREET.items():
    name = 'street_' + sid
    im = Image.open(os.path.join(STREET_SRC, sid + '.jpg')).convert('RGB'); w, h = im.size
    p = im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
    save(sq(im, cx, 0, s, cy).resize((160, 160), Image.LANCZOS), 'faces', name)
    save(sq(im, bcx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
    eh = w * 9 / 16; y0 = min(et * h, h - eh)
    e = im.crop((0, round(y0), w, round(y0 + eh))).resize((512, 288), Image.LANCZOS); save(e, 'events', name, 80)
    print(name, p.size, e.size)

# Undercroft encounters. Until a real picture exists these are PLACEHOLDERS drawn from the 32x48 map sprite
# (art/npcs/street_<id>.png) on a dark card. TO SWAP: drop joetopia-art-src/street/<id>.jpg and rerun this script
# (a default crop is used; add a line to STREET above to fine-tune it). The game picks the new files up by id.
from PIL import ImageDraw, ImageFont
UNDER = {'pirates': 'Undercroft Pirates', 'rats': 'Sewer Rat Swarm', 'sailor': 'Drunken Sailor',
         'streetwalker': 'Desperate Streetwalker', 'kraken': 'THE KRAKEN'}
DEFAULT_CROP = (.50, .30, .40, .50, .90, .10, .15)
def font(sz):
    for f in ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf'):
        if os.path.exists(f): return ImageFont.truetype(f, sz)
    return ImageFont.load_default()
def card(w, h, spr, scale, label=None, sy=None):
    im = Image.new('RGB', (w, h), (16, 20, 30)); d = ImageDraw.Draw(im)
    for y in range(h): d.line([(0, y), (w, y)], fill=(16 + y * 20 // h, 22 + y * 30 // h, 34 + y * 40 // h))
    s = spr.resize((spr.width * scale, spr.height * scale), Image.NEAREST)
    im.paste(s, ((w - s.width) // 2, (h - s.height) // 2 if sy is None else sy), s)
    if label:
        f = font(max(12, w // 24)); tw = d.textlength(label, font=f)
        d.rectangle([0, h - f.size - 14, w, h], fill=(0, 0, 0)); d.text(((w - tw) / 2, h - f.size - 9), label, font=f, fill=(255, 210, 120))
    return im
# Real Undercroft art (joetopia-art-src/undercroft/<file>.jpg). Swap an image by dropping a new jpg there and re-running.
UNDER_SRC = os.path.join(os.path.dirname(STREET_SRC), 'undercroft')
UNDER_FILE = {'pirates': 'pirate'}
UNDER_CROP = {  # id: face (cx, cy, s), bust (cx, top, s), portrait box (x0, y0, x1, y1) or None = whole, event box or None = 16:9 from ev_top
    'kraken':       ((.66, .42, .30), (.60, .00, .66), None, (0, .06, 1, .06 + 1712 * 9 / 16 / 1152)),
    'pirates':      ((.50, .22, .32), (.50, .08, .85), None, None),
    'rats':         ((.25, .57, .34), (.33, .22, .64), None, (0, .12, 1, .12 + 1168 * 9 / 16 / 784)),
    'sailor':       ((.41, .22, .22), (.40, .00, .52), None, None),
    'streetwalker': ((.40, .14, .17), (.40, .00, .22), (.22, .00, .58, .46), (.15, .00, .65, .00 + .50 * 1712 * 9 / 16 / 1152)),  # PG-13: upper body only
}
for sid, title in UNDER.items():
    name = 'street_' + sid; ujpg = os.path.join(UNDER_SRC, UNDER_FILE.get(sid, sid) + '.jpg')
    if os.path.exists(ujpg):
        im = Image.open(ujpg).convert('RGB'); w, h = im.size; (fx, fy, fs), (bx, bt, bs), pb, eb = UNDER_CROP[sid]
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', ujpg); continue
    jpg = os.path.join(STREET_SRC, sid + '.jpg')
    if os.path.exists(jpg):
        cx, cy, s, bcx, bs, bt, et = STREET.get(sid, DEFAULT_CROP)
        im = Image.open(jpg).convert('RGB'); w, h = im.size
        p = im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, cx, 0, s, cy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bcx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        eh = min(h, w * 9 / 16); y0 = min(et * h, h - eh)
        save(im.crop((0, round(y0), w, round(y0 + eh))).resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', jpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    face = spr.crop((4, 0, 28, 24)) if sid != 'rats' else spr.crop((0, 16, 32, 48))
    save(card(160, 160, face, 6 if sid != 'rats' else 5), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Scalegate encounters: real art from joetopia-art-src/scalegate/ (duelist, angry_local, parade, bald_fight, fireworks);
# a missing jpg falls back to a placeholder card drawn from the map sprite. TO SWAP: drop joetopia-art-src/scalegate/<id>.jpg
# (duel, angry_local, parade, fireworks, bald_brawl) and re-run this script; add a SCALE_CROP line to fine-tune the crop.
SCALE = {'duel': 'Draconian Duelist', 'angry_local': 'Angry Local', 'parade': 'Martial Parade',
         'fireworks': 'Fireworks over Scalegate', 'bald_brawl': 'Two Bald Brawlers'}
SCALE_SRC = os.path.join(os.path.dirname(STREET_SRC), 'scalegate')
SCALE_FILE = {'duel': 'duelist', 'bald_brawl': 'bald_fight'}  # encounter id -> jpg name when they differ
SCALE_CROP = {  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None = whole, event box or None = 16:9 from the top
    'duel':        ((.43, .13, .20), (.45, .02, .62), None, (0, .04, 1, .04 + 784 * 9 / 16 / 1168)),
    'angry_local': ((.44, .25, .24), (.50, .10, .78), None, (0, .10, 1, .10 + 784 * 9 / 16 / 1168)),
    'bald_brawl':  ((.50, .25, .50), (.50, .05, .62), None, None),  # both brawlers: the break-it-up fight shows this pair
    'fireworks':   ((.53, .28, .40), (.50, .00, .66), None, None),
    'parade':      ((.47, .25, .16), (.47, .10, .42), None, None),
}
for sid, title in SCALE.items():
    name = 'street_' + sid; sjpg = os.path.join(SCALE_SRC, SCALE_FILE.get(sid, sid) + '.jpg')
    if os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size; (fx, fy, fs), (bx, bt, bs), pb, eb = SCALE_CROP.get(sid, ((.5, .3, .4), (.5, .0, .7), None, None))
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Lantern Row encounters (starving_artist, tipsy_muse, acrobats): real art from joetopia-art-src/lantern/<id>.jpg;
# a missing jpg falls back to a placeholder card drawn from the map sprite. TO SWAP: drop joetopia-art-src/lantern/<id>.jpg (starving_artist.jpg, tipsy_muse.jpg, acrobats.jpg) and re-run this script;
# add a LANTERN_CROP line to fine-tune the crop (keep the tipsy muse PG-13: crop to the upper body if needed).
LANTERN = {'starving_artist': 'The Starving Artist', 'tipsy_muse': 'The Tipsy Muse', 'acrobats': 'Street Acrobats'}
LANTERN_SRC = os.path.join(os.path.dirname(STREET_SRC), 'lantern')
LANTERN_CROP = {  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None = whole, event box or None = 16:9 from the top
    'starving_artist': ((.50, .37, .26), (.50, .24, .72), None, (0, .22, 1, .22 + 784 * 9 / 16 / 1168)),
    # PG-13 (as with the Stranger): every copy is cropped head-to-waist, above the shorts; the overall bib stays the focus.
    'tipsy_muse':      ((.50, .14, .20), (.49, .04, .40), (.20, .02, .80, .46), (0, .03, 1, .03 + 1152 * 9 / 16 / 1712)),
    'acrobats':        ((.62, .66, .30), (.50, .00, .67), None, (0, .12, 1, .12 + 1168 * 9 / 16 / 784)),
}
LANTERN_SHADE = {'tipsy_muse': [(.405, .255, .475, .39, 170), (.585, .27, .645, .36, 120)]}
for sid, title in LANTERN.items():
    name = 'street_' + sid; sjpg = os.path.join(LANTERN_SRC, sid + '.jpg')
    if os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        for (x0, y0, x1, y1, a) in LANTERN_SHADE.get(sid, []):  # PG-13: soften the open sides of the overalls into shadow
            from PIL import ImageFilter
            m = Image.new('L', im.size, 0); ImageDraw.Draw(m).ellipse((x0 * w, y0 * h, x1 * w, y1 * h), fill=a)
            im = Image.composite(Image.new('RGB', im.size, (18, 12, 10)), im, m.filter(ImageFilter.GaussianBlur(w * .02)))
        (fx, fy, fs), (bx, bt, bs), pb, eb = LANTERN_CROP.get(sid, ((.5, .25, .35), (.5, .05, .7), None, None))
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Chrome Quarter encounters (courier, public_pooper, discarded_tech, toll_path): PLACEHOLDER cards drawn from the map sprites.
# TO SWAP: drop joetopia-art-src/chrome/<id>.jpg (courier.jpg, public_pooper.jpg, discarded_tech.jpg, toll_path.jpg) and re-run;
# tune with a CHROME_CROP line. Keep the public pooper implied/PG-13 (crop above the waist).
CHROME = {'courier': 'The Courier', 'public_pooper': 'The Public Pooper', 'discarded_tech': 'Discarded Tech', 'toll_path': 'Toll Path'}
CHROME_SRC = os.path.join(os.path.dirname(STREET_SRC), 'chrome')
CHROME_CROP = {}  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None = whole, event box or None = 16:9 from the top
for sid, title in CHROME.items():
    name = 'street_' + sid; sjpg = os.path.join(CHROME_SRC, sid + '.jpg')
    if os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        (fx, fy, fs), (bx, bt, bs), pb, eb = CHROME_CROP.get(sid, ((.5, .25, .35), (.5, .05, .7), None, None))
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')
