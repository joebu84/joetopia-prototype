#!/usr/bin/env python3
"""Draws the 32x48 map sprites for the named characters (matched to their portraits).
Run: python3 tools/make-npc-sprites.py  -> art/npcs/<id>.png. Edit a function below to restyle one,
or just replace the PNG with hand-made art at the same path (or point data/art.js npcs.<id> elsewhere)."""
from PIL import Image, ImageDraw
import os
OUT = os.path.join(os.path.dirname(__file__), '..', 'art', 'npcs')
W, H = 32, 48

def canvas():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); return im, ImageDraw.Draw(im)
def R(d, x0, y0, x1, y1, c): d.rectangle([x0, y0, x1, y1], fill=c)
def P(d, pts, c):
    for x, y in pts: d.point((x, y), fill=c)
def shadow(d): d.ellipse([7, 44, 24, 47], fill=(0, 0, 0, 90))
def head(d, skin, top=6, eyes=(20, 20, 30)):
    R(d, 11, top + 2, 20, top + 12, skin); R(d, 12, top + 1, 19, top + 13, skin)
    P(d, [(13, top + 7), (14, top + 7), (17, top + 7), (18, top + 7)], eyes)
    P(d, [(15, top + 10), (16, top + 10)], tuple(max(0, v - 60) for v in skin[:3]))
def legs(d, c, top=36, bot=44, shoe=(30, 24, 20)):
    R(d, 12, top, 15, bot, c); R(d, 17, top, 20, bot, c); R(d, 11, bot + 1, 15, bot + 2, shoe); R(d, 17, bot + 1, 21, bot + 2, shoe)
def arms(d, c, skin, top=19, bot=31):
    R(d, 7, top + 1, 9, bot, c); R(d, 22, top + 1, 24, bot, c); R(d, 7, bot + 1, 9, bot + 2, skin); R(d, 22, bot + 1, 24, bot + 2, skin)

SK_L, SK_M, SK_T, SK_D = (240, 200, 165), (215, 165, 125), (190, 135, 95), (150, 100, 70)
BLK, NIGHT = (18, 16, 22), (34, 30, 44)

def robert():  # VIP-door bouncer: slicked black hair, blue-lens shades, long black coat, badge
    im, d = canvas(); shadow(d)
    legs(d, BLK, 38, 44, (10, 10, 12))
    R(d, 9, 19, 22, 40, NIGHT); R(d, 10, 19, 21, 41, NIGHT); R(d, 15, 20, 16, 40, (60, 60, 80))  # coat + seam
    P(d, [(10, y) for y in range(20, 41)] + [(21, y) for y in range(20, 41)], (70, 70, 95))
    arms(d, NIGHT, SK_L, 19, 33)
    R(d, 12, 23, 13, 25, (200, 205, 220)); P(d, [(12, 24)], (90, 160, 255))  # badge
    R(d, 13, 18, 18, 19, SK_L); head(d, SK_L, 5)
    R(d, 11, 4, 20, 7, BLK); R(d, 10, 5, 11, 10, BLK); R(d, 20, 5, 21, 10, BLK)  # slicked hair
    R(d, 11, 11, 20, 13, BLK); R(d, 12, 11, 14, 12, (60, 170, 255)); R(d, 17, 11, 19, 12, (60, 170, 255))  # shades
    P(d, [(12, 11), (17, 11)], (200, 240, 255))
    return im

def ramirez():  # Brute Squad captain: long purple-black hair, pink visor, black tactical gear, armband
    im, d = canvas(); shadow(d); hair = (45, 22, 60)
    legs(d, BLK, 34, 44, (10, 10, 12))
    R(d, 9, 19, 22, 34, (28, 28, 34)); R(d, 11, 21, 20, 30, (45, 45, 55))  # vest
    P(d, [(12, 24), (14, 24), (17, 24), (19, 24), (12, 27), (19, 27)], (90, 90, 105))  # pouches
    R(d, 10, 32, 21, 33, (70, 60, 40)); P(d, [(15, 32), (16, 32)], (200, 180, 90))  # belt
    arms(d, (28, 28, 34), SK_T, 19, 31)
    R(d, 7, 23, 9, 25, (150, 60, 220)); P(d, [(8, 24)], (255, 255, 255))  # BRUTE SQUAD armband
    R(d, 13, 18, 18, 19, SK_T); head(d, SK_T, 5)
    R(d, 10, 3, 21, 7, hair); R(d, 8, 5, 10, 24, hair); R(d, 21, 5, 23, 24, hair); P(d, [(9, 25), (22, 25), (8, 26)], hair)
    P(d, [(12, 3), (16, 4), (19, 3)], (110, 60, 150))  # purple sheen
    R(d, 11, 11, 20, 12, (255, 80, 200)); P(d, [(12, 11), (13, 11)], (255, 200, 240))  # pink visor
    R(d, 12, 15, 19, 17, (120, 80, 60)); R(d, 14, 15, 17, 15, SK_T)  # beard
    return im

def rob():  # technomancer: circuit lines on face, high-collared black coat with cyan glow
    im, d = canvas(); shadow(d); cy = (60, 230, 255)
    legs(d, BLK, 36, 44, (10, 10, 12))
    R(d, 9, 19, 22, 38, (20, 22, 32)); arms(d, (20, 22, 32), SK_L, 19, 31)
    P(d, [(12, y) for y in range(22, 37, 2)] + [(19, y) for y in range(21, 37, 3)] + [(13, 30), (14, 30), (18, 26), (17, 26)], cy)
    P(d, [(8, 22), (8, 25), (23, 24), (23, 28)], cy)
    R(d, 13, 18, 18, 19, SK_L); head(d, SK_L, 5)
    R(d, 9, 13, 11, 20, (20, 22, 32)); R(d, 20, 13, 22, 20, (20, 22, 32)); P(d, [(9, y) for y in range(13, 20)] + [(22, y) for y in range(13, 20)], cy)  # collar
    R(d, 11, 3, 20, 7, (40, 30, 25)); R(d, 10, 5, 11, 9, (40, 30, 25)); P(d, [(14, 8), (18, 8)], (40, 30, 25))
    P(d, [(12, 14), (12, 15), (13, 16), (19, 14), (19, 15), (18, 16), (11, 10)], cy)  # face circuits
    P(d, [(13, 12), (18, 12)], (150, 240, 255))  # glowing eyes
    return im

def joseph():  # TikTok pastor: beard, red and gold vestments, ring of fire halo
    im, d = canvas(); shadow(d); red, gold = (170, 25, 30), (235, 185, 60)
    d.ellipse([5, 0, 26, 21], outline=(255, 140, 30)); d.ellipse([6, 1, 25, 20], outline=(255, 210, 80))
    P(d, [(5, 6), (26, 6), (7, 2), (24, 2), (4, 11), (27, 11)], (255, 90, 20))
    R(d, 9, 19, 22, 44, red); R(d, 8, 30, 23, 44, red); R(d, 14, 19, 17, 44, gold)  # robe + stole
    P(d, [(15, 24), (16, 24), (15, 25), (16, 25), (14, 26), (17, 26), (15, 27), (16, 27)], red)  # cross on stole
    R(d, 8, 43, 23, 44, gold); arms(d, red, SK_M, 19, 30); R(d, 7, 29, 9, 30, gold); R(d, 22, 29, 24, 30, gold)
    R(d, 11, 45, 14, 46, (60, 30, 20)); R(d, 17, 45, 20, 46, (60, 30, 20))
    head(d, SK_M, 5)
    R(d, 11, 3, 20, 7, (40, 25, 15)); R(d, 10, 5, 11, 10, (40, 25, 15)); R(d, 20, 5, 21, 10, (40, 25, 15))
    R(d, 11, 14, 20, 19, (45, 28, 18)); R(d, 12, 20, 19, 20, (45, 28, 18)); R(d, 14, 15, 17, 15, (120, 60, 50))  # beard + mouth
    return im

def miranda():  # dancer: long black hair, purple and gold silk gown
    im, d = canvas(); shadow(d); pur, gold = (120, 50, 170), (230, 185, 70)
    R(d, 10, 20, 21, 27, pur); d.polygon([(10, 27), (21, 27), (25, 45), (6, 45)], fill=pur)  # gown
    for x, y in [(9, 34), (11, 39), (8, 42), (22, 36), (20, 41), (23, 43), (15, 30), (16, 37)]: P(d, [(x, y)], gold)
    R(d, 10, 27, 21, 27, gold); R(d, 6, 45, 25, 45, gold)
    R(d, 7, 20, 9, 30, SK_T); R(d, 22, 20, 24, 30, SK_T); P(d, [(7, 27), (8, 27), (23, 27), (24, 27)], gold)  # arms + bangles
    R(d, 13, 18, 18, 19, SK_T); head(d, SK_T, 5)
    R(d, 10, 3, 21, 7, BLK); R(d, 9, 5, 11, 30, BLK); R(d, 20, 5, 22, 30, BLK); P(d, [(10, 31), (21, 31), (21, 32)], BLK)
    P(d, [(17, 14), (16, 14)], (190, 60, 90))  # lips
    P(d, [(10, 9), (21, 9)], gold)  # earrings
    return im

def alex():  # sailor: black bandana, stubble, dark coat, rope coil and a hook
    im, d = canvas(); shadow(d); coat, rope = (55, 45, 40), (190, 160, 100)
    legs(d, (40, 40, 50), 36, 44, (50, 30, 20))
    R(d, 9, 19, 22, 37, coat); R(d, 15, 20, 16, 36, (35, 28, 25)); arms(d, coat, SK_M, 19, 31)
    d.ellipse([16, 23, 25, 32], outline=rope); d.ellipse([17, 24, 24, 31], outline=(150, 120, 70))  # rope coil
    R(d, 6, 33, 7, 36, (170, 170, 180)); P(d, [(8, 36), (9, 35)], (170, 170, 180))  # hook
    R(d, 13, 18, 18, 19, SK_M); head(d, SK_M, 5)
    R(d, 10, 4, 21, 8, BLK); P(d, [(13, 5), (17, 6), (19, 4)], (230, 230, 230)); R(d, 21, 7, 23, 9, BLK)  # bandana + knot
    P(d, [(12, 15), (13, 16), (15, 16), (18, 16), (19, 15), (16, 17), (14, 17)], (110, 80, 60))  # stubble
    return im

def sean():  # raver streamer: headphones, blue shades, glowing hoodie, LED sneakers
    im, d = canvas(); shadow(d); hood = (24, 22, 34)
    R(d, 12, 33, 15, 40, (30, 30, 36)); R(d, 17, 33, 20, 40, (30, 30, 36))  # shorts
    R(d, 12, 41, 14, 43, SK_L); R(d, 18, 41, 20, 43, SK_L)
    R(d, 11, 44, 15, 46, (40, 255, 230)); R(d, 17, 44, 21, 46, (40, 255, 230)); P(d, [(11, 46), (21, 46)], (255, 80, 220))  # LED sneakers
    R(d, 9, 19, 22, 33, hood); arms(d, hood, SK_L, 19, 31)
    P(d, [(13, 23), (14, 22), (15, 23), (16, 22), (17, 23), (18, 22), (15, 26), (16, 27), (13, 28), (18, 28), (14, 30), (17, 30)], (190, 80, 255))
    P(d, [(15, 24), (16, 24), (15, 25), (12, 31), (19, 31)], (60, 230, 255))
    R(d, 13, 18, 18, 19, SK_L); head(d, SK_L, 5)
    R(d, 11, 3, 20, 7, (110, 70, 40)); P(d, [(12, 2), (15, 2), (18, 2)], (110, 70, 40))
    R(d, 10, 2, 21, 3, BLK); R(d, 8, 8, 10, 13, (40, 40, 50)); R(d, 21, 8, 23, 13, (40, 40, 50)); P(d, [(9, 10), (22, 10)], (60, 230, 255))  # headphones
    R(d, 11, 11, 20, 12, (20, 20, 30)); R(d, 12, 11, 14, 12, (50, 120, 255)); R(d, 17, 11, 19, 12, (50, 120, 255))  # shades
    P(d, [(14, 15), (15, 16), (16, 16), (17, 15)], (150, 80, 70))  # grin
    return im

def alec():  # dance-off king: teal silk toga, red fringed cloak, gold sandals
    im, d = canvas(); shadow(d); teal, red, gold = (30, 170, 170), (190, 30, 40), (235, 190, 70)
    R(d, 7, 19, 24, 40, red); P(d, [(x, 41) for x in range(7, 25, 2)], red)  # cloak behind + fringe
    R(d, 10, 20, 21, 40, teal); d.polygon([(10, 20), (14, 20), (21, 34), (21, 38)], fill=(20, 130, 135))  # toga + drape
    P(d, [(x, 20) for x in range(10, 22, 2)], gold)
    R(d, 12, 41, 14, 43, SK_M); R(d, 17, 41, 19, 43, SK_M)
    R(d, 11, 44, 15, 45, gold); R(d, 17, 44, 21, 45, gold); P(d, [(13, 42), (18, 42)], gold)  # sandals
    R(d, 6, 19, 8, 30, red); R(d, 23, 19, 25, 30, red); R(d, 6, 31, 8, 32, SK_M); R(d, 23, 31, 25, 32, SK_M)
    R(d, 13, 18, 18, 19, SK_M); head(d, SK_M, 5)
    R(d, 11, 3, 20, 7, (150, 110, 60)); R(d, 10, 5, 11, 9, (150, 110, 60)); R(d, 20, 5, 21, 8, (150, 110, 60))
    P(d, [(14, 15), (15, 16), (16, 16), (17, 15)], (140, 70, 60))
    return im

def lydia():  # village elder: gray bun, mauve cardigan, cream floral apron
    im, d = canvas(); shadow(d); card, apron = (170, 110, 140), (240, 230, 205)
    R(d, 10, 38, 21, 44, (70, 60, 70)); R(d, 11, 45, 14, 46, (50, 35, 30)); R(d, 17, 45, 20, 46, (50, 35, 30))  # skirt + shoes
    R(d, 9, 22, 22, 38, card); arms(d, card, SK_L, 22, 33)
    R(d, 11, 25, 20, 41, apron); R(d, 12, 22, 19, 25, apron)
    P(d, [(12, 28), (17, 27), (14, 32), (19, 33), (12, 37), (16, 39), (18, 30)], (220, 110, 140))
    P(d, [(13, 28), (18, 28), (15, 32), (13, 37), (17, 39)], (110, 160, 90))
    R(d, 13, 21, 18, 22, SK_L); head(d, SK_L, 8)
    R(d, 11, 7, 20, 10, (200, 200, 205)); R(d, 10, 8, 11, 14, (200, 200, 205)); R(d, 20, 8, 21, 14, (200, 200, 205))
    R(d, 13, 4, 18, 7, (185, 185, 192))  # bun
    P(d, [(12, 14), (15, 14), (16, 14), (19, 14), (13, 15), (18, 15)], (120, 110, 100))  # glasses
    P(d, [(14, 19), (15, 19), (16, 19), (17, 19)], (170, 100, 100))  # smile
    return im

SPRITES = {'robert': robert, 'ramirez': ramirez, 'rob': rob, 'joseph': joseph, 'miranda': miranda,
           'alex': alex, 'sean': sean, 'alec': alec, 'lydia': lydia}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SPRITES.items(): fn().save(os.path.join(OUT, name + '.png'))
    print('wrote', len(SPRITES), 'sprites to', os.path.normpath(OUT))
