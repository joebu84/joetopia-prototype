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

# ---- road / travel encounters (art: joetopia-art-src/encounters/enc_*.jpg) ----
BRONZE, BRZ_D, BRZ_L = (150, 110, 50), (95, 68, 30), (200, 160, 85)
def enc_guard():  # bronze scale armour, crested helmet with glowing blue visor, round shield, electrified spear
    im, d = canvas(); shadow(d); red = (140, 30, 35)
    R(d, 12, 37, 15, 43, SK_M); R(d, 17, 37, 20, 43, SK_M); R(d, 12, 38, 15, 43, BRZ_D); R(d, 17, 38, 20, 43, BRZ_D)  # greaves
    R(d, 11, 44, 15, 45, (90, 60, 30)); R(d, 17, 44, 21, 45, (90, 60, 30))
    R(d, 10, 30, 21, 37, red); P(d, [(x, 37) for x in range(10, 22, 2)], BRZ_L)  # red skirt + fringe
    R(d, 13, 30, 18, 37, BRZ_D)  # front apron
    R(d, 9, 18, 22, 30, BRONZE)  # scale cuirass
    P(d, [(x, y) for y in range(19, 30, 2) for x in range(10 + (y % 4 == 1), 22, 2)], BRZ_D)
    R(d, 9, 28, 22, 29, (110, 30, 30)); P(d, [(15, 28), (16, 28)], BRZ_L)  # belt + boss
    R(d, 7, 18, 9, 21, BRONZE); R(d, 22, 18, 24, 21, BRONZE)  # pauldrons
    R(d, 7, 22, 9, 30, SK_M); R(d, 7, 25, 9, 29, BRZ_D)  # left arm + bracer
    d.ellipse([20, 21, 29, 33], fill=BRONZE, outline=BRZ_D); P(d, [(24, 27), (25, 27), (24, 26)], BRZ_L)  # round shield
    R(d, 4, 10, 4, 44, (70, 70, 80)); P(d, [(3, 9), (4, 8), (5, 9)], (200, 200, 220))  # spear
    P(d, [(3, 14), (5, 18), (3, 22), (5, 26), (3, 31), (5, 35), (4, 12), (4, 40)], (90, 200, 255))  # crackling lightning
    R(d, 13, 16, 18, 18, SK_M)
    R(d, 10, 5, 21, 16, BRONZE); R(d, 11, 4, 20, 5, BRZ_L)  # helmet
    R(d, 15, 0, 16, 4, (180, 140, 60)); P(d, [(14, 1), (17, 1), (13, 2), (18, 2)], (180, 140, 60))  # crest
    R(d, 11, 9, 20, 13, (20, 40, 80)); R(d, 12, 10, 19, 12, (60, 170, 255)); P(d, [(13, 10), (14, 10)], (200, 240, 255))  # blue visor
    P(d, [(15, 13), (16, 13), (15, 14), (16, 14)], (20, 40, 80))
    return im

def enc_preacher():  # bearded street preacher: red robe, blue mantle, ring-light staff, phone showing LIVE
    im, d = canvas(); shadow(d); red, blue, ring = (170, 35, 40), (40, 70, 170), (255, 220, 90)
    R(d, 9, 19, 22, 44, red); R(d, 8, 32, 23, 44, red)  # red robe
    d.polygon([(9, 19), (14, 19), (22, 40), (22, 44), (16, 44), (9, 28)], fill=blue)  # blue mantle across
    P(d, [(x, x + 6) for x in range(10, 21)], (70, 110, 220))
    R(d, 11, 45, 14, 46, (70, 45, 25)); R(d, 17, 45, 20, 46, (70, 45, 25))
    R(d, 7, 20, 9, 30, red); R(d, 22, 20, 24, 30, blue); R(d, 7, 31, 9, 32, SK_M); R(d, 22, 31, 24, 32, SK_M)
    R(d, 4, 13, 7, 18, SK_M); R(d, 5, 19, 7, 21, red)  # raised hand
    R(d, 25, 20, 25, 45, (60, 50, 40)); d.ellipse([22, 13, 29, 20], outline=ring); P(d, [(25, 16), (26, 16)], (255, 250, 210))  # ring-light staff
    R(d, 18, 27, 22, 32, (25, 25, 35)); R(d, 19, 28, 21, 29, (255, 50, 60)); P(d, [(19, 30), (20, 31), (21, 30)], (120, 200, 255))  # phone: LIVE
    R(d, 13, 18, 18, 19, SK_M); head(d, SK_M, 5)
    R(d, 10, 2, 21, 6, (35, 22, 15)); P(d, [(10, 1), (13, 1), (16, 1), (19, 1), (21, 2)], (35, 22, 15)); R(d, 10, 5, 11, 10, (35, 22, 15)); R(d, 20, 5, 21, 10, (35, 22, 15))  # curly hair
    R(d, 11, 13, 20, 19, (40, 28, 20)); R(d, 12, 20, 19, 21, (40, 28, 20)); R(d, 14, 15, 17, 16, (120, 50, 50))  # beard, mouth open
    return im

def enc_egirl():  # stream e-girl: cat ears, long purple-black hair, gold-and-black outfit, ring-light phone
    im, d = canvas(); shadow(d); blk, gold, pur, hair = (25, 20, 30), (230, 185, 70), (170, 80, 230), (60, 25, 85)
    R(d, 12, 37, 14, 43, SK_L); R(d, 17, 37, 19, 43, SK_L); P(d, [(12, y) for y in range(38, 44, 2)] + [(19, y) for y in range(38, 44, 2)], blk)  # fishnets
    R(d, 11, 44, 14, 46, blk); R(d, 17, 44, 20, 46, blk)
    d.polygon([(10, 30), (21, 30), (23, 37), (8, 37)], fill=blk); P(d, [(x, 36) for x in range(9, 23, 2)] + [(x, 31) for x in range(11, 21, 2)], gold)  # skirt
    R(d, 11, 27, 20, 29, SK_L)  # midriff
    R(d, 10, 19, 21, 26, blk); P(d, [(12, 21), (14, 23), (17, 21), (19, 23), (15, 25), (16, 25), (15, 20), (16, 20)], gold); P(d, [(15, 22)], pur)  # top + chains
    d.polygon([(7, 20), (10, 20), (8, 38), (5, 36)], fill=(140, 90, 190)); d.polygon([(21, 20), (24, 20), (27, 36), (23, 38)], fill=(140, 90, 190))  # sheer purple shawl
    R(d, 22, 20, 23, 29, SK_L); R(d, 8, 20, 9, 26, SK_L); P(d, [(22, 25), (23, 25)], gold)
    R(d, 5, 18, 6, 34, (30, 25, 25)); d.ellipse([0, 8, 11, 19], outline=(230, 120, 255)); d.ellipse([1, 9, 10, 18], outline=(255, 190, 255))  # ring-light
    R(d, 4, 11, 7, 16, (40, 35, 30)); P(d, [(5, 12), (6, 12)], gold)  # phone
    R(d, 13, 18, 18, 19, SK_L); head(d, SK_L, 5, (120, 40, 160))
    R(d, 10, 3, 21, 7, hair); R(d, 9, 5, 11, 26, hair); R(d, 20, 5, 22, 26, hair); P(d, [(9, 27), (22, 27), (21, 28)], hair)
    P(d, [(11, 4), (14, 3), (18, 4), (10, 15), (21, 18)], pur)  # purple sheen
    d.polygon([(10, 4), (11, 0), (14, 3)], fill=blk); d.polygon([(17, 3), (20, 0), (21, 4)], fill=blk)  # cat ears
    P(d, [(11, 2), (20, 2)], (230, 140, 200))
    R(d, 11, 4, 20, 4, gold); P(d, [(15, 3), (16, 3)], gold)  # circlet
    P(d, [(15, 15), (16, 15)], (200, 70, 110)); P(d, [(10, 11), (21, 11)], gold)
    return im

def enc_trader():  # bearded trader in a white-and-gold toga, leading a cyber goat pulling a hover cart
    im, d = canvas(); shadow(d); white, gold, goat = (235, 228, 210), (220, 175, 60), (110, 110, 125)
    # hover cart behind-right with purple cloth bales and a glowing orb
    R(d, 18, 30, 31, 38, (110, 80, 40)); R(d, 19, 26, 30, 30, (120, 50, 130)); R(d, 20, 23, 29, 26, (150, 70, 160)); P(d, [(x, 32) for x in range(19, 31, 2)], gold)
    d.ellipse([26, 31, 30, 35], fill=(200, 120, 255)); P(d, [(27, 32)], (255, 230, 255))
    P(d, [(x, 40) for x in range(19, 31, 3)], (120, 160, 255)); P(d, [(x, 39) for x in range(20, 31, 3)], (70, 90, 255))  # hover glow
    # cyber goat at the front-right
    R(d, 24, 14, 30, 20, goat); R(d, 25, 21, 26, 25, goat); R(d, 29, 21, 30, 25, goat); R(d, 27, 9, 30, 13, goat)
    P(d, [(26, 8), (25, 7), (25, 9), (31, 8)], (200, 170, 90)); P(d, [(29, 10)], (80, 230, 255)); P(d, [(25, 16), (27, 16), (29, 16)], gold)  # horns, glowing eye, harness
    # the trader
    R(d, 10, 19, 19, 43, white); R(d, 9, 30, 20, 43, white); d.polygon([(10, 19), (13, 19), (19, 33), (19, 36)], fill=gold)  # toga + gold sash
    R(d, 8, 19, 10, 30, (35, 30, 30)); P(d, [(x, 42) for x in range(9, 21, 2)], gold)  # dark cloak edge, gold hem
    R(d, 11, 44, 13, 45, (150, 110, 60)); R(d, 16, 44, 18, 45, (150, 110, 60))
    R(d, 7, 31, 9, 32, SK_T); R(d, 20, 21, 22, 29, white); R(d, 20, 30, 22, 31, SK_T); P(d, [(21, 28)], gold)
    R(d, 12, 18, 17, 19, SK_T); P(d, [(12, 18), (14, 19), (16, 18)], gold)  # gold collar
    R(d, 10, 7, 19, 17, SK_T); R(d, 11, 6, 18, 18, SK_T); P(d, [(12, 11), (13, 11), (16, 11), (17, 11)], (20, 20, 30))
    R(d, 10, 3, 19, 7, (25, 18, 15)); P(d, [(10, 2), (13, 2), (16, 2), (19, 3)], (25, 18, 15)); R(d, 9, 5, 10, 10, (25, 18, 15))
    R(d, 10, 14, 19, 18, (40, 30, 25)); R(d, 13, 15, 16, 15, (110, 60, 50))  # beard
    return im

def _goblin(d, ox, oy, extra=None):  # one small blue toothy goblin in rags, ~11x22
    blue, dk, rag = (50, 110, 220), (25, 60, 150), (90, 70, 45)
    R(d, ox + 2, oy + 9, ox + 9, oy + 18, rag); P(d, [(ox + 2, oy + 19), (ox + 5, oy + 19), (ox + 8, oy + 19)], rag)  # ragged tunic
    R(d, ox + 3, oy + 19, ox + 4, oy + 22, blue); R(d, ox + 7, oy + 19, ox + 8, oy + 22, blue)  # legs
    R(d, ox, oy + 10, ox + 1, oy + 16, blue); R(d, ox + 10, oy + 10, ox + 11, oy + 16, blue)  # arms
    R(d, ox, oy, ox + 11, oy + 8, blue); P(d, [(ox, oy), (ox + 11, oy)], (0, 0, 0, 0)); P(d, [(ox + 1, oy + 1), (ox + 5, oy), (ox + 9, oy + 2)], dk)
    P(d, [(ox + 3, oy + 2), (ox + 8, oy + 2)], (255, 255, 230)); P(d, [(ox + 3, oy + 3), (ox + 8, oy + 3)], (10, 10, 20))  # bulging eyes
    R(d, ox + 1, oy + 5, ox + 10, oy + 7, (120, 20, 40)); P(d, [(x, oy + 5) for x in range(ox + 1, ox + 11, 2)] + [(x, oy + 7) for x in range(ox + 2, ox + 11, 2)], (250, 245, 225))  # toothy grin
    if extra == 'shades': R(d, ox + 1, oy + 2, ox + 10, oy + 3, (15, 15, 20)); P(d, [(ox + 2, oy + 2), (ox + 7, oy + 2)], (120, 120, 140))
    if extra == 'knife': R(d, ox + 11, oy + 12, ox + 12, oy + 16, (200, 200, 210)); P(d, [(ox + 11, oy + 17)], (90, 50, 30))
    if extra == 'phone': R(d, ox - 1, oy + 10, ox + 1, oy + 13, (25, 25, 35)); P(d, [(ox, oy + 11)], (200, 90, 255))
def enc_goblins():  # three blue toothy goblins: sunglasses, knife, phone - with a mushroom behind
    im, d = canvas()
    d.ellipse([3, 46, 29, 47], fill=(0, 0, 0, 90))
    R(d, 14, 4, 17, 16, (210, 200, 170)); d.ellipse([7, 0, 24, 8], fill=(210, 40, 50)); P(d, [(10, 3), (15, 2), (20, 4), (13, 5)], (255, 240, 240))  # red mushroom
    _goblin(d, 10, 12, 'knife')
    _goblin(d, 0, 24, 'shades')
    _goblin(d, 20, 24, 'phone')
    return im

def enc_fans():  # a crowd of toga fans holding up glowing phones
    im, d = canvas(); d.ellipse([1, 44, 30, 47], fill=(0, 0, 0, 90))
    def fan(ox, oy, toga, skin, hair, phone_side):
        R(d, ox + 1, oy + 8, ox + 8, oy + 22, toga); P(d, [(ox + 1 + i, oy + 8 + i) for i in range(7)], (230, 190, 80))  # toga + gold edge
        R(d, ox + 2, oy, ox + 7, oy + 7, skin); R(d, ox + 2, oy - 1, ox + 7, oy + 1, hair); P(d, [(ox + 3, oy + 3), (ox + 6, oy + 3)], (20, 20, 30))
        P(d, [(ox + 4, oy + 5), (ox + 5, oy + 5)], (120, 50, 50))  # open mouth
        px = ox - 2 if phone_side < 0 else ox + 9
        R(d, px + (1 if phone_side < 0 else 0), oy - 5, px + (1 if phone_side < 0 else 0), oy + 8, skin)  # raised arm
        R(d, px, oy - 9, px + 2, oy - 5, (25, 25, 35)); P(d, [(px + 1, oy - 8), (px + 1, oy - 7)], (90, 220, 255))  # phone
    fan(1, 20, (220, 210, 190), SK_L, (200, 200, 200), -1)   # grey-haired fan, left
    fan(22, 21, (215, 205, 185), SK_M, (30, 25, 20), 1)      # right
    fan(11, 14, (110, 50, 150), SK_M, (35, 25, 20), 1)       # purple-toga fan in the middle, holding a phone up
    P(d, [(12, 21), (13, 22), (14, 21), (15, 22), (16, 21)], (30, 25, 20))  # his beard
    fan(5, 27, (235, 225, 200), SK_T, (25, 20, 18), 1)       # front row
    R(d, 6, 27, 13, 28, (230, 190, 80))  # gold headband
    return im

SPRITES = {'robert': robert, 'ramirez': ramirez, 'rob': rob, 'joseph': joseph, 'miranda': miranda,
           'alex': alex, 'sean': sean, 'alec': alec, 'lydia': lydia,
           'enc_guard': enc_guard, 'enc_preacher': enc_preacher, 'enc_egirl': enc_egirl,
           'enc_trader': enc_trader, 'enc_goblins': enc_goblins, 'enc_fans': enc_fans}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SPRITES.items(): fn().save(os.path.join(OUT, name + '.png'))
    print('wrote', len(SPRITES), 'sprites to', os.path.normpath(OUT))
