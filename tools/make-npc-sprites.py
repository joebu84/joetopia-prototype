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

# ---- Babylon street encounters (art: joetopia-art-src/street/<id>.jpg -> street_<id>) ----
GOLD, GOLD_D, PURP, NEONP = (225, 180, 70), (160, 120, 40), (150, 60, 200), (220, 90, 255)
def _robed(d, robe, skin, top=19, bot=44, sandals=(110, 75, 40), sash=None, hem=None):
    R(d, 10, top, 21, bot - 1, robe); R(d, 9, top + 12, 22, bot - 1, robe)  # toga/robe
    if sash: d.polygon([(10, top), (13, top), (21, top + 14), (21, top + 17)], fill=sash)
    if hem: P(d, [(x, bot - 2) for x in range(9, 23, 2)], hem)
    R(d, 11, bot, 14, bot + 1, sandals); R(d, 17, bot, 20, bot + 1, sandals)
    R(d, 13, top - 1, 18, top, skin)
def _face(d, skin, top=5, hair=None, beard=None, mouth=None, eyes=(20, 20, 30)):
    head(d, skin, top, eyes)
    if hair: R(d, 10, top - 2, 21, top + 2, hair); R(d, 10, top, 11, top + 6, hair); R(d, 20, top, 21, top + 6, hair)
    if beard: R(d, 11, top + 9, 20, top + 14, beard); R(d, 12, top + 15, 19, top + 16, beard)
    if mouth: R(d, 14, top + 10, 17, top + 11, mouth)

def street_punks():  # two thugs in red togas with gold chains: one with a glowing purple baton, one swinging a chain
    im, d = canvas(); d.ellipse([1, 44, 30, 47], fill=(0, 0, 0, 90)); red, redd = (165, 30, 35), (110, 20, 25)
    def thug(ox, skin, hair, headband):
        R(d, ox + 1, 20, ox + 12, 41, red); d.polygon([(ox + 1, 20), (ox + 4, 20), (ox + 12, 32), (ox + 12, 35)], fill=redd)
        P(d, [(ox + 3, 22), (ox + 5, 24), (ox + 7, 25), (ox + 9, 24), (ox + 11, 22)], GOLD)  # gold chain
        R(d, ox + 2, 42, ox + 5, 44, (60, 40, 25)); R(d, ox + 8, 42, ox + 11, 44, (60, 40, 25))
        R(d, ox + 2, 8, ox + 11, 18, skin); P(d, [(ox + 4, 12), (ox + 9, 12)], (20, 15, 15)); R(d, ox + 5, 15, ox + 8, 15, (90, 30, 30))
        R(d, ox + 2, 6, ox + 11, 8, hair)
        if headband: R(d, ox + 2, 8, ox + 11, 9, GOLD)
        R(d, ox + 3, 16, ox + 10, 19, hair if headband else skin)  # beard / jaw
    thug(17, SK_M, (30, 22, 18), False)
    thug(2, SK_D, (20, 15, 12), True)
    R(d, 0, 26, 2, 33, SK_D); R(d, 0, 30, 3, 40, NEONP); P(d, [(1, 31), (1, 34), (1, 37)], (255, 210, 255))  # glowing purple baton
    P(d, [(29, 26), (30, 28), (29, 30), (30, 32), (29, 34), (30, 36)], (170, 170, 180)); R(d, 28, 24, 30, 25, SK_M)  # chain
    return im

def street_drunk():  # huge bearded drunk in a wine-stained toga, clay jug raised
    im, d = canvas(); shadow(d); toga, wine = (150, 95, 70), (110, 20, 40)
    R(d, 8, 18, 23, 44, toga); R(d, 7, 28, 24, 44, toga)
    P(d, [(10, 22), (11, 23), (19, 27), (18, 28), (12, 34), (13, 35), (20, 38), (9, 40), (16, 31)], wine)  # wine stains
    d.polygon([(8, 18), (12, 18), (23, 32), (23, 36)], fill=(120, 40, 45))
    R(d, 9, 45, 13, 46, (80, 55, 30)); R(d, 18, 45, 22, 46, (80, 55, 30))
    R(d, 4, 19, 7, 30, SK_M); R(d, 24, 12, 27, 22, SK_M)  # arms, right raised
    d.ellipse([23, 4, 30, 13], fill=(170, 100, 55)); R(d, 25, 2, 28, 4, (140, 80, 45))  # jug
    R(d, 12, 16, 19, 18, SK_M); head(d, SK_M, 4); R(d, 10, 1, 21, 5, (30, 22, 18)); R(d, 9, 3, 10, 12, (30, 22, 18)); R(d, 21, 3, 22, 12, (30, 22, 18))
    R(d, 10, 12, 21, 20, (35, 25, 20)); R(d, 13, 13, 18, 15, (130, 40, 40))  # big beard, shouting
    P(d, [(12, 9), (19, 9)], (190, 60, 60))  # red eyes
    return im

def street_party_girls():  # three party girls in simple long gowns (purple, black, pink) with gold headpieces
    im, d = canvas(); d.ellipse([1, 44, 30, 47], fill=(0, 0, 0, 90))
    def girl(ox, oy, gown, skin, hair):
        d.polygon([(ox + 2, oy + 9), (ox + 7, oy + 9), (ox + 9, oy + 26), (ox, oy + 26)], fill=gown)  # simple gown
        R(d, ox + 2, oy + 9, ox + 7, oy + 12, gown); P(d, [(ox + 2, oy + 13), (ox + 7, oy + 13)], GOLD)  # gold armlets
        R(d, ox + 2, oy + 1, ox + 7, oy + 8, skin); P(d, [(ox + 3, oy + 4), (ox + 6, oy + 4)], (20, 15, 20)); P(d, [(ox + 4, oy + 6), (ox + 5, oy + 6)], (200, 70, 110))
        R(d, ox + 1, oy, ox + 8, oy + 1, hair); R(d, ox + 1, oy + 1, ox + 1, oy + 10, hair); R(d, ox + 8, oy + 1, ox + 8, oy + 10, hair)
        R(d, ox + 2, oy, ox + 7, oy, GOLD); P(d, [(ox + 4, oy - 1), (ox + 5, oy - 1)], GOLD)  # gold headpiece
    girl(1, 18, (25, 22, 30), SK_D, (15, 12, 15))       # black gown, left
    girl(22, 18, (230, 130, 170), SK_L, (190, 70, 40))   # pink gown, red hair, right
    girl(11, 15, (150, 80, 200), SK_T, (25, 18, 15))     # purple gown, middle
    return im

def street_beggar():  # old beggar in rags, sitting, holding out a bowl
    im, d = canvas(); d.ellipse([4, 43, 28, 47], fill=(0, 0, 0, 90)); rag, ragd = (120, 105, 85), (85, 72, 58)
    d.polygon([(8, 20), (23, 20), (27, 44), (4, 44)], fill=rag)  # hunched, sitting in rags
    P(d, [(9, 26), (12, 31), (20, 28), (23, 36), (7, 40), (15, 38), (18, 42), (11, 35)], ragd)
    R(d, 21, 30, 26, 33, SK_T); d.ellipse([24, 30, 31, 35], fill=(70, 60, 55)); P(d, [(26, 31), (28, 31)], (90, 200, 255))  # outstretched arm + bowl
    R(d, 12, 19, 19, 21, SK_T); head(d, SK_T, 8); R(d, 10, 6, 21, 9, (70, 60, 55)); R(d, 9, 8, 10, 16, (70, 60, 55)); R(d, 21, 8, 22, 16, (70, 60, 55))
    R(d, 11, 16, 20, 24, (150, 145, 140)); R(d, 13, 16, 18, 17, SK_T)  # grey beard
    return im

def street_geneticist():  # wild-eyed, wild-haired bearded geneticist with a green glowing syringe
    im, d = canvas(); shadow(d); robe, trim = (150, 120, 85), (40, 80, 150)
    _robed(d, robe, SK_M, 19, 44, (90, 60, 35), hem=trim)
    R(d, 13, 22, 18, 30, trim); R(d, 14, 25, 17, 28, GOLD)  # medallion on a tabard
    R(d, 7, 20, 9, 31, robe); R(d, 22, 12, 24, 22, SK_M)  # raised right arm
    R(d, 23, 2, 25, 11, (60, 255, 140)); P(d, [(24, 0), (24, 1)], (220, 255, 230)); R(d, 22, 10, 26, 11, (200, 200, 210))  # syringe
    head(d, SK_M, 5, (255, 255, 255)); P(d, [(13, 12), (18, 12)], (20, 20, 30))  # wild white eyes
    hair = (90, 80, 75); R(d, 8, 2, 23, 5, hair); R(d, 7, 4, 10, 18, hair); R(d, 21, 4, 24, 18, hair); P(d, [(7, 1), (11, 0), (16, 1), (20, 0), (24, 2), (6, 8)], hair)
    R(d, 11, 15, 20, 24, (110, 100, 95)); R(d, 13, 15, 18, 16, (240, 240, 230))  # beard, toothy grin
    return im

def street_preacher():  # busking street preacher: cream toga, purple sash, gold tip bowl, hand raised
    im, d = canvas(); shadow(d); cream = (220, 210, 185)
    _robed(d, cream, SK_M, 19, 44, sash=(110, 50, 140), hem=GOLD)
    R(d, 6, 10, 8, 20, SK_M); R(d, 5, 8, 9, 10, SK_M)  # raised hand
    R(d, 22, 20, 24, 27, cream); d.ellipse([20, 26, 30, 32], fill=GOLD, outline=GOLD_D); P(d, [(25, 28)], (230, 80, 200))  # tip bowl
    head(d, SK_M, 5); R(d, 10, 3, 21, 6, (40, 30, 22)); R(d, 10, 5, 11, 10, (40, 30, 22)); R(d, 20, 5, 21, 10, (40, 30, 22))
    R(d, 11, 14, 20, 18, (70, 60, 50)); R(d, 14, 15, 17, 15, (130, 60, 60))  # short beard, singing
    return im

def street_drone():  # ornate Babylonian delivery drone (bronze, four rotors, blue thrusters) carrying a crate
    im, d = canvas(); d.ellipse([6, 44, 25, 47], fill=(0, 0, 0, 70))
    for x in (1, 22): R(d, x, 3, x + 8, 4, (60, 60, 70)); R(d, x + 3, 5, x + 5, 7, BRZ_D)  # rotors
    R(d, 4, 7, 27, 9, BRZ_D)  # arms
    R(d, 11, 2, 20, 16, BRONZE); R(d, 13, 0, 18, 2, BRZ_L); P(d, [(x, y) for y in range(4, 15, 3) for x in range(12, 20, 2)], BRZ_D)  # ornate body
    P(d, [(15, 7), (16, 7)], (90, 200, 255))  # cracked lens
    for x in (11, 15, 19): R(d, x, 17, x + 1, 19, (80, 180, 255)); P(d, [(x, 20)], (190, 240, 255))  # blue thrusters
    P(d, [(13, y) for y in range(20, 27)] + [(18, y) for y in range(20, 27)], (100, 100, 110))  # cables
    R(d, 8, 27, 23, 39, (150, 105, 50)); R(d, 8, 27, 23, 28, BRZ_L); R(d, 8, 33, 23, 33, BRZ_D); P(d, [(14, 30), (15, 31), (16, 30), (17, 31)], (40, 160, 230))  # crate
    return im

def street_pickpocket():  # grinning kid in rags, mid-snatch with a pouch
    im, d = canvas(); d.ellipse([7, 44, 24, 47], fill=(0, 0, 0, 90)); rag = (130, 125, 105)
    R(d, 11, 22, 20, 36, rag); P(d, [(12, 25), (17, 28), (14, 33), (19, 24), (11, 34)], (95, 90, 75)); P(d, [(11, 37), (14, 37), (17, 37), (20, 37)], rag)
    R(d, 12, 37, 14, 43, SK_T); R(d, 17, 37, 19, 42, SK_T); R(d, 11, 44, 14, 45, SK_D); R(d, 18, 43, 21, 44, SK_D)  # bare feet, running
    R(d, 7, 23, 10, 30, SK_T); R(d, 21, 24, 27, 26, SK_T)  # arm reaching out
    d.ellipse([25, 23, 31, 31], fill=(150, 100, 55)); R(d, 26, 22, 29, 23, (110, 70, 40))  # snatched pouch
    head(d, SK_T, 9); R(d, 9, 6, 22, 10, (20, 15, 15)); P(d, [(9, 5), (12, 4), (15, 5), (18, 4), (21, 5), (8, 9), (22, 10)], (20, 15, 15))  # curly hair
    R(d, 13, 18, 18, 19, (250, 245, 235))  # grin
    return im

def street_megaphone():  # bearded conspiracy theorist in a white toga with a purple stripe, shouting into a neon megaphone
    im, d = canvas(); shadow(d); white = (225, 220, 205)
    _robed(d, white, SK_M, 19, 44, sash=(90, 40, 140))
    R(d, 4, 18, 8, 23, SK_M)  # other hand thrown out
    R(d, 21, 15, 24, 19, (40, 40, 50)); d.polygon([(23, 13), (31, 8), (31, 24), (23, 20)], fill=(210, 60, 200)); R(d, 29, 11, 31, 21, (255, 150, 250))  # neon megaphone
    head(d, SK_M, 5); R(d, 10, 3, 21, 6, (25, 20, 18)); R(d, 10, 5, 11, 10, (25, 20, 18))
    R(d, 11, 13, 21, 20, (30, 25, 20)); R(d, 14, 14, 18, 16, (140, 50, 50))  # beard, shouting
    return im

def street_tourist():  # lost tourist: brand-new white toga with price tags, map in one hand, phone in the other
    im, d = canvas(); shadow(d); white = (235, 230, 215)
    _robed(d, white, SK_L, 19, 44, (130, 90, 50))
    R(d, 18, 22, 20, 27, (240, 240, 240)); R(d, 18, 25, 20, 25, (220, 40, 40)); R(d, 13, 36, 15, 40, (240, 240, 240)); P(d, [(14, 37)], (220, 40, 40))  # price tags
    R(d, 1, 24, 9, 33, (220, 205, 160)); P(d, [(3, 26), (5, 28), (7, 27), (4, 31), (6, 30)], (120, 140, 90))  # map
    R(d, 22, 26, 25, 31, (25, 25, 35)); R(d, 23, 27, 24, 29, (90, 200, 255))  # phone
    head(d, SK_L, 5); R(d, 10, 2, 21, 6, (90, 60, 35)); P(d, [(11, 1), (15, 1), (19, 2)], (90, 60, 35)); R(d, 10, 5, 11, 9, (90, 60, 35))
    P(d, [(15, 15), (16, 15)], (150, 80, 70))  # worried mouth
    return im

def street_stranger():  # dark curly-haired woman in a simple white-and-gold gown
    im, d = canvas(); shadow(d); white, hair = (240, 235, 220), (20, 15, 20)
    d.polygon([(11, 19), (20, 19), (23, 44), (8, 44)], fill=white)  # long simple gown
    R(d, 11, 25, 20, 26, GOLD); P(d, [(x, 43) for x in range(9, 23, 2)], GOLD)  # gold belt + hem
    d.line([(17, 27), (20, 44)], fill=(215, 205, 185))  # fold
    R(d, 8, 20, 10, 30, SK_L); R(d, 21, 20, 23, 30, SK_L); P(d, [(8, 23), (23, 23)], GOLD)  # arms + armlets
    R(d, 13, 18, 18, 19, SK_L); P(d, [(13, 19), (15, 19), (16, 19), (18, 19)], GOLD)  # gold necklace
    head(d, SK_L, 5); P(d, [(15, 15), (16, 15)], (150, 20, 40))  # dark red lips
    R(d, 9, 2, 22, 6, hair); R(d, 8, 4, 11, 20, hair); R(d, 20, 4, 23, 20, hair)
    P(d, [(8, 2), (12, 1), (16, 1), (20, 1), (23, 3), (7, 9), (24, 12), (7, 16), (24, 19)], hair)  # curls
    P(d, [(10, 12), (21, 12)], GOLD)  # earrings
    return im

def street_noble():  # bearded noble in gilded armour with a gold headband, a glowing purple runed sword
    im, d = canvas(); shadow(d); cape = (110, 40, 120)
    R(d, 9, 30, 22, 38, (210, 200, 175)); R(d, 12, 39, 15, 43, GOLD_D); R(d, 17, 39, 20, 43, GOLD_D)  # skirt, greaves
    R(d, 11, 44, 15, 45, BRZ_D); R(d, 17, 44, 21, 45, BRZ_D)
    R(d, 9, 18, 22, 30, GOLD); P(d, [(x, y) for y in range(19, 30, 2) for x in range(10 + (y % 4 == 1), 22, 2)], GOLD_D)  # gilded scale armour
    d.polygon([(9, 18), (13, 18), (22, 30), (19, 30)], fill=cape)  # purple sash
    R(d, 6, 18, 9, 21, GOLD); R(d, 22, 18, 25, 21, GOLD); R(d, 6, 22, 8, 29, SK_T); R(d, 23, 22, 25, 29, SK_T)
    d.line([(7, 30), (1, 46)], fill=NEONP, width=2); d.line([(8, 30), (3, 46)], fill=(255, 200, 255)); P(d, [(4, 37), (3, 41), (5, 34)], (255, 255, 255))  # runed glowing sword
    R(d, 5, 29, 9, 30, GOLD)  # crossguard
    R(d, 13, 16, 18, 18, SK_T); head(d, SK_T, 4, (170, 20, 30))  # blood-red eyes
    R(d, 10, 1, 21, 5, (25, 18, 15)); P(d, [(10, 0), (13, 0), (17, 0), (21, 1), (9, 4), (22, 4)], (25, 18, 15))
    R(d, 10, 5, 21, 6, GOLD)  # gold headband
    R(d, 11, 13, 20, 19, (35, 25, 20)); R(d, 13, 14, 18, 15, (130, 40, 40))  # beard, snarling
    return im

def street_creep():  # the creep from the club: smirking, bearded, curly dark hair, worn dusty toga, gold chain
    im, d = canvas(); shadow(d); toga, dk = (125, 110, 90), (85, 74, 60)
    _robed(d, toga, SK_T, 19, 44, (70, 50, 30))
    d.polygon([(9, 19), (14, 19), (22, 36), (22, 40), (17, 40), (9, 26)], fill=dk)  # draped fold
    P(d, [(x, x + 4) for x in range(10, 21, 2)], (140, 125, 100)); P(d, [(12, 33), (18, 28), (11, 40), (20, 42)], (95, 80, 60))  # worn patches
    P(d, [(13, 20), (14, 21), (15, 21), (16, 21), (17, 20)], GOLD)  # chain
    R(d, 7, 20, 9, 32, toga); R(d, 22, 20, 24, 31, toga); R(d, 22, 32, 24, 33, SK_T); R(d, 7, 33, 9, 34, SK_T)
    P(d, [(23, 34)], (180, 255, 230))  # the little vial
    head(d, SK_T, 5); P(d, [(12, 11), (19, 11)], (30, 20, 20))
    hair = (25, 18, 15); R(d, 10, 2, 21, 6, hair); P(d, [(9, 3), (12, 1), (15, 2), (18, 1), (21, 3), (9, 8), (22, 8)], hair); R(d, 9, 5, 10, 11, hair); R(d, 21, 5, 22, 11, hair)
    R(d, 11, 13, 20, 19, (40, 30, 24)); P(d, [(15, 14), (16, 14), (17, 13)], (150, 80, 70))  # beard, crooked smirk
    return im

def street_temptress():  # the furious church lady: wild grey hair, dark knitted shawl over a brown dress, pointing
    im, d = canvas(); shadow(d); shawl, dress = (40, 36, 34), (95, 70, 45)
    d.polygon([(10, 22), (21, 22), (23, 44), (8, 44)], fill=dress); P(d, [(11, 30), (15, 34), (19, 31), (13, 39), (18, 41)], (120, 90, 55))
    R(d, 9, 19, 22, 31, shawl); P(d, [(x, y) for y in range(20, 31, 2) for x in range(10 + (y % 4 == 0), 22, 2)], (58, 52, 48))  # knit
    R(d, 11, 45, 14, 46, (50, 35, 25)); R(d, 17, 45, 20, 46, (50, 35, 25))
    R(d, 22, 20, 28, 22, shawl); R(d, 28, 20, 31, 21, SK_L); P(d, [(31, 19)], SK_L)  # arm out, finger pointing
    R(d, 7, 21, 9, 29, shawl); R(d, 7, 30, 9, 31, SK_L)
    skin = (205, 160, 125); head(d, skin, 5, (60, 70, 90)); R(d, 12, 8, 19, 8, (120, 80, 60))  # furrowed brow
    R(d, 13, 14, 18, 16, (110, 30, 30)); R(d, 14, 14, 17, 14, (250, 250, 245))  # shouting mouth
    grey = (190, 185, 180); R(d, 10, 2, 21, 6, grey); R(d, 8, 4, 10, 18, grey); R(d, 21, 4, 23, 18, grey)
    P(d, [(8, 2), (11, 1), (14, 0), (18, 1), (22, 2), (24, 6), (7, 8), (24, 13), (7, 15)], grey)  # wild wisps
    return im

# Undercroft sprites, drawn from the real art in joetopia-art-src/undercroft/ (pirate, rats, sailor, streetwalker, kraken).
def street_pirates():  # grinning long-haired pirate: black coat with gold trim, red sash, curved sword, tall boots
    im, d = canvas(); shadow(d); coat, gold, sash, hair = (28, 24, 30), (215, 170, 60), (170, 30, 35), (25, 18, 14)
    R(d, 12, 34, 15, 41, (40, 32, 30)); R(d, 17, 34, 20, 41, (40, 32, 30)); R(d, 11, 41, 15, 45, (55, 38, 25)); R(d, 17, 41, 21, 45, (55, 38, 25))  # boots
    d.polygon([(9, 19), (22, 19), (24, 42), (7, 42)], fill=coat); R(d, 13, 19, 18, 33, (70, 50, 40))  # long coat, open over a vest
    P(d, [(9, y) for y in range(20, 42, 2)] + [(22, y) for y in range(20, 42, 2)] + [(x, 42) for x in range(7, 25, 2)], gold)  # gold trim
    R(d, 11, 29, 20, 31, sash); R(d, 18, 31, 20, 37, sash)  # red sash, hanging tail
    R(d, 6, 20, 8, 30, coat); R(d, 23, 20, 25, 30, coat); R(d, 6, 31, 8, 32, SK_M); R(d, 23, 31, 25, 32, SK_M)
    d.line([(25, 32), (28, 38), (29, 44)], fill=(205, 210, 220), width=1); R(d, 24, 31, 26, 33, gold)  # curved sword, gold hilt
    _face(d, SK_M, 5, beard=(45, 32, 24)); R(d, 13, 15, 18, 15, (250, 245, 235))  # beard and a big white grin
    R(d, 10, 2, 21, 6, hair); R(d, 9, 4, 11, 22, hair); R(d, 20, 4, 22, 22, hair)  # long dark hair
    return im

def street_rats():  # swarm of huge scaly black sewer rats with glowing red eyes
    im, d = canvas(); fur, scale, tail, eye = (32, 32, 42), (70, 80, 105), (120, 90, 100), (255, 40, 40)
    for ox, oy, k in ((1, 34, 1), (15, 37, 1), (9, 24, 0), (18, 22, 1), (2, 14, 0)):
        d.ellipse([ox, oy, ox + 13, oy + 8], fill=fur); P(d, [(ox + 3 + j * 2, oy + 2 + j % 2) for j in range(5)], scale)  # scaly back
        hx = ox + 10 if k else ox - 3; d.ellipse([hx, oy, hx + 6, oy + 5], fill=fur)
        P(d, [(hx + 4 if k else hx + 1, oy + 1)], eye); P(d, [(hx + 4 if k else hx + 1, oy + 2)], (255, 140, 120))  # glowing red eye
        P(d, [(hx + 6 if k else hx, oy + 4)], (150, 110, 120))  # snout
        d.line([(ox if k else ox + 13, oy + 6), (ox - 4 if k else ox + 17, oy + 8)], fill=tail)
        P(d, [(ox + 2, oy + 8), (ox + 10, oy + 8)], (60, 55, 70))
    return im

def street_sailor():  # bearded angry drunk sailor in rope-wrapped brown robes, bottle in one hand, pointing with the other
    im, d = canvas(); robe, rope, hair = (105, 88, 62), (170, 140, 95), (45, 32, 24)
    _robed(d, robe, SK_M, sandals=(50, 38, 28), hem=(80, 66, 46))
    P(d, [(x, 27 + (x % 2)) for x in range(9, 23)] + [(x, 33 - (x % 2)) for x in range(10, 22)] + [(11 + i, 20 + i) for i in range(8)], rope)  # rope wraps
    R(d, 6, 20, 9, 29, robe); R(d, 5, 22, 6, 27, (95, 125, 70)); R(d, 5, 20, 6, 21, (60, 80, 45))  # bottle hand
    R(d, 22, 20, 26, 23, robe); R(d, 27, 21, 29, 22, SK_M); P(d, [(30, 21)], SK_M)  # arm pointing at you
    _face(d, SK_M, 5, hair=hair, beard=hair, mouth=(110, 30, 30)); P(d, [(13, 11), (17, 11)], hair)  # shouting, angry brows
    return im

def street_streetwalker():  # tearful woman in a wet red dress, long black hair (modest silhouette, fully clothed)
    im, d = canvas(); shadow(d); dress, dk, hair = (175, 30, 40), (125, 18, 28), (20, 16, 18)
    d.polygon([(11, 19), (20, 19), (22, 44), (9, 44)], fill=dress); P(d, [(12, y) for y in range(22, 44, 3)] + [(19, y) for y in range(23, 44, 3)], dk)  # long gown, wet sheen
    R(d, 9, 19, 10, 29, SK_L); R(d, 21, 19, 22, 29, SK_L)  # bare arms
    R(d, 11, 45, 14, 46, (90, 30, 30)); R(d, 17, 45, 20, 46, (90, 30, 30))
    head(d, SK_L, 5); P(d, [(13, 13), (18, 13), (13, 14)], (130, 190, 240)); P(d, [(15, 15), (16, 15)], (170, 80, 90))  # tears
    R(d, 10, 2, 21, 6, hair); R(d, 9, 4, 11, 22, hair); R(d, 20, 4, 22, 22, hair)  # long wet black hair
    P(d, [(13, 19), (15, 21), (17, 19)], (215, 170, 60))  # thin gold necklace
    return im

def street_kraken():  # THE KRAKEN: red tentacled body under a golden spiral shell, one huge amber eye, rising from the flood
    im, d = canvas(); body, dk, sucker, shell, shd = (175, 40, 50), (120, 25, 35), (240, 150, 150), (205, 160, 70), (140, 100, 40)
    R(d, 0, 41, 31, 47, (20, 40, 60)); P(d, [(x, 41 + (x % 3 == 0)) for x in range(0, 32)], (200, 80, 200))  # flooded tunnel, neon on the water
    d.ellipse([12, 1, 31, 22], fill=shell)
    for r in (8, 5, 2): d.arc([22 - r, 11 - r, 22 + r, 11 + r], 0, 300, fill=shd)  # golden spiral
    for x0, top, lean in ((1, 22, -1), (5, 28, 0), (25, 26, 1), (29, 20, 1), (9, 32, 0), (21, 32, 0)):
        for y in range(top, 42): x = x0 + (lean * (y - top) // 6 if lean else 0); R(d, x, y, x + 1, y, body)
        P(d, [(x0, y) for y in range(top + 1, 41, 3)], sucker)
    d.ellipse([5, 10, 24, 33], fill=body); P(d, [(x, 31) for x in range(7, 23, 2)], dk)
    d.ellipse([9, 15, 19, 25], fill=(255, 175, 40)); d.ellipse([11, 17, 17, 23], fill=(235, 120, 20)); R(d, 13, 17, 14, 23, BLK)  # huge amber eye
    return im


# ---- Scalegate encounters, drawn from joetopia-art-src/scalegate/ (duelist, angry_local, parade, bald_fight, fireworks).
SCALE_G, SCALE_B = (60, 120, 80), (40, 80, 55)
def _lizard(d, ox=0, oy=0, armor=(150, 115, 55)):  # a Draconian in bronze legion armour
    R(d, 12 + ox, 34 + oy, 15 + ox, 44 + oy, SCALE_B); R(d, 17 + ox, 34 + oy, 20 + ox, 44 + oy, SCALE_B)
    R(d, 10 + ox, 19 + oy, 21 + ox, 34 + oy, armor); P(d, [(x + ox, y + oy) for x in range(11, 21, 2) for y in range(21, 33, 3)], (110, 80, 35))
    R(d, 11 + ox, 6 + oy, 20 + ox, 18 + oy, SCALE_G); R(d, 18 + ox, 11 + oy, 23 + ox, 15 + oy, SCALE_G)  # long snout
    P(d, [(17 + ox, 9 + oy)], (255, 200, 40)); P(d, [(x + ox, 5 + oy) for x in (12, 14, 16, 18)], SCALE_B)  # yellow eye, crest
def _bald(d, ox, skin, top=5, w=10):  # big bald head with a shine
    R(d, ox + 1, top + 1, ox + w - 1, top + 11, skin); R(d, ox, top + 3, ox + w, top + 9, skin)
    P(d, [(ox + 3, top + 2), (ox + 4, top + 2)], (255, 245, 230)); R(d, ox + 3, top + 12, ox + w - 3, top + 13, skin)
BGOLD, TOGA_BLK = (220, 175, 60), (20, 18, 22)
def street_duel():  # duel challenger (duelist.jpg): bald man in a black bodysuit with gold patterning, gold visor glasses, fighting stance
    im, d = canvas(); shadow(d); suit = (22, 20, 26)
    R(d, 9, 33, 14, 43, suit); R(d, 18, 33, 23, 43, suit); R(d, 7, 44, 14, 45, (8, 8, 10)); R(d, 18, 44, 25, 45, (8, 8, 10))  # wide stance, black shoes
    P(d, [(10, y) for y in range(34, 43, 2)] + [(21, y) for y in range(34, 43, 2)], BGOLD)
    R(d, 10, 19, 21, 33, suit); P(d, [(12, 21), (13, 23), (15, 25), (18, 21), (17, 23), (16, 27), (12, 29), (19, 30), (15, 31)], BGOLD)  # gold patterning
    R(d, 6, 20, 9, 30, suit); R(d, 22, 20, 25, 30, suit); R(d, 5, 30, 8, 32, SK_M); R(d, 23, 30, 26, 32, SK_M)  # fists ready
    R(d, 13, 18, 18, 19, suit)  # high collar
    _bald(d, 11, SK_M); R(d, 11, 10, 21, 11, BGOLD); P(d, [(13, 10), (18, 10)], (255, 235, 140))  # gold visor glasses
    R(d, 14, 15, 17, 15, (110, 60, 50))
    return im
def street_angry_local():  # angry local (angry_local.jpg): huge bald man in a black-and-gold toga, round mirrored glasses, pointing
    im, d = canvas(); shadow(d)
    _robed(d, TOGA_BLK, SK_T, top=19, bot=44, sandals=(40, 30, 20), sash=BGOLD, hem=BGOLD)
    R(d, 8, 19, 23, 30, TOGA_BLK); R(d, 8, 19, 10, 26, SK_T)  # broad shoulders, bare arm
    d.line([(10, 19), (22, 33)], fill=BGOLD); d.line([(9, 21), (21, 35)], fill=BGOLD)  # gold-key trim on the toga
    R(d, 23, 18, 29, 21, SK_T); R(d, 29, 17, 31, 18, SK_T); P(d, [(31, 16)], SK_T)  # arm out, finger jabbing at you
    R(d, 6, 26, 8, 33, SK_T)
    _bald(d, 11, SK_T, 4); d.ellipse([12, 8, 15, 11], fill=(200, 210, 220)); d.ellipse([16, 8, 19, 11], fill=(200, 210, 220)); P(d, [(13, 9), (17, 9)], (255, 255, 255))  # round mirrored glasses
    R(d, 14, 13, 17, 14, (90, 30, 30))  # shouting
    return im
def street_parade():  # martial parade (parade.jpg): ranks of black-and-gold armoured soldiers, conical helmets, eagle shields
    im, d = canvas(); d.ellipse([0, 44, 31, 47], fill=(0, 0, 0, 90)); arm, gold, dk = (38, 34, 30), (190, 150, 60), (20, 18, 16)
    for ox, oy in ((20, 2), (10, 0), (0, -2)):  # back rank to front
        R(d, ox + 2, 21 + oy, ox + 9, 38 + oy, arm); P(d, [(ox + x, y + oy) for x in (3, 5, 7) for y in range(23, 37, 3)], gold)  # scale armour
        R(d, ox + 3, 39 + oy, ox + 4, 45 + oy, dk); R(d, ox + 7, 39 + oy, ox + 8, 45 + oy, dk); P(d, [(ox + 3, 44 + oy), (ox + 8, 44 + oy)], (230, 40, 40))  # greaves, red glints
        R(d, ox + 3, 13 + oy, ox + 8, 20 + oy, (60, 52, 40)); R(d, ox + 4, 16 + oy, ox + 7, 16 + oy, dk)  # face guard, eye slit
        d.polygon([(ox + 2, 13 + oy), (ox + 9, 13 + oy), (ox + 5, 6 + oy)], fill=gold)  # conical helmet
        R(d, ox + 6, 25 + oy, ox + 10, 34 + oy, (30, 26, 20)); R(d, ox + 6, 25 + oy, ox + 10, 25 + oy, gold); R(d, ox + 6, 34 + oy, ox + 10, 34 + oy, gold)
        P(d, [(ox + 8, 28 + oy), (ox + 7, 29 + oy), (ox + 9, 29 + oy), (ox + 8, 30 + oy), (ox + 8, 31 + oy)], gold)  # eagle on the shield
    return im
def street_fireworks():  # fireworks show (fireworks.jpg): red, gold and white bursts over black-glass towers with red lights
    im, d = canvas()
    for x0, x1, top in ((0, 6, 14), (25, 31, 18), (7, 10, 30), (21, 24, 28)):
        R(d, x0, top, x1, 44, (14, 14, 20)); P(d, [(x, y) for x in range(x0 + 1, x1, 2) for y in range(top + 2, 43, 4)], (60, 60, 80))  # black glass
    P(d, [(1, 30), (2, 30), (28, 34), (29, 34), (5, 40), (26, 40)], (230, 30, 40))  # red tower lights
    for cx, cy, c in ((10, 8, (255, 255, 240)), (21, 6, (240, 190, 70)), (15, 17, (235, 40, 50)), (25, 14, (230, 50, 60))):
        for dx, dy in ((0, -5), (4, -3), (5, 0), (4, 3), (0, 5), (-4, 3), (-5, 0), (-4, -3)): d.line([(cx, cy), (cx + dx, cy + dy)], fill=c)
        P(d, [(cx, cy)], (255, 255, 255)); d.line([(cx, cy + 6), (cx, cy + 12)], fill=tuple(v // 2 for v in c))  # trail
    R(d, 0, 45, 31, 47, (30, 25, 30)); P(d, [(x, 46) for x in range(1, 31, 3)], (180, 40, 50))  # wet street reflections
    return im
def street_bald_brawl():  # two bald men fighting (bald_fight.jpg): one in a black-and-gold toga, one in a grey-and-red toga
    im, d = canvas(); d.ellipse([0, 44, 31, 47], fill=(0, 0, 0, 90))
    for ox, skin, toga, trim in ((0, SK_M, TOGA_BLK, BGOLD), (16, (175, 170, 165), (110, 108, 112), (175, 30, 35))):
        R(d, ox + 2, 21, ox + 13, 38, toga); d.line([(ox + 3, 21), (ox + 12, 33)], fill=trim); P(d, [(x, 38) for x in range(ox + 2, ox + 14, 2)], trim)
        R(d, ox + 3, 39, ox + 5, 44, skin); R(d, ox + 10, 39, ox + 12, 44, skin)
        R(d, ox + 1, 20, ox + 14, 23, skin)  # bare shoulders
        _bald(d, ox + 3, skin, 6, 9); P(d, [(ox + 5, 11), (ox + 9, 11)], (20, 20, 25)); R(d, ox + 5, 9, ox + 10, 9, tuple(v - 50 for v in skin))  # scowl
    R(d, 13, 23, 15, 26, SK_M); R(d, 16, 23, 18, 26, (175, 170, 165))  # raised fists, face to face
    return im

# Lantern Row encounters, drawn from the user's art in joetopia-art-src/lantern/<id>.jpg.
PAINTS = [(220, 60, 50), (60, 120, 210), (245, 200, 60), (70, 170, 90), (230, 120, 40), (150, 80, 200)]
def street_starving_artist():  # starving_artist.jpg: gaunt bearded painter, wild dark hair, ragged paint-stained robe, red sash, brush + palette
    im, d = canvas(); shadow(d); robe, hair, skin = (190, 170, 135), (45, 32, 25), (195, 150, 115)
    _robed(d, robe, skin, sandals=(80, 55, 35), sash=None)
    R(d, 10, 31, 21, 32, (150, 40, 40))  # red cloth belt
    P(d, [(x, 43) for x in (9, 12, 16, 19, 22)], (0, 0, 0, 0)); P(d, [(x, 42) for x in (10, 14, 18, 21)], (150, 130, 100))  # ragged, torn hem
    for i, (x, y) in enumerate([(12, 22), (19, 25), (14, 28), (11, 36), (18, 38), (20, 34), (15, 40), (13, 33)]): P(d, [(x, y)], PAINTS[i % 6])  # paint stains
    d.line([(10, 19), (14, 30)], fill=(150, 130, 100)); d.line([(21, 19), (17, 30)], fill=(150, 130, 100))  # robe folds / patched layers
    _face(d, skin, hair=hair, beard=(60, 48, 40)); P(d, [(9, 2), (12, 1), (15, 2), (19, 1), (22, 3), (9, 9), (22, 10)], hair)  # wild hair
    P(d, [(12, 10), (19, 10)], (150, 105, 80)); P(d, [(13, 8), (18, 8)], (120, 85, 65))  # hollow cheeks, tired eyes
    R(d, 6, 20, 9, 28, robe); R(d, 6, 26, 9, 28, skin); d.line([(7, 26), (3, 17)], fill=(120, 85, 50)); P(d, [(3, 16), (2, 15)], (220, 60, 50))  # raised hand with a brush
    R(d, 22, 21, 25, 30, robe); R(d, 23, 30, 25, 31, skin)  # other arm
    d.ellipse([21, 30, 31, 36], fill=(150, 105, 65)); P(d, [(23, 32), (25, 31), (27, 32), (29, 33), (26, 34), (28, 35)], (220, 60, 50))  # palette
    P(d, [(25, 31)], PAINTS[1]); P(d, [(27, 32)], PAINTS[2]); P(d, [(29, 33)], PAINTS[3]); P(d, [(26, 34)], PAINTS[5])
    return im
def street_tipsy_muse():  # tipsy_muse.jpg (PG-13): smiling, short blue hair, paint-splattered denim overall shorts with a full bib, sandals
    im, d = canvas(); shadow(d); skin, denim, dk, hair = (200, 140, 95), (50, 65, 105), (35, 45, 75), (40, 110, 230)
    R(d, 12, 35, 14, 43, skin); R(d, 17, 35, 19, 43, skin)  # bare legs
    R(d, 11, 44, 14, 45, (120, 70, 35)); R(d, 17, 44, 20, 44, (120, 70, 35)); P(d, [(12, 42), (18, 42)], (120, 70, 35))  # strappy sandals
    R(d, 10, 29, 21, 35, denim); P(d, [(15, 33), (16, 34)], dk); R(d, 10, 35, 13, 35, (90, 105, 140)); R(d, 18, 35, 21, 35, (90, 105, 140))  # shorts, frayed hems
    R(d, 9, 18, 22, 28, skin)  # shoulders / arms-in silhouette
    R(d, 11, 21, 20, 29, denim); R(d, 13, 24, 18, 27, dk)  # full bib (covers the whole chest) with its pocket
    d.line([(11, 21), (11, 18)], fill=denim); d.line([(20, 21), (20, 18)], fill=denim); P(d, [(11, 21), (20, 21)], (230, 200, 120))  # straps + brass buttons
    R(d, 7, 19, 9, 30, skin); R(d, 22, 19, 24, 30, skin)  # arms down at her sides
    for i, (x, y) in enumerate([(12, 23), (19, 26), (14, 30), (20, 32), (11, 33), (16, 22), (8, 25), (13, 39), (18, 37)]): P(d, [(x, y)], PAINTS[i % 6])  # paint splatter
    _face(d, skin, mouth=(170, 50, 60)); R(d, 14, 15, 17, 15, (255, 255, 255))  # big smile
    R(d, 9, 2, 22, 6, hair); R(d, 9, 6, 11, 14, hair); R(d, 20, 6, 22, 14, hair); P(d, [(9, 15), (22, 15), (8, 4), (23, 5), (13, 1), (18, 1)], hair)  # short spiky blue bob
    R(d, 12, 6, 15, 7, hair); P(d, [(14, 4), (19, 3)], (130, 190, 255))  # fringe + highlights
    return im
def street_acrobats():  # acrobats.jpg: two acrobats in striped bodysuits doing handstands on a mosaic street
    im, d = canvas()
    for x in range(0, 32): P(d, [(x, 46), (x, 47)], PAINTS[(x // 2) % 6] if x % 2 else (40, 50, 90))  # mosaic street
    stripes = [(200, 50, 60), (130, 70, 150), (40, 130, 140), (230, 170, 60), (40, 50, 100)]
    for ox in (2, 17):  # two upside-down bodies: hands on the ground, legs straight up
        R(d, ox + 2, 37, ox + 3, 45, SK_M); R(d, ox + 9, 37, ox + 10, 45, SK_M); R(d, ox + 1, 45, ox + 3, 45, SK_M); R(d, ox + 9, 45, ox + 11, 45, SK_M)  # arms + hands
        R(d, ox + 4, 39, ox + 8, 44, SK_M); R(d, ox + 4, 43, ox + 8, 44, (30, 22, 20)); P(d, [(ox + 3, 44), (ox + 9, 44)], (30, 22, 20)); P(d, [(ox + 5, 41), (ox + 7, 41)], (20, 20, 30)); P(d, [(ox + 6, 39)], (150, 80, 70))  # head down, dark hair at the bottom
        R(d, ox + 3, 35, ox + 9, 37, SK_M)  # bare shoulders
        for y in range(4, 35): R(d, ox + 4 if y < 24 else ox + 3, y, ox + 8 if y < 24 else ox + 9, y, stripes[(y // 2) % 5])  # striped bodysuit (torso + legs)
        R(d, ox + 4, 3, ox + 8, 23, (0, 0, 0, 0))
        for y in range(4, 24): R(d, ox + 4, y, ox + 5, y, stripes[(y // 2) % 5]); R(d, ox + 7, y, ox + 8, y, stripes[(y // 2) % 5])  # two legs
        R(d, ox + 4, 1, ox + 5, 3, SK_M); R(d, ox + 7, 1, ox + 8, 3, SK_M)  # bare feet pointing up
    return im

# Chrome Quarter encounters: PLACEHOLDER sprites (no art yet). TO SWAP: drop joetopia-art-src/chrome/<id>.jpg and restyle here.
NEON = [(0, 230, 255), (255, 40, 200), (120, 255, 120)]
def street_courier():  # hover-skating courier in a neon jacket holding out a holo-envelope + stylus
    im, d = canvas(); shadow(d); jacket, skin = (40, 40, 60), SK_M
    R(d, 10, 44, 21, 45, (90, 90, 110)); P(d, [(11, 46), (20, 46)], NEON[0])  # hover-skates glowing underneath
    R(d, 11, 32, 14, 43, (30, 30, 45)); R(d, 17, 32, 20, 43, (30, 30, 45))  # legs
    R(d, 9, 19, 22, 32, jacket); d.line([(9, 25), (22, 25)], fill=NEON[1]); d.line([(15, 19), (15, 32)], fill=NEON[0])  # neon-trim jacket
    R(d, 5, 13, 11, 25, (90, 90, 110)); P(d, [(6, 14), (9, 14)], NEON[0])  # drone backpack (behind the shoulder)
    R(d, 22, 21, 27, 23, jacket); R(d, 26, 18, 31, 23, (150, 230, 255)); P(d, [(28, 20), (29, 21)], (255, 255, 255))  # arm out with the holo-envelope
    d.line([(24, 24), (27, 28)], fill=(200, 200, 210))  # stylus
    _face(d, skin, hair=(30, 25, 25), mouth=(160, 60, 60)); R(d, 10, 3, 21, 5, NEON[1])  # cap
    return im
def street_public_pooper():  # (comedic, implied) a Technomancer crouched behind a recycling drone: only head, hood and hitched robe show
    im, d = canvas(); shadow(d); robe, skin = (70, 40, 140), SK_M
    R(d, 9, 22, 22, 36, robe); P(d, [(11, 24), (15, 27), (20, 30)], NEON[0])  # crouched holo-robe hunched over
    _face(d, skin, top=11, hair=(40, 30, 30), mouth=(140, 60, 60)); R(d, 9, 9, 22, 12, robe)  # hood
    R(d, 21, 22, 26, 26, (30, 30, 40)); P(d, [(23, 23)], NEON[2])  # phone held up, he keeps scrolling
    R(d, 3, 30, 28, 45, (90, 110, 100)); R(d, 4, 31, 27, 32, (130, 150, 140)); P(d, [(8, 37), (9, 37), (22, 37), (23, 37)], NEON[2])  # recycling drone hiding everything below the waist
    d.text((12, 37), '♻', fill=(120, 255, 120)) if False else P(d, [(14, 38), (15, 37), (16, 38), (15, 40), (14, 39), (16, 39)], (180, 255, 180))  # recycle logo
    for x, y in ((25, 6), (27, 4), (29, 7)): P(d, [(x, y)], (150, 200, 120))  # stink lines
    d.line([(25, 9), (26, 6)], fill=(150, 200, 120)); d.line([(28, 10), (29, 7)], fill=(150, 200, 120))
    return im
def street_discarded_tech():  # a pile of e-waste with a cracked, sparking gadget on top
    im, d = canvas()
    R(d, 2, 34, 29, 45, (60, 60, 70)); P(d, [(x, 34) for x in range(3, 29, 3)], (90, 90, 100))  # junk heap
    for x, y, c in ((5, 38, (120, 40, 40)), (12, 41, (40, 90, 130)), (20, 39, (90, 90, 40)), (25, 42, (60, 120, 60))): R(d, x, y, x + 3, y + 2, c)  # broken boards
    R(d, 10, 22, 21, 33, (40, 40, 55)); R(d, 11, 23, 20, 31, (20, 120, 160)); d.line([(12, 24), (19, 30)], fill=(220, 240, 255)); d.line([(18, 23), (14, 31)], fill=(220, 240, 255))  # cracked screen
    P(d, [(22, 20), (23, 18), (24, 21), (21, 17), (25, 19)], (255, 230, 80)); P(d, [(8, 19), (7, 17)], (255, 230, 80))  # sparks
    P(d, [(20, 25)], (255, 40, 40))  # error light
    return im
def street_toll_path():  # chrome-armoured toll guard with a shock-baton beside a glowing turnstile
    im, d = canvas(); shadow(d); chrome, dk = (190, 200, 210), (110, 120, 135)
    R(d, 24, 26, 30, 44, (60, 60, 75)); R(d, 23, 30, 31, 31, NEON[0]); R(d, 23, 36, 31, 37, NEON[0])  # turnstile
    R(d, 9, 33, 13, 44, dk); R(d, 15, 33, 19, 44, dk)  # armoured legs
    R(d, 7, 18, 21, 33, chrome); R(d, 10, 20, 18, 28, dk); P(d, [(12, 22), (16, 22)], (255, 255, 255))  # chest plate
    R(d, 3, 19, 6, 30, chrome); R(d, 22, 19, 24, 27, chrome)  # arms
    d.line([(2, 31), (2, 20)], fill=(40, 40, 50)); P(d, [(2, 19), (1, 18), (3, 18), (2, 17)], NEON[0])  # crackling shock-baton
    R(d, 8, 3, 20, 16, chrome); R(d, 9, 8, 19, 10, (30, 30, 40)); R(d, 10, 9, 18, 9, (255, 50, 60))  # helmet with red visor
    return im

SPRITES = {'robert': robert, 'ramirez': ramirez, 'rob': rob, 'joseph': joseph, 'miranda': miranda,
           'alex': alex, 'sean': sean, 'alec': alec, 'lydia': lydia,
           'enc_guard': enc_guard, 'enc_preacher': enc_preacher, 'enc_egirl': enc_egirl,
           'enc_trader': enc_trader, 'enc_goblins': enc_goblins, 'enc_fans': enc_fans,
           **{f'street_{k}': globals()[f'street_{k}'] for k in ('punks', 'drunk', 'party_girls', 'beggar', 'geneticist', 'preacher',
              'drone', 'pickpocket', 'megaphone', 'tourist', 'stranger', 'noble', 'creep', 'temptress', 'pirates', 'rats', 'sailor', 'streetwalker', 'kraken',
              'duel', 'angry_local', 'parade', 'fireworks', 'bald_brawl', 'starving_artist', 'tipsy_muse', 'acrobats',
              'courier', 'public_pooper', 'discarded_tech', 'toll_path')}}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SPRITES.items(): fn().save(os.path.join(OUT, name + '.png'))
    print('wrote', len(SPRITES), 'sprites to', os.path.normpath(OUT))
