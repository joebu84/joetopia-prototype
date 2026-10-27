#!/usr/bin/env python3
"""v1.7 / text 2.7.6 art: Royal Crypt + Eden placeholders and the four flower-girl portraits.
v1.8 / text 2.7.7: + the eight Babylon district backdrops (district_*).
v1.9 / text 2.7.8: + Pastor Evelyn (real art, cropped to face and shoulders).
Additive only (never deletes). Writes:
  joetopia-web/art/{portraits 512, faces 160 sq, busts 256 sq, events 512x288 (landscape sources only)}
  android-text-rpg assets/art/{portraits 800 long side, events 800x450 (landscape only)}  WebP q72
  joetopia-web/text/art (mirror of the APK art) + regenerated text/art/ids.js
Real portraits (flower girls, wolves) are shown whole: no event banner crop, portraits keep the full picture."""
import os
from PIL import Image
SRC = '/workspace/joetopia-art-src'
WEB = '/workspace/joetopia-web/art'
APK = '/workspace/android-text-rpg/app/src/main/assets/art'
TXT = '/workspace/joetopia-web/text/art'
ART = {  # art id -> source (relative to SRC); 'placeholder/' = generated stand-in
    'enemy_evil_spirit': 'placeholder/evil_spirit', 'enemy_zombie_goblin': 'placeholder/zombie_goblin',
    'enemy_graverobbers': 'placeholder/graverobbers', 'enemy_possessed_man': 'placeholder/possessed_man',
    'enemy_necromancer': 'placeholder/necromancer', 'enemy_vampire': 'placeholder/vampire',
    'royal_crypt': 'placeholder/royal_crypt', 'thaddeus_tomb': 'placeholder/thaddeus_tomb', 'crypt_grave': 'placeholder/crypt_grave',
    'enemy_flaming_sword': 'placeholder/flaming_sword', 'enemy_serpent': 'placeholder/serpent',
    'eden_garden': 'placeholder/eden_garden', 'tree_knowledge': 'placeholder/tree_knowledge', 'tree_life': 'placeholder/tree_life',
    'ending_thaddeus': 'placeholder/ending_thaddeus', 'draconian_true': 'placeholder/draconian_true', 'ushapti_true': 'placeholder/ushapti_true',
    # v1.8 / text 2.7.7: Babylon district backdrops (PLACEHOLDERS, 16:9 scenes)
    'district_spire': 'placeholder/district_spire',
    'district_chrome': 'placeholder/district_chrome',
    'district_lantern': 'placeholder/district_lantern',
    'district_scale': 'placeholder/district_scale',
    'district_under': 'placeholder/district_under',
    'district_core': 'placeholder/district_core',
    'district_neon_abyss': 'placeholder/district_neon_abyss',
    'district_docks': 'placeholder/district_docks',
    # real art (user-supplied), uncropped
    'street_flower_girl': 'npc/flower_girl', 'street_flower_girl_blue': 'npc/flower_girl_blue',
    # v1.11.1: near full-body portraits (rose girl framed on her face and upper body); faces/busts still come from the face crops (FACE_SRC)
    'street_sheeple_drink': 'npc/sheeple_girl', 'street_sheeple_dance': 'npc/sheeple_girl_rose',  # v1.12 (t258u): the whole full-body picture
    'enemy_ash_wolf_red_hood': 'enemy/ash_wolf_red_hood', 'enemy_ash_wolf_blue_hood': 'enemy/ash_wolf_blue_hood',
    # v1.9 / text 2.7.8: Pastor Evelyn, REAL art (user-supplied npc/evelyn.jpg), pre-cropped head-to-book (face and shoulders)
    # as npc/evelyn_portrait.jpg: im.crop((205, 22, 655, 502)) of the 784x1168 original.
    'evelyn': 'npc/evelyn',  # v1.12 (t260u): whole full-body original; face/bust icons still from the old head crop (FACE_SRC)
    # v1.9: the two Lost Explorers, REAL art (user-supplied), pre-cropped to face and shoulders:
    # encounter/lost_explorer.jpg .crop((175, 15, 525, 385)); encounter/lost_explorer_crypt.jpg .crop((268, 0, 640, 405)) (head, face, magnifying glass; no cleavage).
    'street_lost_explorer': 'encounter/lost_explorer',  # v1.12: whole full-body original
    'street_crypt_explorer': 'encounter/lost_explorer_crypt',
    # encounter/lost_explorer_undercroft.jpg .crop((110, 0, 690, 620)): sailor cap down to the tablet.
    'street_under_explorer': 'encounter/lost_explorer_undercroft',
    # npc/explorers_guild.jpg .crop((160, 40, 480, 392)): pith helmet + feather down to the neck only (no chest).
    'street_explorers_guild': 'npc/explorers_guild',
    # v1.12 Thistledown (t260u-t265u): REAL art, full body (whole picture); tall Sunflower (944x2096) is padded to 2:3 on a blurred backdrop (PAD)
    'sunflower': 'npc/sunflower', 'street_td_cotton': 'npc/cotton', 'street_td_explorer': 'npc/sheeple_explorer_library',
    'street_td_foxtail': 'npc/father_foxtail', 'street_td_veteran': 'npc/sheeple_veteran',  # Old Burdock (t266u)
    'street_td_constable': 'npc/sheeple_constable',  # Constable Rhubarb (t267u); also stands in for the Sheeple Soldiers in fights
    # generated stand-ins (no real people): the meadow village and two villagers
    'thistledown': 'placeholder/thistledown', 'street_td_villager_woman': 'placeholder/td_villager_woman',
    'street_td_villager_man': 'placeholder/td_villager_man',
}
from PIL import ImageFilter
def save(im, root, sub, name, q):
    os.makedirs(os.path.join(root, sub), exist_ok=True); im.save(os.path.join(root, sub, name + '.webp'), 'WEBP', quality=q, method=6)
def sq(im, cy, s):
    w, h = im.size; s = round(min(w, h) * s); cx = w / 2; y0 = max(0, min(h - s, round(cy * h - s / 2)))
    return im.crop((round(cx - s / 2), y0, round(cx + s / 2), y0 + s))
def wide(im, W, H):
    w, h = im.size; eh = w * H / W
    if eh <= h: y0 = (h - eh) / 2; return im.crop((0, round(y0), w, round(y0 + eh))).resize((W, H), Image.LANCZOS)
    ew = h * W / H; x0 = (w - ew) / 2; return im.crop((round(x0), 0, round(x0 + ew), h)).resize((W, H), Image.LANCZOS)
FACE_SRC = {'street_sheeple_drink': 'npc/sheeple_girl_face', 'street_sheeple_dance': 'npc/sheeple_girl_rose_face',
            'evelyn': 'npc/evelyn_portrait', 'street_lost_explorer': 'encounter/lost_explorer_portrait',
            'street_crypt_explorer': 'encounter/lost_explorer_crypt_portrait', 'street_under_explorer': 'encounter/lost_explorer_undercroft_portrait',
            'street_explorers_guild': 'npc/explorers_guild_portrait'}
FACE_AT = {  # full-body sources without a face crop: (face cy, face s, bust cy, bust s) as fractions (sq())
    'sunflower': (.14, .5, .22, .85), 'street_td_cotton': (.22, .36, .32, .7), 'street_td_explorer': (.21, .34, .33, .7),
    'street_td_foxtail': (.16, .34, .27, .7), 'street_td_veteran': (.2, .36, .3, .72), 'street_td_constable': (.15, .36, .25, .72), 'street_td_villager_woman': (.22, .4, .32, .75), 'street_td_villager_man': (.2, .4, .3, .75)}
PAD = {'sunflower'}  # taller than 2:3: pad (never stretch) to 2:3 on a blurred copy of itself
LETTERBOX = {'street_td_veteran', 'street_td_constable', 'evelyn', 'sunflower', 'street_td_cotton', 'street_td_explorer', 'street_td_foxtail', 'street_td_villager_woman', 'street_td_villager_man', 'street_flower_girl', 'street_flower_girl_blue', 'street_sheeple_drink', 'street_sheeple_dance', 'street_lost_explorer', 'street_crypt_explorer', 'street_under_explorer', 'street_explorers_guild'}  # web encounter banner: the WHOLE portrait centred on a blurred backdrop (no crop)
def letterbox(im, W, H):
    bg = wide(im, W, H).filter(ImageFilter.GaussianBlur(18)); bg = Image.blend(bg, Image.new('RGB', (W, H), (12, 10, 16)), .45)
    fg = im.copy(); fg.thumbnail((W, H), Image.LANCZOS); bg.paste(fg, ((W - fg.size[0]) // 2, (H - fg.size[1]) // 2)); return bg
for nid, src in ART.items():
    im = Image.open(os.path.join(SRC, src + '.jpg')).convert('RGB'); land = im.size[0] > im.size[1]
    if nid in PAD:
        w, h = im.size; W = round(h * 2 / 3); bg = wide(im, W, h).filter(ImageFilter.GaussianBlur(30)); bg = Image.blend(bg, Image.new('RGB', (W, h), (12, 10, 16)), .35)
        bg.paste(im, ((W - w) // 2, 0)); im = bg
    p = im.copy(); p.thumbnail((512, 512), Image.LANCZOS); save(p, WEB, 'portraits', nid, 82)
    save(sq(im, .5 if land else .2, .55 if land else .45).resize((160, 160), Image.LANCZOS), WEB, 'faces', nid, 82)
    save(sq(im, .5 if land else .33, 1 if land else .75).resize((256, 256), Image.LANCZOS), WEB, 'busts', nid, 82)
    p = im.copy(); p.thumbnail((800, 800), Image.LANCZOS)
    for root in (APK, TXT): save(p, root, 'portraits', nid, 72)
    if land:
        save(wide(im, 512, 288), WEB, 'events', nid, 80)
        e = wide(im, 800, 450)
        for root in (APK, TXT): save(e, root, 'events', nid, 72)
    if nid in LETTERBOX: save(letterbox(im, 512, 288), WEB, 'events', nid, 80)
    print(nid, im.size, 'landscape' if land else 'portrait')
    if nid in FACE_AT:
        a = Image.open(os.path.join(SRC, src + '.jpg')).convert('RGB')
        save(sq(a, FACE_AT[nid][0], FACE_AT[nid][1]).resize((160, 160), Image.LANCZOS), WEB, 'faces', nid, 82)
        save(sq(a, FACE_AT[nid][2], FACE_AT[nid][3]).resize((256, 256), Image.LANCZOS), WEB, 'busts', nid, 82)
    if nid in FACE_SRC:  # small face / bust icons from the dedicated face crop
        f = Image.open(os.path.join(SRC, FACE_SRC[nid] + '.jpg')).convert('RGB')
        save(sq(f, .5, .55).resize((160, 160), Image.LANCZOS), WEB, 'faces', nid, 82)
        save(sq(f, .5, 1).resize((256, 256), Image.LANCZOS), WEB, 'busts', nid, 82)
names = lambda sub: sorted(f[:-5] for f in os.listdir(os.path.join(TXT, sub)) if f.endswith('.webp'))
por, ev = names('portraits'), names('events')
open(os.path.join(TXT, 'ids.js'), 'w').write('window.TEXT_ART="%s";\nwindow.TEXT_ART_FOLDERS={portraits:new Set("%s".split(\',\')),events:new Set("%s".split(\',\'))};\n' % (','.join(sorted(set(por) | set(ev))), ','.join(por), ','.join(ev)))
print('ids.js', len(set(por) | set(ev)))
