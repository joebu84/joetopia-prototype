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
        if eb == 'COMPOSITE':
            (lb, rb) = SPIRE_COMPOSITE[sid]; L = box(lb); R = box(rb)
            L = L.resize((round(L.size[0] * 288 / L.size[1]), 288), Image.LANCZOS); R = R.resize((round(R.size[0] * 288 / R.size[1]), 288), Image.LANCZOS)
            e = Image.new('RGB', (L.size[0] + R.size[0], 288)); e.paste(L, (0, 0)); e.paste(R, (L.size[0], 0))
            save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg, 'composite', e.size); continue
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
        if eb == 'COMPOSITE':
            (lb, rb) = SPIRE_COMPOSITE[sid]; L = box(lb); R = box(rb)
            L = L.resize((round(L.size[0] * 288 / L.size[1]), 288), Image.LANCZOS); R = R.resize((round(R.size[0] * 288 / R.size[1]), 288), Image.LANCZOS)
            e = Image.new('RGB', (L.size[0] + R.size[0], 288)); e.paste(L, (0, 0)); e.paste(R, (L.size[0], 0))
            save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg, 'composite', e.size); continue
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
        if eb == 'COMPOSITE':
            (lb, rb) = SPIRE_COMPOSITE[sid]; L = box(lb); R = box(rb)
            L = L.resize((round(L.size[0] * 288 / L.size[1]), 288), Image.LANCZOS); R = R.resize((round(R.size[0] * 288 / R.size[1]), 288), Image.LANCZOS)
            e = Image.new('RGB', (L.size[0] + R.size[0], 288)); e.paste(L, (0, 0)); e.paste(R, (L.size[0], 0))
            save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg, 'composite', e.size); continue
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Chrome Quarter encounters (courier, rude_worker, discarded_tech, toll_path). All four use REAL art:
# courier.jpg, rude_worker.jpg, broken_tech.jpg (-> discarded_tech) and toll.jpg (-> toll_path).
# TO SWAP: replace joetopia-art-src/chrome/<file>.jpg (see CHROME_FILE for renamed sources) and re-run;
# tune with a CHROME_CROP line.
CHROME = {'courier': 'The Courier', 'rude_worker': 'Rude Out-of-Town Worker', 'discarded_tech': 'Discarded Tech', 'toll_path': 'Toll Path'}
CHROME_SRC = os.path.join(os.path.dirname(STREET_SRC), 'chrome')
CHROME_FILE = {'discarded_tech': 'broken_tech', 'toll_path': 'toll'}  # encounter id -> source jpg name, when they differ
CHROME_CROP = {
    'rude_worker': ((.51, .365, .33), (.5, .2, .75), None, (0, .2, 1, .5785)),
    'discarded_tech': ((.52, .55, .45), (.5, .3, .8), None, (0, .38, 1, .7576)),
    'courier': ((.50, .285, .3), (.55, .2, .75), None, (0, .23, 1, .6076)),
    'toll_path': ((.53, .5, .28), (.53, .25, .5), (.25, 0, .75, 1), (0, .1, 1, .938)),
}  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None = whole, event box or None = 16:9 from the top
for sid, title in CHROME.items():
    name = 'street_' + sid; sjpg = os.path.join(CHROME_SRC, CHROME_FILE.get(sid, sid) + '.jpg')
    if os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        (fx, fy, fs), (bx, bt, bs), pb, eb = CHROME_CROP.get(sid, ((.5, .25, .35), (.5, .05, .7), None, None))
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        if eb == 'COMPOSITE':
            (lb, rb) = SPIRE_COMPOSITE[sid]; L = box(lb); R = box(rb)
            L = L.resize((round(L.size[0] * 288 / L.size[1]), 288), Image.LANCZOS); R = R.resize((round(R.size[0] * 288 / R.size[1]), 288), Image.LANCZOS)
            e = Image.new('RGB', (L.size[0] + R.size[0], 288)); e.paste(L, (0, 0)); e.paste(R, (L.size[0], 0))
            save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg, 'composite', e.size); continue
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Gilded Spire encounters (runaway_chariot, reality_show + its episodes, lost_jewelry, charity_gala). All use REAL art from
# joetopia-art-src/spire/: chariot.jpg, reality_show.jpg (the fictional celebrity Valeria Kurigalzu; cropped head-to-hips
# for PG-13), jewelry.jpg, charity.jpg. The private-guards fight reuses the chariot driver's picture (see art.js enemyArt).
# TO SWAP: replace a jpg (names in SPIRE_FILE) and re-run; tune with a SPIRE_CROP line.
SPIRE = {'runaway_chariot': 'Runaway Chariot', 'reality_show': 'Reality Show', 'lost_jewelry': 'Lost Jewelry', 'charity_gala': 'Charity Gala',
         # reality-show EPISODES other than the Kurigalzus (Street.EPISODES art ids)
         'reality_pushup': 'Push-Up Challenge', 'reality_blind_date': 'Blind Date a Noble', 'reality_makeup': 'Makeup Tutorial', 'reality_fletcher': 'Fletcher Chats', 'reality_petyr': "Petyr's Interview",
         # Wizard Couriers (wizard_courier.jpg: red-robed wizard offering an amber vial to a man in a toga; the wizard fight reuses it)
         'wizard_couriers': 'Wizard Couriers', 'adrenochrome': 'Adrenochrome Vial'}
SPIRE_SRC = os.path.join(os.path.dirname(STREET_SRC), 'spire')
SPIRE_FILE = {'runaway_chariot': 'chariot', 'lost_jewelry': 'jewelry', 'charity_gala': 'charity',
              'reality_pushup': 'togiru', 'reality_blind_date': 'blind_date_noble', 'reality_makeup': 'bathsheba', 'reality_fletcher': 'fletcher', 'reality_petyr': 'petyr',
              'wizard_couriers': 'wizard_courier', 'adrenochrome': 'wizard_courier'}  # encounter id -> source jpg name, when they differ
SPIRE_CROP = {
    'runaway_chariot': ((.503, .21, .1), (.5, .1, .36), (.2, 0, .8, .85), (0, .05, 1, .886)),
    'reality_show': ((.5, .16, .22), (.5, .07, .6), (.12, .02, .88, .52), (0, .04, 1, .27)),
    'charity_gala': ((.55, .31, .36), (.5, .2, .8), None, (0, .2, 1, .578)),
    'lost_jewelry': ((.5, .65, .55), (.5, .45, .8), None, (0, .5, 1, .878)),
    'reality_pushup': ((.47, .13, .28), (.5, .04, .7), None, (0, .03, 1, .407)),
    # PG-13 like the Stranger: the noble and Bathsheba are cut at the shoulders/upper chest (no cleavage or legs)
    'reality_blind_date': ((.79, .23, .16), (.82, .02, .26), (.66, .02, .98, .43), 'COMPOSITE'),
    'reality_makeup': ((.53, .36, .25), (.55, .18, .48), (.1, .12, .95, .49), (0, .13, 1, .508)),
    'reality_fletcher': ((.48, .26, .22), (.5, .15, .6), None, (0, .12, 1, .497)),
    'reality_petyr': ((.55, .30, .3), (.5, .08, .8), None, (0, .05, 1, .427)),
    # landscape 1712x1152: face/bust on the wizard (left), whole picture as portrait, 16:9 banner keeps wizard, vial and the toga man
    'wizard_couriers': ((.37, .37, .2), (.33, .05, .58), None, (0, .07, 1, .906)),
    # the vial in the wizard's hand (item picture for Adrenochrome log lines)
    'adrenochrome': ((.52, .56, .1), (.52, .42, .2), (.40, .40, .64, .76), (.30, .38, .74, .748)),
}
# event banners built from two crops side by side (left box, right box), each fractions of the source
SPIRE_COMPOSITE = {'reality_blind_date': ((.18, .32, .395, .78), (.655, 0, .968, .43))}  # floating camera + table | her face  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None = whole, event box or None = 16:9 from the top
for sid, title in SPIRE.items():
    name = 'street_' + sid; sjpg = os.path.join(SPIRE_SRC, SPIRE_FILE.get(sid, sid) + '.jpg')
    if os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        (fx, fy, fs), (bx, bt, bs), pb, eb = SPIRE_CROP.get(sid, ((.5, .25, .35), (.5, .05, .7), None, None))
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        if eb == 'COMPOSITE':
            (lb, rb) = SPIRE_COMPOSITE[sid]; L = box(lb); R = box(rb)
            L = L.resize((round(L.size[0] * 288 / L.size[1]), 288), Image.LANCZOS); R = R.resize((round(R.size[0] * 288 / R.size[1]), 288), Image.LANCZOS)
            e = Image.new('RGB', (L.size[0] + R.size[0], 288)); e.paste(L, (0, 0)); e.paste(R, (L.size[0], 0))
            save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg, 'composite', e.size); continue
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Toadstool Forest encounters (Forest.kt). REAL art from joetopia-art-src/forest/<id>.jpg: troll, weirdo (the bearded woodsman),
# trustworthy_human (the felt-puppet "human"), goblin_banger (RED crew: blue skin, red bandana, energy SMG), goblin_banger_blue (BLUE crew: red skin, blue bandana, revolver; either can be the goblin inside the human), unicorn, pixie. The gnome is a PLACEHOLDER card (drop forest/gnome.jpg and rerun).
# PG-13: the pixie picture is cropped to head, shoulders and upper wings for EVERY output (portrait, face, bust, event);
# nothing below the collarbone ships, and the full pixie.jpg is never copied anywhere.
# Item pictures: unicorn_horn (the horn cropped from unicorn.jpg), pixie_wings (a wing cropped from pixie.jpg, wings only);
# gnome kit and unicorn gear are sprite cards (tools/make-npc-sprites.py).
FOREST = {'troll': 'Bridge Troll', 'weirdo': 'Weirdo in the Woods', 'trustworthy_human': 'Trustworthy Normal Human', 'goblin_banger': 'Goblin Banger', 'goblin_banger_blue': 'Blue Goblin Banger', 'goblin_unaffiliated': 'Unaffiliated Goblins', 'bigfoot': 'Bigfoot!',
          'unicorn': 'Unicorn', 'pixie': 'Pixie', 'gnome': 'Forest Gnome',
          'unicorn_horn': 'Unicorn Horn', 'pixie_wings': 'Pixie Wings', 'gnome_hat': 'Gnome Hat', 'work_jeans': "Worker's Jeans",
          'flannel_shirt': 'Flannel Shirt', 'woodsman_axe': "Woodsman's Axe", 'unicorn_wand': 'Unicorn Wand', 'unicorn_sword': 'Unicorn Sword',
          'unicorn_heels': 'Unicorn Heels', 'goblin_zapper': 'Goblin Zapper SMG', 'banger_bandana': 'Banger Bandana',
          'red_shiv': 'Red-Taped Shiv', 'bike_chain': 'Goblin Bike Chain', 'stem_bat': 'Mushroom-Stem Bat',
          'goblin_revolver': 'Goblin Six-Shooter', 'blue_bandana': 'Blue Bandana', 'blue_shiv': 'Blue-Taped Shiv', 'goblin_slingshot': 'Goblin Slingshot', 'big_booma': 'Da Big Booma', 'ballistic_hat': 'Ballistic Hat'}
FOREST_SRC = os.path.join(os.path.dirname(STREET_SRC), 'forest')
FOREST_FILE = {'unicorn_horn': 'unicorn', 'pixie_wings': 'pixie'}
FOREST_CROP = {  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None, event box or None (fractions of the source)
    'troll': ((.50, .17, .13), (.55, .02, .5), None, (0, .05, 1, .888)),
    'weirdo': ((.52, .21, .25), (.50, .10, .75), None, (0, .06, 1, .437)),
    'goblin_banger': ((.41, .27, .17), (.45, .04, .55), None, (0, .08, 1, .918)),
    'goblin_banger_blue': ((.50, .38, .35), (.50, .25, .75), None, (0, .22, 1, .598)),
    # landscape 1168x784: face = the squatting middle goblin, bust = all three heads, event = the whole crew
    'goblin_unaffiliated': ((.50, .55, .16), (.50, .22, .62), None, (0, .10, 1, .941)),
    # landscape 1168x784: face = the mother, bust = mother + baby, event = the whole mushroom glade
    'bigfoot': ((.39, .25, .17), (.40, .10, .56), None, (0, .04, 1, .92)),
    'trustworthy_human': ((.52, .33, .40), (.55, .15, .80), None, (0, .12, 1, .497)),
    'unicorn': ((.53, .76, .14), (.62, .25, .55), None, (0, .10, 1, .938)),
    # PG-13: everything stops above the collarbone (y < .25 of the 784x1168 source)
    'pixie': ((.49, .16, .22), (.49, .02, .29), (.12, 0, .92, .25), (.16, 0, .82, .25)),
    'unicorn_horn': ((.47, .63, .12), (.47, .52, .16), (.40, .50, .56, .78), (.30, .52, .66, .76)),
    'pixie_wings': ((.80, .29, .22), (.80, .19, .24), (.68, .19, .94, .41), (.62, .19, .98, .39)),
}
for sid, title in FOREST.items():
    name = 'street_' + sid; sjpg = os.path.join(FOREST_SRC, FOREST_FILE.get(sid, sid) + '.jpg')
    if sid in FOREST_CROP and os.path.exists(sjpg):
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        (fx, fy, fs), (bx, bt, bs), pb, eb = FOREST_CROP[sid]
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        e = box(eb) if eb else im.crop((0, 0, w, round(min(h, w * 9 / 16))))
        save(e.resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + (' (placeholder art)' if sid == 'gnome' else '')), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24) if sid != 'gnome' else (4, 8, 28, 32)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'card')

# Dance-floor encounters: real art from joetopia-art-src/dance/<file>.jpg (water, dj, pickpocket, boyfriend, complimentary_drinks).
# PG-13: the pickpocket is cropped to face + shoulders; the server to head, shoulders and her tray; on the boyfriend card the
# girlfriend behind him is cropped/shaded so only her face reads. TO SWAP: replace a jpg and re-run; tune with a DANCE_CROP line.
DANCE = {'dance_water': 'Bro, can you buy me a water?', 'dance_dj': 'The DJ shout-out', 'dance_pickpocket': 'Pickpocket in the crowd',
         'dance_boyfriend': 'Are you looking at my girl?', 'dance_drinks': 'Complimentary drinks'}
DANCE.update({'dance_stranger_%d' % i: 'A stranger asks you to dance' for i in range(1, 6)})
DANCE_SRC = os.path.join(os.path.dirname(STREET_SRC), 'dance')
DANCE_FILE = {'dance_water': 'water', 'dance_dj': 'dj', 'dance_pickpocket': 'pickpocket', 'dance_boyfriend': 'boyfriend', 'dance_drinks': 'complimentary_drinks'}
DANCE_FILE.update({'dance_stranger_%d' % i: 'stranger_%d' % i for i in range(1, 6)})
# Strangers: 1 alien (Groucho glasses), 2 bearded old man, 3 scarab dancer (stranger_3.jpg is ALREADY the PG-13 face + shoulders crop,
# the top 38% of the original), 4 man in an open vest pointing, 5 man in a tunic reaching out. Sources 784x1168 (3: 784x444).
H169 = 784 * 9 / 16 / 1168
DANCE_CROP = {  # id: face (cx, cy, s), bust (cx, top, s), portrait box or None, event box (16:9 in source pixels)
    'dance_water': ((.50, .21, .22), (.52, .08, .55), (0, .04, 1, .62), (0, .08, 1, .08 + 1152 * 9 / 16 / 1712)),
    'dance_dj': ((.53, .30, .22), (.52, .07, .60), None, (0, .08, 1, .08 + 1264 * 9 / 16 / 1568)),
    'dance_pickpocket': ((.47, .24, .20), (.47, .03, .36), (.12, .02, .88, .35), (.12, .04, .88, .04 + .76 * 784 * 9 / 16 / 1168)),
    'dance_boyfriend': ((.37, .31, .20), (.40, .09, .50), (0, .08, .78, .62), (0, .08, 1, .08 + 784 * 9 / 16 / 1168)),
    'dance_drinks': ((.47, .22, .18), (.55, .06, .55), (.10, .04, 1, .52), (0, .14, 1, .14 + 784 * 9 / 16 / 1168)),
    'dance_stranger_1': ((.49, .24, .26), (.48, .06, .60), (0, .02, 1, .62), (0, .08, 1, .08 + H169)),
    'dance_stranger_2': ((.30, .27, .24), (.38, .08, .60), (0, .04, 1, .62), (0, .10, 1, .10 + H169)),
    'dance_stranger_3': ((.43, .62, .30), (.45, 0, .56), None, (0, 0, 1, 441 / 444)),
    'dance_stranger_4': ((.45, .18, .24), (.45, .04, .60), (0, 0, 1, .62), (0, .04, 1, .04 + H169)),
    'dance_stranger_5': ((.42, .18, .24), (.45, .04, .60), (0, 0, 1, .62), (0, .04, 1, .04 + H169)),
}
# Bar drinkers ("A stranger invites you to drink"): joetopia-art-src/bar/drinker_1..6.jpg. PG-13: 1 is ALREADY cropped to face + necklace
# (922x599), 4 to face + hair only (455x350), 5 to face + hair down to the collar (830x616); 2, 3 and 6 are as-is (784x1168, 6: 1152x1712).
DANCE.update({'bar_drinker_%d' % i: 'A stranger invites you to drink' for i in range(1, 7)})
DANCE_FILE.update({'bar_drinker_%d' % i: '../bar/drinker_%d' % i for i in range(1, 7)})
DANCE_CROP.update({
    'bar_drinker_1': ((.55, .62, .42), (.55, 0, .64), None, (0, 0, 1, 922 * 9 / 16 / 599)),
    'bar_drinker_2': ((.62, .42, .30), (.55, .25, .60), (0, .15, 1, .75), (0, .28, 1, .28 + H169)),
    'bar_drinker_3': ((.55, .29, .26), (.62, .05, .60), (0, 0, 1, .62), (0, .05, 1, .05 + H169)),
    'bar_drinker_4': ((.55, .55, .55), (.50, 0, .76), None, (0, .10, 1, .10 + 455 * 9 / 16 / 350)),
    'bar_drinker_5': ((.50, .55, .45), (.50, 0, .74), None, (0, .05, 1, .05 + 830 * 9 / 16 / 616)),
    'bar_drinker_6': ((.47, .32, .26), (.50, .04, .60), (0, 0, 1, .62), (0, .06, 1, .06 + 1152 * 9 / 16 / 1712)),
})
DANCE_SHADE = {'dance_boyfriend': [(.66, .42, 1.0, .70, 235)]}  # the girlfriend's torso goes into shadow behind him
for sid, title in DANCE.items():
    name = 'street_' + sid; sjpg = os.path.join(DANCE_SRC, DANCE_FILE[sid] + '.jpg')
    if os.path.exists(sjpg):
        from PIL import ImageFilter
        im = Image.open(sjpg).convert('RGB'); w, h = im.size
        for (x0, y0, x1, y1, a) in DANCE_SHADE.get(sid, []):
            m = Image.new('L', im.size, 0); ImageDraw.Draw(m).ellipse((x0 * w, y0 * h, x1 * w + w * .2, y1 * h), fill=a)
            im = Image.composite(Image.new('RGB', im.size, (20, 8, 30)), im, m.filter(ImageFilter.GaussianBlur(w * .03)))
        (fx, fy, fs), (bx, bt, bs), pb, eb = DANCE_CROP[sid]
        box = lambda b: im.crop((round(b[0] * w), round(b[1] * h), round(b[2] * w), round(b[3] * h)))
        p = box(pb) if pb else im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', name)
        save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', name)
        save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', name)
        save(box(eb).resize((512, 288), Image.LANCZOS), 'events', name, 80); print(name, 'from', sjpg); continue
    spr = Image.open(os.path.join(ART, 'npcs', name + '.png')).convert('RGBA')
    save(card(384, 512, spr, 8, title + ' (placeholder art)'), 'portraits', name)
    save(card(160, 160, spr.crop((4, 0, 28, 24)), 6), 'faces', name)
    save(card(256, 256, spr, 5), 'busts', name)
    save(card(512, 288, spr, 5, title), 'events', name, 80)
    print(name, 'placeholder')

# Named talk NPCs with real art (district hosts etc.), keyed by the Kotlin NPC id: joetopia-art-src/npc/<file>.jpg.
# Whole picture for the portrait, a square head crop for the face, a head-to-chest square for the bust. No event banner.
# TO ADD ONE: drop the jpg in joetopia-art-src/npc/, add a line here, a sprite in make-npc-sprites.py and an id in data/art.js.
NPC_SRC = os.path.dirname(STREET_SRC)  # joetopia-art-src root (npc/, enemy/, boss/)
NPC_ART = {  # id: (file under joetopia-art-src, (face cx, cy, s), (bust cx, top, s))
    'lantern_poet':        ('npc/miriam_inkwell',        (.44, .245, .32), (.52, .08, .74)),
    'dealer_tamar':        ('npc/tamar_glitch',          (.32, .55, .40),  (.45, 0, .643)),
    'shamgar':             ('npc/shamgar',               (.56, .11, .22),  (.50, .02, .75)),
    'dr_spore':            ('npc/dr_spore',              (.52, .21, .32),  (.50, .03, .80)),
    'priscilla_talk':      ('npc/old_priscilla',         (.47, .18, .34),  (.50, .02, .85)),
    'barnabas_talk':       ('npc/barnabas',              (.53, .19, .30),  (.50, .02, .85)),
    'ushapti_smuggler':    ('enemy/ushapti_smuggler',    (.38, .42, .28),  (.45, .22, .75)),
    'draconian_bodyguard': ('enemy/draconian_bodyguard', (.50, .10, .26),  (.50, 0, .80)),
    'ash_cultist':         ('enemy/ash_cultist',         (.50, .17, .28),  (.50, .04, .75)),
    'enlil_ka':            ('boss/enlil_ka',             (.36, .16, .30),  (.45, .03, .80)),
    'marduk_ra':           ('boss/marduk_ra',            (.44, .16, .26),  (.45, .02, .80)),
    'inanna_shar':         ('boss/inanna_shar',          (.48, .17, .26),  (.50, .02, .80)),
    'ushapti_broker':      ('boss/ushapti_broker',       (.50, .29, .30),  (.50, .12, .85)),
    'under_boss':          ('npc/big_jehoshaphat',       (.40, .10, .30),  (.40, 0, .80)),   # Big Jehoshaphat, Undercroft
    'scale_veteran':       ('npc/ssarru_kin',            (.45, .11, .25),  (.50, .02, .75)),  # Ssarru-Kin, Scalegate
    'thornback_alpha':     ('boss/thornback_alpha',      (.63, .37, .35),  (.55, .15, .85)),  # Toadstool Forest boss (enemy alpha)
}
for nid, (fname, (fx, fy, fs), (bx, bt, bs)) in NPC_ART.items():
    im = Image.open(os.path.join(NPC_SRC, fname + '.jpg')).convert('RGB')
    p = im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, 'portraits', nid)
    save(sq(im, fx, 0, fs, fy).resize((160, 160), Image.LANCZOS), 'faces', nid)
    save(sq(im, bx, bt, bs).resize((256, 256), Image.LANCZOS), 'busts', nid)
    print(nid, 'from', fname)
