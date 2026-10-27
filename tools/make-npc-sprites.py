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

# Chrome Quarter encounters: all four sprites match their real art (courier.jpg, rude_worker.jpg, broken_tech.jpg, toll.jpg).
NEON = [(0, 230, 255), (255, 40, 200), (120, 255, 120)]
def street_courier():  # (matches courier.jpg) BAB-07 courier: grey armoured suit, red-lit roller skates, holding out a signature tablet
    im, d = canvas(); shadow(d); grey, dk, skin, red = (150, 155, 165), (95, 100, 110), SK_T, (255, 40, 50)
    R(d, 10, 43, 15, 44, (60, 60, 70)); R(d, 17, 43, 22, 44, (60, 60, 70)); P(d, [(11, 45), (14, 45), (18, 45), (21, 45)], red)  # skates, red-lit wheels
    R(d, 11, 32, 14, 42, grey); R(d, 17, 32, 20, 42, grey); P(d, [(12, 36), (18, 36)], dk); P(d, [(13, 41), (19, 41)], red)  # armoured legs + knee pads
    R(d, 9, 18, 22, 32, grey); R(d, 11, 20, 20, 26, dk); P(d, [(12, 22), (14, 22), (16, 22)], (230, 230, 235))  # chest plate "BAB-07"
    R(d, 9, 29, 22, 30, (60, 60, 70)); P(d, [(10, 21), (21, 21)], red)  # belt + red suit lights
    R(d, 5, 20, 8, 30, grey)  # arm swinging back
    R(d, 22, 20, 26, 23, grey); R(d, 24, 22, 31, 29, (25, 25, 30)); R(d, 25, 23, 30, 25, (235, 235, 240)); R(d, 25, 27, 30, 27, red)  # signature tablet held out
    _face(d, skin, hair=(25, 20, 20), mouth=(150, 70, 60)); R(d, 9, 15, 22, 17, dk)  # dark curls, grey hood collar
    return im
def street_rude_worker():  # (matches rude_worker.jpg) bald contract tech worker: big mustache, glowing red forehead implant, white shirt + wrap, red sash, chrome bracers, pointing
    im, d = canvas(); shadow(d); white, wrap, skin, chrome = (235, 232, 225), (205, 200, 190), SK_D, (200, 205, 215)
    R(d, 10, 34, 14, 44, (190, 170, 130)); R(d, 17, 34, 21, 44, (190, 170, 130))  # khaki trousers
    R(d, 9, 19, 22, 34, white); d.line([(10, 19), (21, 31)], fill=wrap); d.line([(11, 19), (22, 30)], fill=wrap)  # white shirt + diagonal wrap
    R(d, 9, 31, 22, 33, (200, 30, 40)); R(d, 15, 33, 17, 38, (200, 30, 40))  # red sash with a hanging knot
    R(d, 6, 20, 9, 31, white); R(d, 6, 28, 9, 30, chrome); P(d, [(7, 29)], (255, 40, 40))  # left arm, chrome bracer
    R(d, 22, 20, 28, 23, white); R(d, 24, 20, 26, 23, chrome); P(d, [(25, 21)], (255, 40, 40))  # pointing arm, bracer
    R(d, 28, 21, 29, 23, skin); R(d, 30, 21, 31, 21, skin)  # hand + jabbing finger
    _face(d, skin, mouth=None)  # bald: no hair
    P(d, [(15, 8), (16, 8)], (255, 30, 30)); P(d, [(15, 7), (16, 7)], (220, 220, 230))  # glowing red forehead implant
    R(d, 12, 14, 19, 15, (25, 20, 20)); P(d, [(11, 16), (20, 16)], (25, 20, 20))  # big mustache
    d.line([(12, 11), (14, 12)], fill=(30, 20, 20)); d.line([(19, 11), (17, 12)], fill=(30, 20, 20))  # stern brows
    return im
def street_discarded_tech():  # (matches broken_tech.jpg) a cracked, rune-covered phone lying in a street trash can
    im, d = canvas()
    d.ellipse([3, 40, 28, 47], fill=(0, 0, 0, 90))
    R(d, 5, 26, 26, 44, (55, 58, 65)); R(d, 4, 24, 27, 27, (85, 90, 100))  # metal trash can + rim
    for x in (9, 14, 19, 23): d.line([(x, 29), (x, 43)], fill=(45, 48, 55))  # ribs
    R(d, 6, 22, 25, 25, (30, 30, 36)); P(d, [(7, 21), (11, 20), (20, 21), (24, 22)], (70, 70, 80))  # black bags of rubbish
    R(d, 11, 12, 20, 25, (20, 20, 28)); R(d, 12, 13, 19, 24, (35, 20, 55))  # phone + dark screen
    P(d, [(13, 15), (14, 17), (16, 16), (18, 19), (15, 21), (17, 22), (13, 20)], (220, 80, 255))  # glowing purple runes
    d.line([(12, 14), (19, 23)], fill=(220, 225, 240)); d.line([(18, 13), (13, 24)], fill=(220, 225, 240))  # cracks
    R(d, 1, 2, 6, 8, (255, 50, 50)); P(d, [(2, 4), (4, 4), (3, 6), (5, 6)], (120, 0, 0))  # red holo sign
    R(d, 24, 1, 30, 9, (60, 255, 120)); P(d, [(25, 3), (27, 3), (26, 5), (28, 7)], (0, 100, 40))  # green holo sign
    return im
def street_toll_path():  # (matches toll.jpg) chrome toll-gate arch with a red sign over a gleaming walkway between holo-signs
    im, d = canvas(); chrome, dk = (200, 205, 215), (90, 95, 110)
    d.polygon([(11, 47), (20, 47), (17, 30), (14, 30)], fill=(175, 180, 195)); d.line([(15, 31), (15, 46)], fill=(240, 240, 250))  # gleaming walkway
    R(d, 7, 14, 10, 40, chrome); R(d, 21, 14, 24, 40, chrome); R(d, 8, 15, 9, 39, dk); R(d, 22, 15, 23, 39, dk)  # chrome pillars
    R(d, 6, 11, 25, 15, chrome); R(d, 8, 12, 23, 14, (40, 20, 25)); P(d, [(9, 13), (11, 13), (13, 13), (15, 13), (18, 13), (20, 13), (22, 13)], (255, 60, 60))  # arch + red sign
    R(d, 0, 4, 5, 12, (255, 50, 50)); P(d, [(1, 6), (3, 6), (2, 8), (4, 10)], (120, 0, 0))  # red holo sign
    R(d, 26, 2, 31, 11, (60, 255, 120)); P(d, [(27, 4), (29, 4), (28, 7), (30, 9)], (0, 100, 40))  # green holo sign
    P(d, [(2, 42), (4, 44), (28, 43), (26, 45)], (255, 60, 60)); P(d, [(27, 41), (29, 44)], (60, 255, 120))  # neon reflections
    return im

# Gilded Spire encounters: all four sprites match their real art (chariot.jpg, reality_show.jpg, jewelry.jpg, charity.jpg).
GOLD, GOLD_D, IVORY, SILVER = (240, 200, 70), (180, 140, 40), (245, 240, 228), (195, 200, 210)
def street_runaway_chariot():  # (matches chariot.jpg) man in a white toga + gold-rimmed sunglasses on a silver-and-gold hover-chariot, glowing thrusters
    im, d = canvas()
    d.ellipse([6, 43, 26, 47], fill=(255, 220, 120, 120))  # hover glow on the marble
    R(d, 9, 15, 22, 25, IVORY); d.line([(10, 16), (20, 24)], fill=GOLD); R(d, 7, 17, 9, 24, SK_T); R(d, 22, 17, 24, 24, SK_T)  # toga + gold sash, arms on the rails
    _face(d, SK_T, hair=(25, 20, 20), mouth=None); R(d, 11, 10, 20, 11, GOLD); P(d, [(12, 11), (13, 11), (18, 11), (19, 11)], (235, 240, 255))  # gold-rimmed shades
    d.polygon([(6, 22), (26, 22), (21, 38), (16, 42), (11, 38)], fill=SILVER); d.polygon([(10, 24), (22, 24), (19, 34), (16, 37), (13, 34)], fill=(110, 115, 125))  # chariot hull
    d.line([(16, 24), (16, 40)], fill=GOLD); P(d, [(13, 29), (19, 29)], (255, 230, 140))  # gold trim, headlamps
    R(d, 1, 27, 6, 31, SILVER); R(d, 26, 27, 31, 31, SILVER); P(d, [(2, 29), (29, 29)], (255, 210, 90))  # side thrusters
    d.line([(0, 33), (6, 31)], fill=(255, 210, 90)); d.line([(31, 33), (26, 31)], fill=(255, 210, 90))  # light trails
    return im
def street_reality_show():  # (matches reality_show.jpg, PG-13) celebrity Valeria Kurigalzu: long dark hair, gold chain gown, walking a small white dog
    im, d = canvas(); shadow(d); hair, gown = (30, 22, 20), (225, 200, 140)
    R(d, 9, 6, 22, 24, hair)  # long dark hair behind
    d.polygon([(9, 45), (22, 45), (19, 22), (12, 22)], fill=gown); R(d, 11, 18, 20, 23, GOLD); R(d, 11, 25, 20, 26, GOLD)  # gold top + belt, long draped skirt
    for y in (30, 35, 40): P(d, [(12, y), (16, y + 1), (19, y)], GOLD_D)  # chain fringe
    R(d, 7, 19, 9, 30, SK_T); R(d, 22, 19, 24, 30, SK_T); P(d, [(8, 26), (23, 26)], GOLD)  # arms + cuffs
    _face(d, SK_T, hair=hair, mouth=(170, 70, 80)); P(d, [(10, 12), (21, 12)], GOLD)  # earrings
    d.line([(24, 30), (27, 40)], fill=GOLD)  # chain leash
    R(d, 25, 40, 30, 44, (248, 248, 248)); R(d, 26, 38, 28, 40, (248, 248, 248)); P(d, [(26, 39)], (30, 30, 30))  # small white dog
    return im
def street_lost_jewelry():  # (matches jewelry.jpg) a glowing engraved gold ring lying on a white marble floor
    im, d = canvas()
    R(d, 0, 26, 31, 47, (235, 232, 228)); d.line([(2, 30), (12, 40)], fill=(200, 198, 195)); d.line([(20, 28), (30, 44)], fill=(205, 200, 198))  # marble + veins
    d.line([(0, 34), (31, 30)], fill=(210, 180, 100))  # gold inlay line
    d.ellipse([7, 30, 25, 42], fill=(255, 220, 120, 90))  # glow
    d.ellipse([8, 31, 24, 40], outline=GOLD, width=3); d.ellipse([9, 32, 23, 39], outline=GOLD_D)  # ring band
    P(d, [(11, 33), (14, 32), (18, 32), (21, 34), (12, 38), (20, 38)], (120, 80, 20))  # engraving
    P(d, [(15, 30), (24, 28), (6, 35)], (255, 255, 210))  # sparkles
    return im
def street_charity_gala():  # (matches charity.jpg) man in an embroidered white-and-gold coat handing over a wax-sealed invitation
    im, d = canvas(); shadow(d)
    R(d, 10, 34, 14, 44, IVORY); R(d, 17, 34, 21, 44, IVORY)
    R(d, 9, 17, 22, 36, IVORY); d.line([(15, 17), (15, 35)], fill=GOLD); P(d, [(16, 20), (16, 24), (16, 28)], GOLD); P(d, [(11, 22), (12, 27), (20, 30)], GOLD_D)  # embroidered coat
    R(d, 13, 16, 18, 17, GOLD)  # gold collar
    R(d, 6, 18, 9, 30, IVORY); R(d, 22, 18, 25, 24, IVORY); R(d, 24, 24, 26, 26, SK_T)  # arms, hand out
    R(d, 23, 25, 31, 31, (240, 232, 210)); P(d, [(27, 28), (26, 28), (27, 27)], (170, 20, 30))  # invitation + red wax seal
    _face(d, SK_T, hair=(25, 20, 20), mouth=(150, 70, 60))
    return im

# Reality-show episodes (Street.EPISODES): sprites match togiru.jpg, blind_date_noble.jpg, bathsheba.jpg, fletcher.jpg, petyr.jpg (PG-13).
def street_reality_pushup():  # Togiru: black hair, black-and-gold winged-lion tank top and kilt, gold mic
    im, d = canvas(); shadow(d); blk = (28, 26, 30)
    R(d, 11, 34, 14, 44, SK_T); R(d, 17, 34, 20, 44, SK_T); R(d, 10, 44, 14, 45, GOLD_D); R(d, 17, 44, 21, 45, GOLD_D)  # legs + sandals
    R(d, 9, 28, 22, 35, blk); P(d, [(10, 34), (13, 35), (16, 34), (19, 35), (21, 34)], GOLD); R(d, 9, 27, 22, 28, GOLD)  # kilt + gold belt/fringe
    R(d, 10, 17, 21, 27, blk); P(d, [(14, 21), (15, 20), (16, 20), (17, 21), (15, 22), (16, 22), (13, 22), (18, 22)], GOLD)  # tank top + winged lion
    R(d, 6, 17, 9, 28, SK_T); R(d, 22, 17, 25, 22, SK_T); R(d, 21, 13, 24, 17, SK_T)  # big arms, one raised to the mic
    R(d, 21, 10, 23, 13, GOLD); R(d, 21, 9, 23, 10, (60, 50, 40))  # gold mic
    _face(d, SK_T, hair=(20, 18, 22), mouth=(150, 80, 70)); P(d, [(15, 17), (16, 17)], GOLD)  # chain
    return im
def street_reality_blind_date():  # Lady Ysolde Carnelian: red curls, red-and-gold jewelled gown, by a table with a floating camera
    im, d = canvas(); shadow(d); red, hair = (165, 25, 35), (175, 45, 30)
    R(d, 9, 5, 23, 22, hair)  # red curls
    d.polygon([(9, 45), (23, 45), (20, 21), (12, 21)], fill=red); R(d, 11, 19, 21, 23, red); P(d, [(12, 20), (20, 20), (16, 22), (14, 28), (18, 33), (16, 40)], GOLD)  # high-necked gown, gold jewels
    R(d, 7, 20, 9, 30, SK_T); R(d, 23, 20, 25, 30, SK_T); P(d, [(8, 26), (24, 26)], GOLD)  # arms + cuffs
    _face(d, SK_T, hair=hair, mouth=(190, 20, 40)); P(d, [(10, 12), (22, 12)], GOLD)
    R(d, 0, 35, 6, 37, (230, 222, 210)); R(d, 2, 37, 4, 44, GOLD_D)  # little table
    R(d, 1, 24, 6, 28, (60, 50, 40)); P(d, [(3, 26)], (190, 90, 255)); P(d, [(2, 30), (5, 30)], (190, 90, 255, 120))  # floating camera, purple lens
    P(d, [(26, 40), (28, 42), (29, 39)], (200, 30, 50))  # rose petals
    return im
def street_reality_makeup():  # Bathsheba: long dark hair with pink streaks, blue dress, lipstick at a gilded vanity
    im, d = canvas(); shadow(d); hair, blue = (30, 22, 26), (60, 95, 170)
    R(d, 8, 5, 22, 28, hair); d.line([(9, 9), (9, 26)], fill=(225, 90, 160)); d.line([(21, 9), (21, 26)], fill=(225, 90, 160))  # hair + pink streaks
    d.polygon([(9, 45), (21, 45), (20, 21), (10, 21)], fill=blue); R(d, 10, 19, 20, 22, blue)  # dress, covered
    R(d, 7, 20, 9, 30, SK_T); R(d, 20, 15, 22, 21, SK_T); R(d, 20, 13, 21, 15, (200, 40, 80)); P(d, [(20, 12)], GOLD)  # arm raised with lipstick
    _face(d, SK_T, hair=hair, mouth=(190, 70, 100)); P(d, [(10, 12), (20, 12)], GOLD)
    R(d, 23, 30, 31, 33, (240, 236, 226)); R(d, 23, 33, 31, 34, GOLD); R(d, 24, 34, 25, 44, GOLD_D); R(d, 29, 34, 30, 44, GOLD_D)  # marble-and-gold vanity
    R(d, 25, 27, 26, 30, (40, 30, 30)); R(d, 28, 28, 29, 30, GOLD)  # brushes, compact
    return im
def street_reality_fletcher():  # Fletcher: big bearded podcast host, white-and-gold toga, navy cap, wooden-spoon mic
    im, d = canvas(); shadow(d)
    R(d, 11, 41, 14, 44, SK_T); R(d, 18, 41, 21, 44, SK_T)
    d.polygon([(7, 42), (25, 42), (24, 17), (8, 17)], fill=IVORY); d.line([(9, 18), (23, 40)], fill=GOLD); R(d, 8, 27, 24, 28, GOLD)  # wide toga, gold sash + belt
    R(d, 5, 18, 8, 30, IVORY); R(d, 24, 18, 27, 26, SK_T)
    d.line([(26, 25), (26, 36)], fill=(160, 110, 60), width=2); R(d, 25, 22, 27, 25, (40, 40, 45))  # wooden spoon + mic
    _face(d, SK_T, hair=(30, 22, 18), beard=(30, 22, 18), mouth=None); R(d, 10, 4, 21, 7, (30, 40, 80)); R(d, 9, 7, 16, 8, (30, 40, 80)); P(d, [(15, 5)], (240, 240, 255))  # navy cap
    return im
def street_reality_petyr():  # Petyr: curly hair, cream-and-gold jester hat and robes, gold mic held out
    im, d = canvas(); shadow(d); cream = (236, 226, 200)
    d.polygon([(9, 45), (22, 45), (21, 18), (10, 18)], fill=cream); d.line([(15, 18), (15, 44)], fill=GOLD); P(d, [(11, 30), (20, 30), (12, 38), (19, 38)], GOLD_D)
    R(d, 7, 18, 10, 30, cream); R(d, 21, 19, 28, 22, cream); R(d, 27, 18, 30, 21, SK_T); R(d, 28, 15, 31, 18, GOLD)  # arm out with gold mic
    _face(d, SK_T, hair=(45, 30, 22), mouth=(150, 80, 70))
    d.polygon([(8, 7), (12, 0), (15, 6), (19, 0), (23, 7)], fill=cream); R(d, 9, 6, 22, 8, GOLD); P(d, [(12, 0), (19, 0), (8, 7), (23, 7)], GOLD)  # jester hat + bells
    return im

# Wizard Couriers (matches spire/wizard_courier.jpg): white-bearded wizard, pointed red hat, crimson gold-trimmed robes, spectacles,
# holding out a glowing amber vial. TO SWAP: replace wizard_courier.jpg + rerun make-encounter-art.py; restyle here.
def street_wizard_couriers():
    im, d = canvas(); shadow(d); red, redd, beard = (140, 22, 28), (95, 14, 20), (236, 234, 228)
    d.polygon([(7, 45), (24, 45), (22, 18), (9, 18)], fill=red); d.line([(15, 19), (15, 44)], fill=GOLD); P(d, [(10, 30), (21, 30), (11, 38), (20, 38)], GOLD_D)  # robe + gold trim
    R(d, 5, 18, 9, 32, redd); R(d, 22, 19, 29, 23, red); R(d, 27, 18, 30, 22, SK_T)  # sleeves, arm held out
    R(d, 28, 13, 30, 17, (255, 170, 40)); P(d, [(29, 12)], (200, 190, 170)); P(d, [(27, 14), (31, 14)], (255, 200, 90, 140))  # glowing amber vial + glow
    _face(d, SK_T, hair=(220, 220, 215), beard=beard, mouth=None); R(d, 11, 15, 20, 24, beard)  # long white beard
    P(d, [(12, 8), (13, 8), (18, 8), (19, 8)], (200, 170, 90))  # spectacles
    R(d, 7, 3, 24, 4, red); d.polygon([(10, 3), (21, 3), (17, -10), (13, -6)], fill=red); P(d, [(12, 2), (19, 2)], GOLD)  # wide brim + pointed hat
    return im
def street_adrenochrome():  # the sealed amber vial on its own (item picture)
    im, d = canvas()
    d.ellipse([6, 18, 26, 44], fill=(255, 190, 60, 60)); R(d, 12, 22, 19, 41, (255, 160, 30)); R(d, 13, 23, 15, 38, (255, 215, 120))  # glow, vial, highlight
    R(d, 13, 17, 18, 21, (210, 205, 195)); R(d, 12, 15, 19, 16, GOLD)  # neck, gold seal
    return im


# ---- Toadstool Forest (matches joetopia-art-src/forest/*.jpg; the gnome and the item icons are drawn here) ----
MOSS, MOSS_D, BARK, BARK_D = (110, 140, 90), (75, 100, 62), (95, 62, 38), (60, 38, 24)
def street_troll():  # green one-eyed troll, tusks, leather loincloth, spiked club over the shoulder (troll.jpg)
    im, d = canvas(); d.ellipse([3, 44, 28, 47], fill=(0, 0, 0, 90)); g, gd = (120, 145, 105), (85, 105, 75)
    R(d, 7, 16, 24, 34, g); R(d, 5, 18, 7, 32, gd); R(d, 24, 18, 26, 32, gd)  # huge torso + arms
    R(d, 9, 30, 22, 36, BARK); R(d, 9, 37, 14, 44, gd); R(d, 17, 37, 22, 44, gd)  # loincloth + legs
    R(d, 10, 5, 21, 16, g); R(d, 13, 8, 18, 10, (240, 230, 200)); P(d, [(15, 9), (16, 9)], (20, 20, 20))  # head + ONE eye
    P(d, [(11, 14), (11, 13), (20, 14), (20, 13)], (245, 240, 220)); R(d, 13, 13, 18, 13, (60, 30, 30))  # tusks + mouth
    d.line([(26, 31), (30, 6)], fill=BARK_D, width=3); P(d, [(28, 9), (31, 12), (27, 14), (30, 17)], (200, 200, 190))  # spiked club
    return im
def street_weirdo():  # long-haired bearded woodsman, green cloak, leather vest, pouches + tools, hand held out (weirdo.jpg)
    im, d = canvas(); shadow(d); hair = (60, 40, 28)
    d.polygon([(6, 18), (25, 18), (27, 44), (4, 44)], fill=(55, 75, 50)); R(d, 10, 18, 21, 38, (110, 75, 45))  # cloak + vest
    R(d, 9, 30, 22, 31, BARK_D); R(d, 9, 32, 12, 36, (130, 90, 55)); R(d, 19, 32, 22, 36, (130, 90, 55)); P(d, [(15, 33), (16, 34), (15, 35)], (170, 170, 175))  # belt, pouches, tool
    legs(d, (70, 55, 40), 39, 44); R(d, 21, 22, 30, 25, (110, 75, 45)); R(d, 28, 21, 31, 25, SK_M)  # arm out, open hand
    _face(d, SK_M, hair=hair, beard=hair, mouth=None); R(d, 9, 4, 11, 18, hair); R(d, 20, 4, 22, 18, hair)  # long hair + big beard
    R(d, 13, 15, 18, 15, (230, 220, 210))  # grin
    return im
def street_trustworthy_human():  # felt puppet "human": floppy hat, ping-pong eyes, big nose, green coat, BLUE CLAWED HAND
    im, d = canvas(); shadow(d); felt = (205, 160, 110)
    R(d, 9, 18, 22, 41, (95, 100, 55)); R(d, 13, 18, 18, 36, (230, 220, 195))  # coat + shirt
    legs(d, (90, 70, 50), 41, 44); R(d, 6, 20, 9, 32, (95, 100, 55)); R(d, 22, 22, 29, 25, (95, 100, 55))
    R(d, 26, 20, 31, 27, (70, 120, 210)); P(d, [(31, 19), (31, 22), (31, 25), (26, 28)], (40, 40, 40))  # blue hand + claws
    R(d, 10, 6, 21, 17, felt); R(d, 11, 8, 14, 11, (250, 250, 250)); R(d, 17, 8, 20, 11, (250, 250, 250)); P(d, [(13, 10), (18, 10)], (20, 20, 20))  # ping-pong eyes
    R(d, 14, 11, 17, 13, (175, 125, 85)); R(d, 13, 14, 18, 15, (120, 40, 40))  # nose + mouth
    R(d, 6, 4, 25, 6, (120, 85, 55)); R(d, 10, 0, 21, 4, (120, 85, 55)); P(d, [(19, 2), (20, 2)], (180, 120, 230))  # floppy hat + flower
    return im
def street_unicorn():  # yellow unicorn, golden mane, rainbow horn (unicorn.jpg)
    im, d = canvas(); shadow(d); y, yd, mane = (245, 225, 110), (215, 190, 80), (240, 190, 60)
    R(d, 6, 22, 24, 32, y); R(d, 7, 33, 9, 44, yd); R(d, 11, 33, 13, 44, y); R(d, 18, 33, 20, 44, yd); R(d, 22, 33, 24, 44, y)  # body + legs
    R(d, 21, 12, 26, 24, y); R(d, 23, 8, 30, 15, y); P(d, [(27, 10)], (20, 20, 30))  # neck + head
    R(d, 19, 9, 22, 22, mane); R(d, 3, 22, 6, 34, mane)  # mane + tail
    for i, c in enumerate([(230, 50, 50), (240, 150, 40), (240, 230, 60), (60, 190, 80), (60, 120, 230), (150, 70, 200)]): P(d, [(27 + i // 2, 7 - i)], c)  # rainbow horn
    return im
def street_pixie():  # small winged pixie, curly brown hair, green leaf dress (PG-13)
    im, d = canvas(); d.ellipse([10, 44, 21, 47], fill=(0, 0, 0, 70)); wing = (170, 225, 255, 160)
    d.ellipse([2, 12, 13, 26], fill=wing); d.ellipse([18, 12, 29, 26], fill=wing); d.ellipse([4, 24, 13, 33], fill=wing); d.ellipse([18, 24, 27, 33], fill=wing)
    d.polygon([(11, 22), (20, 22), (22, 36), (9, 36)], fill=(60, 150, 70)); P(d, [(10, 35), (13, 36), (17, 36), (21, 35)], (40, 110, 50))  # leaf dress
    R(d, 13, 36, 14, 41, SK_L); R(d, 17, 36, 18, 41, SK_L); R(d, 10, 22, 11, 29, SK_L); R(d, 20, 22, 21, 29, SK_L)
    R(d, 12, 11, 19, 20, SK_L); P(d, [(14, 15), (17, 15)], (40, 30, 20)); P(d, [(15, 18), (16, 18)], (200, 90, 90))
    hair = (110, 70, 40); R(d, 10, 8, 21, 11, hair); R(d, 9, 10, 11, 21, hair); R(d, 20, 10, 22, 21, hair); P(d, [(9, 22), (22, 22), (11, 7), (20, 7)], hair)  # curls
    P(d, [(5, 9), (27, 30), (24, 6)], (255, 240, 150))  # sparkles
    return im
def street_gnome():  # gnome: tall red hat, white beard, flannel shirt, work jeans, tiny axe
    im, d = canvas(); d.ellipse([8, 44, 23, 47], fill=(0, 0, 0, 80))
    R(d, 10, 30, 21, 38, (180, 50, 45)); P(d, [(12, 31), (15, 31), (18, 31), (12, 35), (15, 35), (18, 35)], (110, 25, 25))  # flannel
    R(d, 11, 39, 15, 43, (60, 85, 140)); R(d, 16, 39, 20, 43, (60, 85, 140)); R(d, 10, 44, 15, 45, BARK_D); R(d, 16, 44, 21, 45, BARK_D)  # jeans + boots
    R(d, 11, 20, 20, 28, SK_L); P(d, [(13, 23), (18, 23)], (20, 20, 30)); R(d, 15, 24, 16, 25, (220, 140, 120))
    R(d, 10, 25, 21, 33, (240, 240, 235))  # beard
    d.polygon([(9, 21), (22, 21), (15, 4)], fill=(200, 40, 40))  # pointy hat
    R(d, 22, 26, 23, 36, BARK); R(d, 23, 25, 26, 28, (180, 185, 190))  # axe
    return im
# item icons (log pictures)
def street_unicorn_horn():
    im, d = canvas(); d.ellipse([6, 14, 26, 44], fill=(255, 240, 200, 50))
    for i, c in enumerate([(230, 50, 50), (240, 150, 40), (240, 230, 60), (60, 190, 80), (60, 120, 230), (150, 70, 200)]): d.line([(10 + i * 2, 42 - i * 5), (12 + i * 2, 38 - i * 5)], fill=c, width=3)
    return im
def street_pixie_wings():
    im, d = canvas(); wing = (170, 225, 255, 200); vein = (110, 170, 220)
    d.ellipse([2, 10, 15, 28], fill=wing); d.ellipse([17, 10, 30, 28], fill=wing); d.ellipse([4, 26, 14, 38], fill=wing); d.ellipse([18, 26, 28, 38], fill=wing)
    d.line([(15, 24), (5, 14)], fill=vein); d.line([(16, 24), (26, 14)], fill=vein); P(d, [(8, 8), (25, 40), (28, 9)], (255, 240, 150))
    return im
def street_gnome_hat():
    im, d = canvas(); d.polygon([(6, 38), (26, 38), (16, 6)], fill=(200, 40, 40)); R(d, 4, 37, 27, 40, (160, 30, 30)); return im
def street_work_jeans():
    im, d = canvas(); jean = (60, 85, 140); R(d, 9, 12, 23, 18, jean); R(d, 9, 18, 15, 42, jean); R(d, 17, 18, 23, 42, jean); R(d, 9, 12, 23, 13, BARK); P(d, [(12, 20), (20, 20)], (220, 180, 90)); return im
def street_flannel_shirt():
    im, d = canvas(); r, rd = (180, 50, 45), (110, 25, 25); R(d, 9, 12, 22, 38, r); R(d, 4, 13, 9, 30, r); R(d, 22, 13, 27, 30, r)
    for y in range(14, 38, 5): R(d, 4, y, 27, y, rd)
    for x in (7, 13, 18, 25): R(d, x, 12, x, 38, rd)
    return im
def street_woodsman_axe():
    im, d = canvas(); d.line([(10, 42), (21, 10)], fill=BARK, width=3); d.polygon([(17, 8), (27, 6), (27, 18), (20, 15)], fill=(185, 190, 195)); return im
def street_unicorn_wand():
    im, d = canvas(); d.line([(10, 42), (22, 8)], fill=(245, 225, 110), width=2)
    for i, c in enumerate([(230, 50, 50), (240, 230, 60), (60, 190, 80), (60, 120, 230)]): P(d, [(21 + i % 2, 9 - i), (19 - i, 6 + i)], c)
    return im
def street_unicorn_sword():
    im, d = canvas(); d.line([(16, 4), (16, 34)], fill=(250, 245, 230), width=3)
    for i, c in enumerate([(230, 50, 50), (240, 150, 40), (240, 230, 60), (60, 190, 80), (60, 120, 230), (150, 70, 200)]): P(d, [(16, 6 + i * 5)], c)
    R(d, 10, 34, 22, 36, GOLD); R(d, 15, 37, 17, 43, BARK); return im
def street_unicorn_heels():
    im, d = canvas(); y = (245, 225, 110)
    for ox in (2, 16): d.polygon([(ox, 36), (ox + 12, 32), (ox + 13, 38), (ox, 38)], fill=y); R(d, ox + 11, 38, ox + 12, 44, (200, 120, 230)); P(d, [(ox + 2, 34)], (60, 190, 80))
    return im

def street_goblin_banger():  # RED crew: blue-skinned goblin, red bandana, jeans, boots, crackling energy SMG (goblin_banger.jpg)
    im, d = canvas(); shadow(d); sk, skd = (70, 120, 200), (45, 85, 150)
    R(d, 10, 20, 21, 30, (60, 60, 70)); R(d, 10, 31, 21, 38, (60, 85, 140)); R(d, 10, 39, 14, 41, (60, 85, 140)); R(d, 17, 39, 21, 41, (60, 85, 140))  # tee, jeans
    R(d, 9, 42, 14, 45, (70, 50, 35)); R(d, 17, 42, 22, 45, (70, 50, 35))  # boots
    R(d, 7, 21, 9, 29, sk); R(d, 22, 21, 24, 27, sk)  # arms
    R(d, 10, 6, 21, 18, sk); P(d, [(7, 9), (8, 10), (6, 8), (23, 9), (24, 8), (25, 7)], skd)  # head + pointy ears
    R(d, 9, 5, 22, 8, (220, 30, 30)); P(d, [(8, 9), (7, 10)], (220, 30, 30))  # bandana + knot
    R(d, 12, 10, 14, 11, (255, 255, 255)); R(d, 17, 10, 19, 11, (255, 255, 255)); P(d, [(13, 11), (18, 11)], (10, 10, 10))
    R(d, 11, 14, 20, 16, (245, 240, 230)); P(d, [(12, 15), (14, 15), (16, 15), (18, 15)], (90, 20, 20))  # big toothy grin
    R(d, 14, 25, 27, 27, (70, 70, 80)); R(d, 18, 28, 19, 31, (70, 70, 80)); P(d, [(28, 25), (29, 24), (30, 26), (28, 27)], (120, 210, 255))  # SMG + sparks
    return im
def street_goblin_banger_blue():  # BLUE crew: red-skinned goblin, blue bandana, dark trousers, boots, revolver + blue rag (goblin_banger_blue.jpg)
    im, d = canvas(); shadow(d); sk, skd = (200, 60, 50), (150, 40, 35); bl = (60, 100, 190)
    R(d, 10, 20, 21, 30, sk); P(d, [(13, 23), (18, 23), (15, 27)], skd)  # bare red torso
    R(d, 10, 30, 21, 31, (90, 70, 50)); R(d, 10, 32, 21, 38, (40, 38, 36)); R(d, 10, 39, 14, 41, (40, 38, 36)); R(d, 17, 39, 21, 41, (40, 38, 36))  # belt, trousers
    R(d, 9, 42, 14, 45, (120, 95, 60)); R(d, 17, 42, 22, 45, (120, 95, 60))  # boots
    R(d, 7, 21, 9, 29, sk); R(d, 22, 21, 24, 29, sk)  # arms
    R(d, 10, 6, 21, 18, sk); P(d, [(7, 9), (8, 10), (6, 8), (23, 9), (24, 8), (25, 7)], skd)  # head + ears
    R(d, 9, 5, 22, 8, bl); P(d, [(8, 9), (7, 10), (7, 11)], bl)  # blue bandana + knot
    R(d, 12, 10, 14, 11, (250, 170, 40)); R(d, 17, 10, 19, 11, (250, 170, 40)); P(d, [(13, 11), (18, 11)], (10, 10, 10))  # orange eyes
    R(d, 11, 14, 20, 16, (245, 240, 230)); P(d, [(12, 15), (14, 15), (16, 15), (18, 15)], (90, 20, 20))
    R(d, 3, 16, 8, 18, (150, 150, 160)); R(d, 6, 18, 8, 22, (110, 80, 50))  # revolver (left hand)
    R(d, 23, 28, 26, 36, bl); P(d, [(24, 37), (26, 38)], bl)  # blue rag (right hand)
    return im
def street_goblin_revolver():
    im, d = canvas(); R(d, 6, 18, 24, 20, (150, 150, 160)); R(d, 14, 17, 19, 22, (120, 120, 130)); R(d, 17, 22, 21, 32, (110, 80, 50)); R(d, 18, 26, 22, 30, (60, 100, 190)); return im
def street_blue_bandana():
    im, d = canvas(); b = (60, 100, 190); d.polygon([(4, 18), (28, 18), (16, 34)], fill=b); P(d, [(9, 21), (16, 22), (22, 21), (16, 28)], (230, 235, 255)); R(d, 26, 16, 30, 18, b); return im
def street_blue_shiv():
    im, d = canvas(); d.line([(12, 40), (20, 12)], fill=(220, 210, 190), width=2); R(d, 10, 33, 14, 42, (60, 100, 190)); return im
def street_goblin_slingshot():
    im, d = canvas(); w = (120, 85, 50); d.line([(16, 42), (16, 26)], fill=w, width=3); d.line([(16, 27), (9, 12)], fill=w, width=3); d.line([(16, 27), (23, 12)], fill=w, width=3)
    d.line([(9, 13), (16, 22), (23, 13)], fill=(60, 100, 190), width=2); return im
def street_goblin_zapper():
    im, d = canvas(); R(d, 5, 20, 24, 25, (70, 70, 80)); R(d, 10, 26, 13, 34, (70, 70, 80)); R(d, 16, 26, 18, 30, (50, 50, 55)); R(d, 7, 21, 20, 22, (180, 180, 60))
    P(d, [(25, 21), (27, 19), (28, 23), (26, 25), (29, 21)], (120, 210, 255)); return im
def street_banger_bandana():
    im, d = canvas(); r = (220, 30, 30); d.polygon([(4, 18), (28, 18), (16, 34)], fill=r); P(d, [(9, 21), (16, 22), (22, 21), (16, 28)], (255, 230, 230)); R(d, 26, 16, 30, 18, r); return im
def street_red_shiv():
    im, d = canvas(); d.line([(12, 40), (20, 12)], fill=(220, 210, 190), width=2); R(d, 10, 33, 14, 42, (220, 30, 30)); return im
def street_bike_chain():
    im, d = canvas()
    for i in range(9): d.ellipse([6 + i * 2, 8 + i * 4, 10 + i * 2, 12 + i * 4], outline=(220, 30, 30))
    return im
def street_big_booma():
    im, d = canvas(); g = (80, 80, 90); r = (220, 30, 30)
    R(d, 2, 16, 28, 23, g); R(d, 26, 14, 31, 25, (50, 50, 55)); R(d, 8, 24, 12, 34, (110, 80, 50)); R(d, 18, 24, 21, 30, g)  # long barrel, muzzle, grips
    R(d, 4, 17, 6, 22, r); R(d, 14, 17, 16, 22, r); R(d, 22, 17, 24, 22, r)  # red tape
    P(d, [(31, 15), (31, 24), (30, 13)], (255, 190, 60)); return im
def street_ballistic_hat():
    im, d = canvas(); k = (60, 70, 60); d.ellipse([7, 14, 25, 32], fill=k); R(d, 5, 26, 27, 30, (45, 52, 45))  # helmet dome + brim
    R(d, 9, 22, 23, 23, (60, 100, 190)); P(d, [(12, 18), (19, 19), (15, 24)], (110, 120, 110)); return im  # blue band, dents
def street_stem_bat():
    im, d = canvas(); d.line([(10, 42), (22, 8)], fill=(225, 215, 190), width=4); d.line([(10, 42), (13, 34)], fill=(220, 30, 30), width=4); return im

def street_goblin_unaffiliated():  # three grey goblins (goblin_unaffiliated.jpg): bandana + chain + pipe, squatting in purple and yellow, carving a tree
    im, d = canvas(); d.ellipse([0, 44, 31, 47], fill=(0, 0, 0, 90)); g, gd = (150, 155, 160), (110, 115, 120)
    # left: black bandana, black clothes, gold chain, smoking pipe
    R(d, 1, 21, 9, 36, (35, 35, 40)); R(d, 1, 37, 4, 43, (30, 30, 35)); R(d, 6, 37, 9, 43, (30, 30, 35)); R(d, 0, 42, 4, 44, (25, 25, 25)); R(d, 6, 42, 10, 44, (25, 25, 25))
    R(d, 1, 9, 9, 19, g); P(d, [(0, 12), (10, 12), (0, 13)], gd); R(d, 1, 8, 9, 10, (25, 25, 30)); P(d, [(3, 13), (7, 13)], (15, 15, 15)); R(d, 3, 16, 7, 16, (240, 235, 225))
    P(d, [(2, 22), (3, 24), (5, 25), (7, 24), (8, 22), (5, 27)], (200, 160, 50)); R(d, 8, 17, 11, 17, (110, 80, 50)); P(d, [(11, 15), (12, 13), (11, 11)], (200, 200, 200))
    # middle: squatting, purple top, yellow trousers, purple shoes
    R(d, 12, 31, 20, 37, (95, 50, 150)); R(d, 11, 38, 21, 42, (225, 190, 40)); R(d, 11, 43, 14, 44, (95, 50, 150)); R(d, 18, 43, 21, 44, (95, 50, 150))
    R(d, 12, 21, 20, 30, g); P(d, [(11, 24), (21, 24), (10, 23), (22, 23)], gd); P(d, [(14, 25), (18, 25)], (15, 15, 15)); R(d, 15, 28, 17, 28, gd)
    # right: back turned, cream shirt, jeans, tan boots, carving a glyph into a tree
    R(d, 27, 4, 31, 44, (85, 60, 40)); P(d, [(28, 12), (29, 13), (28, 14), (30, 14), (29, 16)], (175, 140, 95))
    R(d, 21, 22, 27, 32, (225, 220, 205)); R(d, 21, 33, 27, 40, (70, 95, 140)); R(d, 21, 41, 23, 44, (175, 130, 70)); R(d, 25, 41, 27, 44, (175, 130, 70))
    R(d, 21, 13, 27, 21, g); P(d, [(20, 16), (28, 17)], gd); R(d, 26, 15, 27, 23, (225, 220, 205)); P(d, [(27, 14)], g)
    return im

def street_bigfoot():  # mother Bigfoot + her baby among giant mushrooms (bigfoot.jpg): big shaggy brown ape-mom, small brown baby at her side
    im, d = canvas(); d.ellipse([0, 44, 31, 47], fill=(0, 0, 0, 90)); fur, fd, fl, face = (95, 65, 40), (65, 42, 25), (125, 90, 55), (55, 45, 40)
    R(d, 26, 2, 27, 10, (225, 215, 195)); d.ellipse([22, 0, 31, 5], fill=(200, 60, 55)); P(d, [(24, 2), (28, 1), (29, 3)], (245, 240, 230))  # toadstool behind
    # mother: tall, hunched, long arms
    R(d, 3, 12, 17, 34, fur); R(d, 1, 15, 4, 33, fd); R(d, 16, 15, 19, 33, fd); R(d, 0, 32, 4, 35, fd); R(d, 16, 32, 19, 35, fd)  # body + long arms + hands
    R(d, 4, 35, 8, 43, fur); R(d, 12, 35, 16, 43, fur); R(d, 3, 43, 9, 45, fd); R(d, 11, 43, 17, 45, fd)  # legs + BIG feet
    R(d, 6, 3, 16, 13, fur); R(d, 9, 6, 16, 11, face); P(d, [(11, 7), (14, 7)], (15, 10, 10)); R(d, 10, 6, 15, 6, fd); R(d, 11, 10, 14, 10, (35, 25, 22))  # head, face, eyes, brow
    P(d, [(5, 18), (8, 22), (13, 20), (6, 27), (14, 28), (10, 31)], fl)  # shaggy fur highlights
    # baby: small, at her side, looking up
    R(d, 20, 28, 27, 39, fur); R(d, 19, 30, 20, 37, fd); R(d, 27, 30, 28, 37, fd)
    R(d, 21, 39, 23, 44, fur); R(d, 25, 39, 27, 44, fur); R(d, 20, 44, 23, 45, fd); R(d, 25, 44, 28, 45, fd)
    R(d, 21, 21, 27, 28, fur); R(d, 23, 23, 27, 27, face); P(d, [(24, 24), (26, 24)], (15, 10, 10)); P(d, [(22, 32), (25, 35)], fl)
    return im

# Dance-floor encounters (joetopia-art-src/dance/*.jpg). Every dancer is fully dressed at sprite scale.
PURPLE, GOLD, GOLD_D = (90, 40, 130), (230, 180, 60), (170, 120, 30)
def street_dance_water():  # water.jpg: sweaty grinning young man, messy blond hair, purple-and-gold vest, one hand reaching out
    im, d = canvas(); shadow(d)
    legs(d, (60, 30, 90), shoe=GOLD_D); R(d, 11, 31, 20, 35, PURPLE); R(d, 11, 31, 20, 31, GOLD)  # baggy purple-gold trousers + belt
    R(d, 10, 18, 21, 30, SK_L); R(d, 10, 18, 13, 30, PURPLE); R(d, 18, 18, 21, 30, PURPLE); P(d, [(11, 20), (12, 24), (19, 22), (20, 27)], GOLD)  # open vest
    R(d, 7, 19, 9, 31, SK_L); R(d, 22, 21, 28, 23, SK_L); R(d, 28, 20, 30, 24, SK_L)  # arm reaching out, open palm
    _face(d, SK_L, mouth=(250, 250, 250)); R(d, 10, 2, 21, 6, (220, 180, 90)); P(d, [(9, 4), (22, 5), (12, 1), (17, 1), (10, 8), (21, 8)], (220, 180, 90))  # messy blond hair
    P(d, [(12, 9), (19, 10), (14, 22), (17, 26)], (255, 255, 255))  # sweat glints
    return im
def street_dance_dj():  # dj.jpg: crowned DJ, gold headphones, pink visor shades, white robe + blue-gold sash, pointing at you
    im, d = canvas(); shadow(d)
    legs(d, (240, 235, 225), shoe=GOLD_D); R(d, 10, 18, 21, 35, (240, 235, 225)); R(d, 13, 18, 15, 35, (40, 70, 160)); P(d, [(14, 21), (14, 26), (14, 31)], GOLD)  # robe + sash
    R(d, 7, 19, 9, 30, (240, 235, 225)); R(d, 22, 18, 26, 20, SK_M); R(d, 26, 17, 29, 19, SK_M); P(d, [(30, 18)], SK_M)  # pointing arm
    _face(d, SK_M, beard=(30, 22, 18)); R(d, 11, 10, 20, 11, (255, 60, 200))  # pink visor shades
    R(d, 9, 8, 10, 13, GOLD); R(d, 21, 8, 22, 13, GOLD); R(d, 10, 4, 21, 4, GOLD_D)  # headphones
    R(d, 11, 0, 20, 4, GOLD); P(d, [(11, 0), (15, 0), (20, 0)], (255, 230, 120)); P(d, [(15, 2)], (40, 70, 200))  # crown with a sapphire
    return im
def street_dance_pickpocket():  # pickpocket.jpg: grinning woman, dark twin ponytails, gold chains, holding a gold-chain purse (dark crop top + skirt)
    im, d = canvas(); shadow(d); skin = (215, 160, 120); hair = (60, 30, 40)
    legs(d, skin, top=36, shoe=GOLD_D); R(d, 10, 29, 21, 36, BLK); P(d, [(11, 36), (14, 36), (17, 36), (20, 36)], GOLD)  # black skirt, gold tassels
    R(d, 10, 18, 21, 29, skin); R(d, 10, 20, 21, 25, BLK); P(d, [(12, 21), (19, 21), (15, 23)], GOLD)  # dark top covering the chest
    R(d, 7, 19, 9, 30, skin); R(d, 22, 19, 24, 30, skin); R(d, 21, 30, 27, 36, BLK); R(d, 21, 30, 27, 30, GOLD); P(d, [(24, 33)], GOLD)  # her purse
    _face(d, skin, hair=hair, mouth=(170, 60, 70)); R(d, 6, 6, 9, 16, hair); R(d, 22, 6, 25, 16, hair); P(d, [(9, 4), (22, 4)], GOLD)  # twin ponytails, gold clips
    return im
def street_dance_boyfriend():  # boyfriend.jpg: angry muscular man in purple-and-gold Babylonian kit, gold headband, fists clenched
    im, d = canvas(); shadow(d)
    legs(d, PURPLE, shoe=GOLD_D); R(d, 9, 30, 22, 36, PURPLE); R(d, 9, 30, 22, 30, GOLD)
    R(d, 8, 17, 23, 30, SK_T); R(d, 11, 17, 20, 30, PURPLE); P(d, [(12, 20), (19, 20), (15, 24), (16, 28)], GOLD)  # broad chest, sash
    R(d, 4, 18, 8, 31, SK_T); R(d, 23, 18, 27, 31, SK_T); R(d, 4, 28, 8, 29, GOLD); R(d, 23, 28, 27, 29, GOLD); R(d, 4, 32, 8, 34, SK_T); R(d, 23, 32, 27, 34, SK_T)  # big arms, cuffs, fists
    _face(d, SK_T, hair=(25, 18, 15), beard=(25, 18, 15), mouth=(120, 40, 40)); R(d, 10, 5, 21, 6, GOLD)  # headband
    P(d, [(12, 9), (13, 10), (18, 10), (19, 9)], (25, 18, 15))  # angry brows
    return im
def street_dance_drinks():  # complimentary_drinks.jpg: server with braided updo, gold collar, cream wrap dress, tray of glowing shots
    im, d = canvas(); shadow(d); skin = (110, 65, 45); hair = (25, 18, 15)
    legs(d, skin, top=37, shoe=GOLD_D); R(d, 10, 18, 21, 37, (235, 225, 200)); R(d, 10, 18, 21, 19, GOLD)  # long cream dress, gold collar
    R(d, 7, 19, 9, 27, skin); R(d, 22, 19, 24, 24, skin); R(d, 21, 24, 31, 25, GOLD)  # arm holding the tray
    for i, x in enumerate(range(22, 31, 2)): R(d, x, 22, x + 1, 23, [(200, 60, 230), (255, 70, 160), (60, 220, 230), (255, 150, 60), (120, 255, 120)][i % 5])  # glowing shots
    _face(d, skin, hair=hair, mouth=(150, 70, 70)); R(d, 12, 0, 19, 3, hair); P(d, [(13, 1), (17, 1)], GOLD); P(d, [(11, 12), (20, 12)], GOLD)  # updo + gold earrings
    return im

# "A stranger asks you to dance" (joetopia-art-src/dance/stranger_1..5.jpg). All fully dressed at sprite scale.
WHITE = (240, 235, 225)
def street_dance_stranger_1():  # grey alien, white-and-gold toga, Groucho glasses + mustache
    im, d = canvas(); shadow(d); g = (175, 180, 185)
    legs(d, g, top=34, shoe=GOLD_D); R(d, 10, 18, 21, 35, WHITE); R(d, 13, 18, 14, 35, GOLD)
    R(d, 7, 19, 9, 29, g); R(d, 22, 19, 24, 29, g)
    _face(d, g, eyes=(10, 10, 10)); R(d, 11, 9, 20, 10, BLK); R(d, 13, 12, 18, 13, (40, 30, 25))  # glasses + mustache
    return im
def street_dance_stranger_2():  # jolly old man, white beard, red-and-gold robe and tall hat
    im, d = canvas(); shadow(d); red = (160, 30, 40)
    legs(d, red, shoe=GOLD_D); R(d, 9, 18, 22, 36, red); R(d, 9, 18, 22, 19, GOLD); R(d, 15, 19, 16, 36, GOLD)
    R(d, 6, 19, 8, 30, red); R(d, 23, 20, 28, 22, red); R(d, 28, 20, 30, 22, SK_L)
    _face(d, SK_L, beard=(240, 240, 240)); R(d, 10, 0, 21, 4, red); R(d, 10, 4, 21, 4, GOLD)
    return im
def street_dance_stranger_3():  # dancer, scarab headpiece, plush Anubis backpack (covered: purple wrap top + long skirt)
    im, d = canvas(); shadow(d); skin = (150, 95, 65); hair = (25, 18, 20)
    legs(d, skin, top=37, shoe=GOLD_D); R(d, 10, 27, 21, 37, PURPLE); R(d, 10, 27, 21, 27, GOLD)
    R(d, 10, 18, 21, 27, PURPLE); P(d, [(12, 20), (19, 20), (15, 24)], GOLD); R(d, 22, 14, 26, 26, BLK); P(d, [(23, 12), (25, 12)], BLK)  # Anubis plush
    R(d, 7, 19, 9, 29, skin); _face(d, skin, hair=hair); R(d, 12, 2, 19, 4, (40, 160, 170)); P(d, [(15, 1)], GOLD)
    return im
def street_dance_stranger_4():  # smiling young man, gold-and-purple open vest, pointing
    im, d = canvas(); shadow(d)
    legs(d, PURPLE, shoe=GOLD_D); R(d, 11, 31, 20, 35, PURPLE); R(d, 11, 31, 20, 31, GOLD)
    R(d, 10, 18, 21, 30, SK_M); R(d, 10, 18, 13, 30, GOLD); R(d, 18, 18, 21, 30, GOLD)
    R(d, 7, 19, 9, 30, SK_M); R(d, 22, 18, 27, 20, SK_M); P(d, [(28, 18)], SK_M)
    _face(d, SK_M, hair=(25, 18, 15), mouth=(250, 250, 250))
    return im
def street_dance_stranger_5():  # smiling young man, black/purple/gold tunic, reaching out a hand
    im, d = canvas(); shadow(d); skin = (110, 70, 50)
    legs(d, BLK, shoe=GOLD_D); R(d, 10, 18, 21, 35, BLK); R(d, 13, 18, 18, 35, PURPLE); R(d, 10, 29, 21, 30, GOLD)
    R(d, 7, 19, 9, 30, skin); R(d, 22, 21, 28, 23, skin); R(d, 28, 20, 30, 24, skin)
    _face(d, skin, hair=(20, 15, 12), mouth=(250, 250, 250))
    return im
# Bar drinkers (joetopia-art-src/bar/drinker_1..4.jpg): strangers who want to share a drink. Fully dressed at sprite scale.
def _goblet(d, x, y): R(d, x, y, x + 3, y + 2, GOLD); R(d, x + 1, y + 3, x + 2, y + 4, GOLD_D); P(d, [(x + 1, y)], (150, 30, 90))
def street_bar_drinker_1():  # short black hair, cream dress, goblet held out, blue goblin plush backpack
    im, d = canvas(); shadow(d); skin = (225, 180, 145)
    legs(d, skin, top=36, shoe=GOLD_D); R(d, 10, 18, 21, 36, (235, 225, 200)); R(d, 4, 16, 8, 26, (60, 140, 200))
    R(d, 22, 21, 27, 23, skin); _goblet(d, 27, 18); _face(d, skin, hair=(20, 18, 30), mouth=(250, 250, 250))
    return im
def street_bar_drinker_2():  # sad old bearded man, white toga, goblet
    im, d = canvas(); shadow(d)
    legs(d, WHITE, shoe=(120, 90, 60)); R(d, 9, 18, 22, 36, WHITE); R(d, 9, 18, 22, 19, GOLD)
    R(d, 22, 22, 25, 25, SK_L); _goblet(d, 24, 20); _face(d, SK_L, hair=(200, 200, 200), beard=(210, 210, 210)); P(d, [(12, 9), (19, 9)], (120, 120, 120))
    return im
def street_bar_drinker_3():  # smiling bald man, white toga with gold trim, offering a goblet
    im, d = canvas(); shadow(d); skin = (90, 55, 40)
    legs(d, WHITE, shoe=GOLD_D); R(d, 8, 18, 23, 36, WHITE); R(d, 8, 18, 23, 19, GOLD); R(d, 12, 19, 13, 36, GOLD)
    R(d, 23, 21, 28, 23, skin); _goblet(d, 27, 18); _face(d, skin, mouth=(250, 250, 250))
    return im
def street_bar_drinker_4():  # red hair, swirl face paint, goblet (covered: emerald wrap dress)
    im, d = canvas(); shadow(d); skin = (235, 190, 160); hair = (190, 50, 30)
    legs(d, skin, top=36, shoe=GOLD_D); R(d, 10, 18, 21, 36, (30, 110, 80)); R(d, 10, 18, 21, 19, GOLD)
    R(d, 22, 20, 25, 23, skin); _goblet(d, 24, 17); _face(d, skin, hair=hair); R(d, 8, 5, 10, 18, hair); R(d, 21, 5, 23, 18, hair); P(d, [(12, 12), (19, 12)], (255, 255, 255))
    return im

def street_bar_drinker_5():  # blonde, blue circuit tattoos, dark-blue high-collar outfit, glowing goblet
    im, d = canvas(); shadow(d); skin = (240, 205, 175); hair = (235, 205, 110); blue = (60, 170, 255)
    legs(d, (25, 35, 80), top=36, shoe=(20, 25, 60)); R(d, 10, 17, 21, 36, (25, 35, 90)); R(d, 13, 16, 18, 18, (25, 35, 90))
    R(d, 22, 20, 25, 23, skin); _goblet(d, 24, 17); P(d, [(25, 16), (26, 15)], blue); _face(d, skin, hair=hair)
    R(d, 8, 5, 10, 19, hair); R(d, 21, 5, 23, 19, hair); P(d, [(15, 8), (16, 9), (13, 13), (18, 13)], blue)
    return im
def street_bar_drinker_6():  # scarred man, yellow eyes, white coat, green goblet with a pill
    im, d = canvas(); shadow(d); skin = (150, 120, 95); green = (90, 255, 90)
    legs(d, (40, 35, 30), top=36, shoe=(20, 20, 20)); R(d, 9, 17, 22, 38, WHITE); R(d, 14, 17, 17, 30, (40, 60, 40))
    R(d, 22, 20, 25, 23, skin); _goblet(d, 24, 17); P(d, [(24, 16), (25, 16), (26, 16)], green); P(d, [(25, 15)], (250, 250, 250))
    _face(d, skin, hair=(25, 25, 25)); P(d, [(13, 11), (18, 11)], (255, 220, 0)); P(d, [(12, 13), (13, 14)], (110, 70, 60))
    return im

# ---- named talk NPCs (art: joetopia-art-src/npc/<file>.jpg) ----
def lantern_poet():  # Miriam Inkwell: curly salt-and-pepper bun, gold glasses + earrings, paint-splattered cream overalls, glowing phone
    im, d = canvas(); shadow(d); skin = (190, 140, 105); hair = (95, 90, 92); over = (232, 225, 205)
    legs(d, over, top=34, shoe=(70, 50, 40)); R(d, 10, 20, 21, 36, over); R(d, 11, 19, 12, 22, over); R(d, 19, 19, 20, 22, over)
    R(d, 12, 19, 19, 23, (225, 225, 230))  # white top under the bib
    arms(d, skin, skin, 19, 29); R(d, 20, 27, 24, 29, skin); R(d, 18, 25, 21, 28, (60, 45, 30)); P(d, [(19, 26), (20, 26)], (255, 210, 90))  # phone glow
    P(d, [(12, 27), (17, 30), (14, 33), (19, 35), (11, 38), (16, 41), (13, 24)], (220, 80, 60))
    P(d, [(15, 28), (12, 32), (18, 38), (14, 42), (19, 31)], (60, 130, 200)); P(d, [(16, 35), (11, 34), (20, 41)], (240, 190, 60))
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6)
    R(d, 10, 4, 21, 8, hair); R(d, 9, 6, 11, 14, hair); R(d, 20, 6, 22, 13, hair); R(d, 12, 1, 19, 4, hair)  # curly bun
    P(d, [(11, 5), (14, 2), (17, 3), (20, 5), (10, 9)], (185, 185, 190))  # grey streaks
    P(d, [(12, 12), (13, 12), (14, 12), (17, 12), (18, 12), (19, 12), (15, 13), (16, 13)], (200, 160, 70))  # gold glasses
    P(d, [(10, 15), (21, 15), (10, 16), (21, 16)], (230, 180, 60))  # earrings
    return im

GOLD2, TEAL = (225, 185, 70), (40, 230, 190)
def dealer_tamar():  # Tamar Glitch: long black curls, tattooed face with glowing orange circuit lines, black armour traced in gold
    im, d = canvas(); shadow(d); skin = (160, 110, 80); arm = (28, 26, 32); hair = (20, 16, 18)
    legs(d, arm, shoe=(15, 12, 15)); R(d, 10, 19, 21, 36, arm); arms(d, arm, skin)
    R(d, 6, 18, 10, 22, (45, 42, 50)); R(d, 21, 18, 25, 22, (45, 42, 50))  # shoulder plates
    P(d, [(12, 22), (13, 24), (14, 26), (18, 23), (19, 25), (16, 29), (12, 31), (19, 32), (7, 19), (24, 19), (15, 34)], (240, 150, 50))
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6)
    R(d, 9, 3, 22, 7, hair); R(d, 8, 6, 11, 22, hair); R(d, 20, 6, 23, 21, hair)  # curls past the shoulders
    P(d, [(13, 15), (14, 16), (18, 14), (17, 16), (19, 12)], (245, 150, 50)); P(d, [(11, 16), (20, 16)], GOLD2)  # face tattoo, earrings
    return im

def shamgar():  # Shamgar the Wall: huge bearded man, dark headwrap with a gold band, leather-and-iron armour, big wooden staff
    im, d = canvas(); shadow(d); skin = SK_T; arm = (70, 55, 40)
    legs(d, (55, 45, 35), shoe=(35, 25, 20)); R(d, 9, 19, 22, 36, arm); R(d, 9, 26, 22, 28, (40, 35, 30)); arms(d, arm, skin)
    R(d, 6, 18, 10, 22, (90, 90, 95)); R(d, 21, 18, 25, 22, (90, 90, 95))
    R(d, 26, 4, 27, 44, (120, 85, 50)); R(d, 24, 30, 26, 32, skin)  # staff in hand
    _face(d, skin, 5, hair=(45, 38, 32), beard=(55, 45, 38)); R(d, 10, 4, 21, 5, GOLD2)
    return im

def dr_spore():  # Dr. Nyxariel Spore: wild grey-violet hair, grin, white lab coat over a purple shirt, glowing mushroom flask
    im, d = canvas(); shadow(d); skin = SK_M; coat = (225, 220, 210)
    legs(d, (50, 45, 60)); R(d, 9, 19, 22, 38, coat); R(d, 14, 19, 17, 34, (110, 60, 150)); arms(d, coat, skin)
    R(d, 22, 30, 25, 34, (120, 255, 200)); P(d, [(23, 29), (24, 29)], (200, 120, 255))  # flask
    _face(d, skin, 6, beard=None, mouth=(240, 240, 235))
    R(d, 7, 1, 24, 6, (150, 140, 175)); R(d, 6, 4, 10, 13, (150, 140, 175)); R(d, 21, 4, 25, 13, (150, 140, 175))
    P(d, [(8, 0), (12, 0), (19, 0), (23, 1), (5, 8), (26, 9)], (175, 165, 200))
    return im

def priscilla_talk():  # Old Priscilla: white-grey bun, brown cardigan, cream apron, holding a pie
    im, d = canvas(); shadow(d); skin = SK_L; hair = (205, 205, 210)
    legs(d, (90, 70, 60), top=38, shoe=(60, 40, 30)); R(d, 9, 19, 22, 40, (120, 85, 60)); R(d, 11, 21, 20, 40, (235, 225, 200)); arms(d, (120, 85, 60), skin)
    R(d, 11, 28, 20, 31, (200, 140, 70)); R(d, 12, 27, 19, 27, (225, 175, 100))  # pie
    _face(d, skin, 6, mouth=(190, 110, 100)); R(d, 10, 4, 21, 8, hair); R(d, 13, 1, 18, 4, hair)
    return im

def barnabas_talk():  # Barnabas the Smith: short grey hair, stubble, glowing blue eyes, blue shirt, leather apron, hammer
    im, d = canvas(); shadow(d); skin = SK_M
    legs(d, (55, 45, 40)); R(d, 9, 19, 22, 36, (50, 80, 130)); R(d, 11, 21, 20, 37, (110, 75, 45)); arms(d, (50, 80, 130), skin)
    R(d, 24, 25, 25, 33, (110, 80, 50)); R(d, 23, 23, 27, 25, (120, 120, 130))  # hammer
    _face(d, skin, 6, hair=(150, 145, 140), eyes=(80, 200, 255)); P(d, [(12, 15), (14, 16), (17, 16), (19, 15)], (130, 120, 115))
    return im

def ushapti_smuggler():  # Ushapti smuggler: grey-skinned alien, round dark goggles, robes, crouching with a satchel
    im, d = canvas(); shadow(d); skin = (150, 150, 150); robe = (70, 65, 60)
    legs(d, robe, top=34, bot=43); R(d, 10, 20, 21, 35, robe); arms(d, robe, skin, 21, 31); R(d, 20, 28, 25, 33, (110, 80, 50))
    R(d, 10, 6, 21, 18, skin); R(d, 11, 4, 20, 6, skin); R(d, 13, 18, 18, 20, skin)
    R(d, 11, 10, 14, 12, BLK); R(d, 17, 10, 20, 12, BLK); R(d, 14, 10, 17, 10, BLK)  # goggles
    return im

def draconian_bodyguard():  # Draconian bodyguard: bronze-scaled lizard in dark gold-trimmed armour
    im, d = canvas(); shadow(d); _lizard(d, 0, 0, armor=(60, 50, 40)); P(d, [(12, 24), (19, 24), (15, 30)], GOLD2)
    return im

def ash_cultist():  # Ash cultist: grey hood and robes, green-glowing gas mask
    im, d = canvas(); shadow(d); robe = (110, 110, 112)
    R(d, 9, 19, 22, 44, robe); arms(d, robe, (90, 90, 92)); R(d, 11, 45, 20, 46, (60, 60, 60))
    R(d, 9, 2, 22, 18, robe); R(d, 11, 6, 20, 16, (40, 40, 42)); P(d, [(13, 9), (18, 9)], (200, 230, 220))
    R(d, 13, 12, 18, 16, (25, 35, 30)); P(d, [(14, 13), (17, 13), (15, 15), (16, 15)], (90, 255, 140))  # mask
    return im

def enlil_ka():  # Enlil-Ka: long white beard and hair, horned gold crown, white-and-gold robes, glowing tablet
    im, d = canvas(); shadow(d); skin = SK_M; robe = (235, 230, 215)
    _robed(d, robe, skin, sash=GOLD2); arms(d, robe, skin)
    R(d, 22, 27, 26, 33, (90, 190, 255))  # holo tablet
    _face(d, skin, 6, hair=(240, 240, 240), beard=(240, 240, 240)); R(d, 11, 18, 20, 24, (240, 240, 240))
    R(d, 10, 2, 21, 5, GOLD2); P(d, [(9, 1), (8, 0), (22, 1), (23, 0)], GOLD2)
    return im

def marduk_ra():  # Marduk-Ra: black beard, tall gold crown, green-and-gold armour, staff with a teal glowing head
    im, d = canvas(); shadow(d); skin = SK_T; arm = (40, 60, 50)
    legs(d, arm, shoe=(90, 70, 30)); R(d, 9, 19, 22, 36, arm); P(d, [(11, 22), (14, 24), (17, 22), (20, 24), (15, 28), (12, 32), (19, 32)], GOLD2)
    arms(d, arm, skin); R(d, 25, 6, 26, 44, GOLD2); R(d, 24, 2, 27, 5, TEAL)
    _face(d, skin, 6, beard=(25, 20, 18)); R(d, 11, 0, 20, 6, GOLD2); P(d, [(15, 2), (16, 2)], TEAL)
    return im

def inanna_shar():  # Inanna-Shar: long black hair, tall gold crown, teal cyber eyepiece, gold armour, a pistol in each hand
    im, d = canvas(); shadow(d); skin = SK_M; arm = (150, 115, 45)
    legs(d, (40, 35, 30), shoe=(120, 90, 35)); R(d, 10, 19, 21, 36, arm); P(d, [(13, 23), (18, 23), (15, 27), (12, 31), (19, 31)], TEAL)
    arms(d, arm, skin); R(d, 4, 30, 8, 32, (60, 60, 65)); R(d, 23, 30, 27, 32, (60, 60, 65))
    head(d, skin, 6); R(d, 9, 6, 11, 22, BLK); R(d, 20, 6, 22, 22, BLK); R(d, 11, 0, 20, 7, GOLD2); R(d, 16, 12, 19, 14, TEAL)
    return im

def ushapti_broker():  # Ushapti broker: grey alien, huge black eyes, dark suit with gold collar chains
    im, d = canvas(); shadow(d); skin = (165, 165, 168); suit = (30, 30, 34)
    legs(d, suit, shoe=BLK); R(d, 10, 21, 21, 36, suit); arms(d, suit, skin, 21, 31); P(d, [(12, 22), (13, 23), (18, 23), (19, 22), (15, 24), (16, 24)], GOLD2)
    R(d, 9, 3, 22, 15, skin); R(d, 11, 15, 20, 18, skin); R(d, 14, 18, 17, 21, skin)
    R(d, 10, 9, 14, 12, BLK); R(d, 17, 9, 21, 12, BLK)
    return im

def under_boss():  # Big Jehoshaphat: giant laughing man, long white beard and hair, cream robe with purple-and-gold sash, glowing purple tablet
    im, d = canvas(); shadow(d); skin = SK_M; robe = (230, 220, 190)
    R(d, 7, 18, 24, 44, robe); R(d, 6, 30, 25, 44, robe); R(d, 13, 28, 18, 44, (95, 50, 130)); P(d, [(13, 28), (15, 28), (17, 28), (14, 34), (16, 38)], GOLD2)
    R(d, 4, 19, 7, 30, robe); R(d, 24, 19, 27, 30, robe); R(d, 9, 24, 22, 28, (70, 30, 110)); P(d, [(12, 25), (15, 26), (19, 25), (17, 27)], (200, 120, 255))
    R(d, 9, 45, 13, 46, (110, 75, 40)); R(d, 18, 45, 22, 46, (110, 75, 40))
    _face(d, skin, 4, hair=(235, 235, 235), beard=(240, 240, 240), mouth=(120, 40, 40)); R(d, 9, 4, 11, 16, (235, 235, 235)); R(d, 20, 4, 22, 16, (235, 235, 235))
    return im

def scale_veteran():  # Ssarru-Kin: scarred grey lizard-skinned brute, amber eyes, white robe with gold trim over green scales, gold claws, holstered pistol
    im, d = canvas(); shadow(d); skin = (95, 98, 95); robe = (215, 210, 195)
    R(d, 8, 18, 23, 44, robe); R(d, 13, 18, 18, 30, (70, 100, 60)); P(d, [(x, y) for x in (9, 22) for y in range(20, 44, 3)], (160, 120, 60))
    R(d, 4, 19, 8, 32, skin); R(d, 23, 19, 27, 32, skin); P(d, [(4, 33), (6, 34), (8, 33), (23, 33), (25, 34), (27, 33)], GOLD2)  # gold claws
    R(d, 18, 28, 21, 33, BLK); R(d, 9, 45, 13, 46, skin); R(d, 18, 45, 22, 46, skin)
    head(d, skin, 5, eyes=(255, 170, 40)); R(d, 13, 17, 18, 18, skin); P(d, [(12, 8), (13, 9), (14, 10), (18, 13), (19, 14)], (60, 50, 50))  # scars
    return im

def thornback_alpha():  # Thornback Alpha: grey wolf with bone thorns down its spine, vine collar, green gem, purple ribbons
    im, d = canvas(); shadow(d); fur = (95, 95, 100); dark = (55, 55, 62)
    R(d, 9, 24, 23, 34, fur); R(d, 10, 34, 12, 44, dark); R(d, 20, 34, 22, 44, dark); R(d, 14, 33, 16, 43, fur); R(d, 17, 33, 19, 43, fur)
    R(d, 10, 12, 21, 23, fur); P(d, [(10, 9), (11, 10), (11, 11), (21, 9), (20, 10), (20, 11)], dark)  # ears
    R(d, 13, 19, 18, 23, (170, 170, 175)); R(d, 15, 21, 16, 22, BLK); P(d, [(12, 15), (13, 15), (18, 15), (19, 15)], (90, 255, 90))
    P(d, [(9, 11), (8, 14), (22, 11), (23, 14), (8, 20), (24, 20), (8, 26), (24, 26), (12, 8), (19, 8)], (220, 215, 195))  # thorns
    R(d, 10, 24, 21, 25, (60, 110, 50)); R(d, 14, 26, 17, 30, (80, 255, 110)); P(d, [(9, 26), (9, 28), (22, 26), (22, 29)], (130, 70, 170))
    return im

# ---- PLACEHOLDER sprites (v1.6): simple colour-matched figures for the generated placeholder portraits in
# joetopia-art-src/placeholder/ (see PLACEHOLDER_ART in tools/make-encounter-art.py). Swap with a hand-drawn sprite any time.
def _ph(skin, robe, hair=None, accent=None, beard=None, eyes=(20, 20, 30), hat=None, hood=None, alien=False, ghost=False):
    im, d = canvas(); shadow(d)
    if ghost: d.polygon([(9, 19), (22, 19), (25, 44), (6, 44)], fill=robe + (210,))
    else: _robed(d, robe, skin, sash=accent, hem=accent)
    R(d, 6, 20, 9, 32, robe); R(d, 22, 20, 25, 32, robe); R(d, 6, 33, 9, 34, skin); R(d, 22, 33, 25, 34, skin)
    if alien:
        R(d, 10, 3, 21, 14, skin); R(d, 12, 15, 19, 17, skin); R(d, 11, 8, 14, 11, BLK); R(d, 17, 8, 20, 11, BLK)
    else:
        _face(d, skin, 5, hair=hair, beard=beard, eyes=eyes)
    if hood: R(d, 9, 2, 22, 5, hood); R(d, 9, 3, 10, 17, hood); R(d, 21, 3, 22, 17, hood)
    if hat == 'crown': P(d, [(x, 2) for x in (11, 13, 15, 17, 19)], GOLD2); R(d, 11, 3, 20, 4, GOLD2)
    if hat == 'foil': d.polygon([(15, -4), (10, 4), (21, 4)], fill=(200, 205, 215))
    return im
_PH = {
    'spire_patron': dict(skin=SK_L, robe=(225, 205, 160), hair=(150, 70, 40), accent=GOLD2),
    'chrome_broker': dict(skin=(150, 155, 165), robe=(190, 190, 215), accent=TEAL, alien=True),
    'zipporah': dict(skin=SK_T, robe=(235, 80, 160), hair=(30, 20, 20), accent=GOLD2),
    'ninsun': dict(skin=(140, 145, 150), robe=(30, 30, 40), accent=NEONP, alien=True),
    'methuselah': dict(skin=SK_M, robe=(130, 90, 50), hair=(230, 230, 230), beard=(235, 235, 235), accent=GOLD2),
    'jezebel': dict(skin=SK_L, robe=(60, 40, 90), hair=BLK, accent=TEAL),
    'ezra': dict(skin=SK_T, robe=(150, 200, 40), hair=(25, 20, 20), accent=GOLD2),
    'grey_acolyte': dict(skin=SK_M, robe=(150, 145, 135), accent=GOLD2),
    'hagar': dict(skin=SK_L, robe=(200, 185, 150), hair=(225, 200, 130)),
    'asher': dict(skin=SK_T, robe=(210, 170, 80), hair=(40, 30, 25)),
    'dj_meph': dict(skin=SK_D, robe=(240, 240, 240), beard=(30, 25, 25), hat='crown', accent=GOLD2),
    'keziah': dict(skin=SK_L, robe=(110, 60, 170), hair=(200, 200, 215), accent=TEAL),
    'boaz': dict(skin=SK_D, robe=(230, 120, 30), accent=(60, 50, 40)),
    'lilith_spin': dict(skin=SK_L, robe=(35, 35, 90), hair=(25, 20, 35), accent=TEAL),
    'delilah': dict(skin=SK_T, robe=(150, 25, 40), hair=BLK, accent=GOLD2),
    'jonah': dict(skin=SK_M, robe=(30, 110, 110), hair=(40, 30, 25), accent=GOLD2),
    'salome': dict(skin=SK_L, robe=(170, 110, 220), hair=(240, 150, 200), accent=TEAL),
    'gideon': dict(skin=(90, 110, 80), robe=(25, 25, 30), eyes=(255, 170, 40), accent=(60, 60, 70)),
    'naamah': dict(skin=SK_T, robe=(40, 70, 40), hair=(30, 25, 25), accent=(230, 150, 255)),
    'jojo_neon': dict(skin=SK_M, robe=(220, 180, 60), hair=(230, 230, 230), accent=NEONP),
    'princess_zillah': dict(skin=SK_L, robe=(190, 230, 200), hair=(200, 170, 230), accent=(240, 150, 190)),
    'doctor_conspiracy': dict(skin=SK_L, robe=(150, 150, 160), hair=(200, 200, 205), beard=(205, 205, 205), hat='foil'),
    'azazel': dict(skin=SK_L, robe=(25, 20, 25), hair=(150, 40, 30), accent=GOLD2),
    'vashti': dict(skin=SK_T, robe=(235, 230, 215), hair=BLK, accent=GOLD2),
    'local': dict(skin=SK_T, robe=(150, 130, 100), hair=BLK, accent=GOLD_D),
    'enemy_bandit': dict(skin=SK_M, robe=(30, 30, 35), hood=(25, 25, 30)),
    'enemy_guard': dict(skin=(60, 60, 65), robe=(55, 55, 60), eyes=(255, 140, 40), hood=(45, 45, 50), accent=(255, 140, 40)),
    'enemy_skeleton': dict(skin=(220, 215, 200), robe=(70, 65, 60), eyes=(180, 100, 255)),
    'enemy_wraith': dict(skin=(120, 120, 125), robe=(90, 90, 95), eyes=(255, 140, 40), hood=(70, 70, 75), ghost=True),
    'enemy_morvane': dict(skin=(150, 150, 140), robe=(40, 35, 30), eyes=TEAL, hat='crown', accent=GOLD2),
    'enemy_matriarch': dict(skin=(225, 220, 225), robe=(25, 22, 30), hair=(235, 235, 240), hood=(200, 200, 210), eyes=(170, 90, 255), hat='crown'),
}
for _k, _kw in _PH.items(): globals()[_k] = (lambda kw: (lambda: _ph(**kw)))(_kw)
_matriarch_body = enemy_matriarch
def enemy_matriarch():  # Hollow Matriarch: hooded white-haired queen over a black spider body
    im = _matriarch_body(); d = ImageDraw.Draw(im)
    for y in (30, 34, 38, 42): R(d, 2, y, 7, y, (40, 35, 45)); R(d, 24, y, 29, y, (40, 35, 45))
    d.ellipse([8, 32, 23, 45], fill=(30, 26, 34)); return im
def enemy_wolf():  # Ash Wolf: grey wolf with orange eyes
    im, d = canvas(); shadow(d); fur = (105, 105, 110); dark = (60, 60, 66)
    R(d, 9, 24, 23, 34, fur); R(d, 10, 34, 12, 44, dark); R(d, 20, 34, 22, 44, dark); R(d, 14, 33, 16, 43, fur); R(d, 17, 33, 19, 43, fur)
    R(d, 10, 12, 21, 23, fur); P(d, [(10, 9), (11, 10), (11, 11), (21, 9), (20, 10), (20, 11)], dark)
    R(d, 13, 19, 18, 23, (170, 170, 175)); R(d, 15, 21, 16, 22, BLK); P(d, [(12, 15), (13, 15), (18, 15), (19, 15)], (255, 150, 40)); return im
def enemy_spider():  # Cave Spider: big black spider with purple eyes
    im, d = canvas(); shadow(d); c = (30, 26, 36)
    for i, y in enumerate((26, 30, 34, 38)):
        d.line([(15, 32), (2, y - 6), (1, y + 6)], fill=c, width=1); d.line([(16, 32), (29, y - 6), (30, y + 6)], fill=c, width=1)
    d.ellipse([9, 28, 22, 44], fill=c); d.ellipse([10, 20, 21, 30], fill=(40, 34, 48))
    P(d, [(13, 24), (15, 23), (16, 23), (18, 24), (14, 26), (17, 26)], (190, 100, 255)); return im
PLACEHOLDER_SPRITES = list(_PH) + ['enemy_wolf', 'enemy_spider', 'dj_meph_back']
dj_meph_back = _PH and globals()['dj_meph']

# ---- v1.7 / text 2.7.6: Royal Crypt + Eden placeholders, and the flower girl / Ash Wolf (real art) map sprites.
def _stone(d, x0, y0, x1, y1, c=(120, 118, 125)): R(d, x0, y0, x1, y1, c); R(d, x0, y0, x1, y0, tuple(min(255, v + 40) for v in c))
def _tomb(cross=GOLD2, lid=(150, 145, 150)):
    im, d = canvas(); shadow(d); _stone(d, 5, 30, 26, 44, (95, 92, 100)); _stone(d, 4, 27, 27, 30, lid)
    R(d, 15, 10, 16, 26, cross); R(d, 11, 14, 20, 15, cross); return im
def _tree(trunk=(90, 60, 35), leaf=(60, 150, 70), fruit=None, glow=None):
    im, d = canvas(); shadow(d)
    if glow: d.ellipse([1, 0, 30, 30], fill=glow + (70,))
    R(d, 14, 26, 17, 44, trunk); d.ellipse([4, 4, 27, 30], fill=leaf)
    for x, y in ((9, 12), (19, 10), (14, 20), (22, 19), (8, 21)):
        if fruit: R(d, x, y, x + 1, y + 1, fruit)
    return im
def royal_crypt(): return _tomb(GOLD2, (170, 160, 120))
def thaddeus_tomb():
    im = _tomb(GOLD2, (190, 175, 120)); d = ImageDraw.Draw(im); P(d, [(x, 25) for x in (9, 12, 15, 18, 21)], GOLD2); return im
def crypt_grave():
    im, d = canvas(); shadow(d); d.ellipse([9, 12, 22, 24], fill=(130, 128, 135)); R(d, 9, 18, 22, 42, (130, 128, 135))
    R(d, 12, 22, 19, 22, (70, 70, 75)); R(d, 12, 26, 19, 26, (70, 70, 75)); R(d, 6, 42, 25, 44, (60, 90, 50)); P(d, [(8, 41), (23, 41)], (240, 220, 90)); return im
def eden_garden(): return _tree((110, 80, 45), (90, 200, 110), (255, 240, 150), (255, 240, 180))
def tree_knowledge(): return _tree((70, 45, 30), (40, 110, 60), (200, 30, 40))
def tree_life(): return _tree((200, 190, 160), (190, 230, 255), (255, 250, 210), (210, 235, 255))
def ending_thaddeus(): return _ph(skin=SK_L, robe=(130, 30, 50), hair=(120, 90, 60), beard=(130, 100, 70), hat='crown', accent=GOLD2)
def enemy_flaming_sword():
    im, d = canvas(); shadow(d); d.polygon([(15, 0), (9, 30), (22, 30)], fill=(255, 140, 30, 150))
    R(d, 15, 2, 16, 32, (255, 230, 150)); R(d, 10, 32, 21, 33, GOLD2); R(d, 15, 34, 16, 41, (120, 70, 40)); return im
def enemy_serpent():
    im, d = canvas(); shadow(d); c = (60, 140, 60)
    for x, y in ((8, 42), (12, 38), (18, 36), (22, 32), (18, 27), (13, 24), (12, 18)): d.ellipse([x - 4, y - 3, x + 4, y + 3], fill=c)
    d.ellipse([9, 9, 20, 18], fill=(70, 160, 70)); P(d, [(12, 12), (17, 12)], (255, 220, 40)); R(d, 14, 17, 15, 20, (220, 40, 60)); return im
def street_flower_girl(): return _ph(skin=SK_L, robe=(200, 40, 50), hair=(150, 90, 50), hood=(200, 30, 40), accent=(250, 240, 120))
def street_flower_girl_blue(): return _ph(skin=SK_L, robe=(40, 80, 200), hair=(150, 90, 50), hood=(40, 70, 200), accent=(250, 250, 250))
def _hood_wolf(fur, hood):
    im = enemy_wolf()
    if fur != (105, 105, 110):  # recolour the grey Ash Wolf (white wolf under the blue hood)
        px = im.load(); light = tuple(min(255, v - 50) for v in fur)
        for x in range(W):
            for y in range(H):
                if px[x, y][:3] == (105, 105, 110): px[x, y] = fur + (255,)
                elif px[x, y][:3] == (60, 60, 66): px[x, y] = light + (255,)
    d = ImageDraw.Draw(im); R(d, 9, 9, 22, 12, hood); R(d, 9, 9, 10, 20, hood); R(d, 21, 9, 22, 20, hood); return im
def enemy_ash_wolf_red_hood(): return _hood_wolf((105, 105, 110), (200, 30, 40))
def enemy_ash_wolf_blue_hood():
    im = _hood_wolf((230, 230, 235), (40, 70, 200)); return im
_PH17 = {
    'enemy_evil_spirit': dict(skin=(200, 205, 230), robe=(150, 160, 210), eyes=(140, 255, 255), ghost=True),
    'enemy_zombie_goblin': dict(skin=(120, 150, 100), robe=(80, 70, 60), eyes=(230, 230, 120)),
    'enemy_graverobbers': dict(skin=SK_M, robe=(70, 60, 50), hood=(50, 45, 40), accent=(160, 140, 90)),
    'enemy_possessed_man': dict(skin=SK_T, robe=(90, 80, 70), hair=(40, 30, 25), beard=(40, 30, 25), eyes=(255, 60, 40)),
    'enemy_necromancer': dict(skin=(200, 195, 190), robe=(30, 20, 40), hood=(25, 15, 35), eyes=(140, 255, 120), accent=(140, 255, 120)),
    'enemy_vampire': dict(skin=(235, 230, 235), robe=(20, 15, 20), hair=BLK, eyes=(230, 30, 40), accent=(160, 20, 30)),
    'draconian_true': dict(skin=(70, 120, 70), robe=(40, 40, 45), eyes=(255, 200, 40), alien=True),
    'ushapti_true': dict(skin=(150, 155, 165), robe=(60, 60, 80), eyes=(120, 220, 255), alien=True),
}
for _k, _kw in _PH17.items(): globals()[_k] = (lambda kw: (lambda: _ph(**kw)))(_kw)
V17_SPRITES = list(_PH17) + ['royal_crypt', 'thaddeus_tomb', 'crypt_grave', 'eden_garden', 'tree_knowledge', 'tree_life', 'ending_thaddeus',
    'enemy_flaming_sword', 'enemy_serpent', 'street_flower_girl', 'street_flower_girl_blue', 'enemy_ash_wolf_red_hood', 'enemy_ash_wolf_blue_hood']

# ---- v1.8 / text 2.7.7: Babylon district backdrops (scene placeholders): a tiny black-and-gold tower with a neon sign.
def _district(neon, roof=GOLD2, wall=(30, 26, 36)):
    im, d = canvas(); shadow(d); R(d, 8, 14, 23, 44, wall); R(d, 11, 6, 20, 13, wall); R(d, 13, 2, 18, 5, roof)
    R(d, 8, 14, 23, 15, roof); R(d, 11, 6, 20, 7, roof); R(d, 10, 20, 21, 23, neon)
    for y in (28, 34): P(d, [(11, y), (15, y), (19, y)], (255, 220, 120))
    R(d, 14, 39, 17, 44, (10, 8, 12)); return im
_DIST = {'district_spire': (255, 200, 80), 'district_chrome': (80, 220, 255), 'district_lantern': (255, 150, 60), 'district_scale': (220, 40, 50),
         'district_under': (170, 90, 255), 'district_core': (255, 60, 200), 'district_neon_abyss': (230, 80, 255), 'district_docks': (120, 160, 255)}
for _k, _c in _DIST.items(): globals()[_k] = (lambda c: (lambda: _district(c)))(_c)
V18_SPRITES = list(_DIST)

# ---- v1.9 / text 2.7.8: Pastor Evelyn, missionary to the Toadstool Forest (real art: joetopia-art-src/npc/evelyn.jpg)
def evelyn():  # red braid, pith helmet, khaki safari dress, belt pouches, black Bible
    im, d = canvas(); shadow(d); skin = (235, 200, 175); khaki = (165, 150, 105); hair = (170, 70, 35); helmet = (200, 180, 130)
    legs(d, skin, top=34, shoe=(185, 170, 130)); R(d, 10, 19, 21, 35, khaki); arms(d, skin, skin)
    R(d, 10, 27, 21, 28, (215, 210, 195)); R(d, 9, 28, 11, 31, (215, 210, 195))  # belt + pouch
    R(d, 19, 22, 24, 28, (25, 22, 20)); P(d, [(19, 22), (24, 22)], (200, 170, 70))  # Bible
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6, eyes=(70, 110, 90))
    R(d, 20, 9, 21, 22, hair); P(d, [(20, 23), (21, 23)], hair)  # braid over the shoulder
    R(d, 8, 5, 23, 6, helmet); R(d, 11, 1, 20, 5, helmet); R(d, 11, 4, 20, 4, (120, 105, 75))  # pith helmet + band
    return im
def street_lost_explorer():  # shaved head, gold neck coils, torn green dress, white boots
    im, d = canvas(); shadow(d); skin = (150, 100, 70); green = (60, 120, 70); gold = (225, 185, 60)
    legs(d, skin, top=34, shoe=(235, 235, 230)); R(d, 10, 19, 21, 35, green); arms(d, skin, skin)
    R(d, 10, 27, 21, 27, (110, 80, 50))  # canteen belt
    R(d, 13, 18, 18, 19, gold); head(d, skin, 6, eyes=(50, 35, 25))
    return im
def street_crypt_explorer():  # dark ponytail, gold earrings, khaki, magnifying glass
    im, d = canvas(); shadow(d); skin = (225, 185, 150); khaki = (175, 155, 110); hair = (40, 28, 22)
    legs(d, skin, top=34, shoe=(90, 65, 40)); R(d, 10, 19, 21, 35, khaki); arms(d, skin, skin)
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6, eyes=(60, 45, 30))
    R(d, 10, 3, 21, 6, hair); R(d, 14, 0, 17, 3, hair)  # hair + high ponytail
    R(d, 22, 22, 25, 25, (200, 170, 70)); R(d, 23, 23, 24, 24, (190, 220, 235))  # magnifying glass
    return im
def street_under_explorer():  # blonde bob, sailor cap, round glasses, tablet
    im, d = canvas(); shadow(d); skin = (240, 205, 180); navy = (40, 55, 95); hair = (230, 200, 110)
    legs(d, skin, top=34, shoe=(30, 30, 35)); R(d, 10, 19, 21, 35, navy); arms(d, skin, skin)
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6, eyes=(40, 40, 40))
    R(d, 9, 6, 11, 14, hair); R(d, 20, 6, 22, 14, hair); R(d, 10, 2, 21, 5, (240, 240, 240)); R(d, 10, 5, 21, 5, navy)  # bob + sailor cap
    R(d, 21, 23, 25, 28, (20, 20, 25)); R(d, 22, 24, 24, 27, (80, 160, 220))  # tablet
    return im
def street_explorers_guild():  # dark curls, pith helmet with red feather, khaki, binoculars, holster
    im, d = canvas(); shadow(d); skin = (215, 165, 130); khaki = (170, 150, 105); hair = (30, 22, 18); helmet = (200, 180, 130)
    legs(d, skin, top=34, shoe=(95, 65, 40)); R(d, 10, 19, 21, 35, khaki); arms(d, skin, skin)
    R(d, 10, 27, 21, 28, (95, 65, 40)); R(d, 19, 28, 21, 32, (95, 65, 40))  # belt + holster
    R(d, 14, 21, 17, 23, (40, 40, 40))  # binoculars
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6, eyes=(70, 50, 35))
    R(d, 8, 7, 10, 16, hair); R(d, 21, 7, 23, 16, hair)  # curls
    R(d, 8, 5, 23, 6, helmet); R(d, 11, 1, 20, 5, helmet); R(d, 11, 4, 20, 4, (230, 230, 220)); R(d, 7, 0, 9, 4, (200, 40, 40))  # helmet + red feather
    return im
V19_SPRITES = ['evelyn', 'street_lost_explorer', 'street_crypt_explorer', 'street_under_explorer', 'street_explorers_guild']
def _sheeple(fleece, top, pack, flower):  # v1.11 Sheeple girl: cream face, floppy ears, curly wool, fleece jacket, backpack with a flower
    im, d = canvas(); shadow(d); skin = (245, 232, 215); wool = (250, 246, 236)
    legs(d, (90, 80, 75), top=34, shoe=(70, 60, 55)); R(d, 10, 19, 21, 35, fleece); R(d, 13, 20, 18, 27, top); arms(d, fleece, fleece)
    R(d, 5, 20, 9, 30, pack); R(d, 5, 18, 8, 20, flower)  # backpack + flower
    R(d, 13, 18, 18, 19, skin); head(d, skin, 6, eyes=(45, 30, 25))
    R(d, 9, 2, 22, 5, wool); R(d, 8, 4, 9, 8, wool); R(d, 22, 4, 23, 8, wool)  # curly wool
    R(d, 5, 8, 8, 10, skin); R(d, 23, 8, 26, 10, skin)  # floppy ears
    return im
def street_sheeple_drink(): return _sheeple((235, 135, 45), (240, 150, 190), (200, 120, 160), (250, 220, 80))
def street_sheeple_dance(): return _sheeple((30, 30, 34), (190, 30, 40), (40, 40, 44), (210, 30, 50))
V111_SPRITES = ['street_sheeple_drink', 'street_sheeple_dance']


SPRITES = {'robert': robert, 'ramirez': ramirez, 'rob': rob, 'joseph': joseph, 'miranda': miranda,
           'alex': alex, 'sean': sean, 'alec': alec, 'lydia': lydia, 'lantern_poet': lantern_poet,
           **{k: globals()[k] for k in ('dealer_tamar', 'shamgar', 'dr_spore', 'priscilla_talk', 'barnabas_talk', 'ushapti_smuggler',
              'draconian_bodyguard', 'ash_cultist', 'enlil_ka', 'marduk_ra', 'inanna_shar', 'ushapti_broker', 'under_boss', 'scale_veteran', 'thornback_alpha')},
           **{k: globals()[k] for k in PLACEHOLDER_SPRITES},
           **{k: globals()[k] for k in V17_SPRITES},
           **{k: globals()[k] for k in V18_SPRITES},
           **{k: globals()[k] for k in V19_SPRITES},
           **{k: globals()[k] for k in V111_SPRITES},
           'enc_guard': enc_guard, 'enc_preacher': enc_preacher, 'enc_egirl': enc_egirl,
           'enc_trader': enc_trader, 'enc_goblins': enc_goblins, 'enc_fans': enc_fans,
           **{f'street_{k}': globals()[f'street_{k}'] for k in ('punks', 'drunk', 'party_girls', 'beggar', 'geneticist', 'preacher',
              'drone', 'pickpocket', 'megaphone', 'tourist', 'stranger', 'noble', 'creep', 'temptress', 'pirates', 'rats', 'sailor', 'streetwalker', 'kraken',
              'duel', 'angry_local', 'parade', 'fireworks', 'bald_brawl', 'starving_artist', 'tipsy_muse', 'acrobats',
              'courier', 'rude_worker', 'discarded_tech', 'toll_path',
              'runaway_chariot', 'reality_show', 'lost_jewelry', 'charity_gala',
              'reality_pushup', 'reality_blind_date', 'reality_makeup', 'reality_fletcher', 'reality_petyr', 'wizard_couriers', 'adrenochrome',
              'troll', 'weirdo', 'trustworthy_human', 'unicorn', 'pixie', 'gnome', 'unicorn_horn', 'pixie_wings', 'gnome_hat', 'work_jeans',
              'flannel_shirt', 'woodsman_axe', 'unicorn_wand', 'unicorn_sword', 'unicorn_heels',
              'goblin_banger', 'goblin_zapper', 'banger_bandana', 'red_shiv', 'bike_chain', 'stem_bat',
              'goblin_banger_blue', 'goblin_revolver', 'blue_bandana', 'blue_shiv', 'goblin_slingshot', 'big_booma', 'ballistic_hat', 'goblin_unaffiliated', 'bigfoot', 'dance_water', 'dance_dj', 'dance_pickpocket', 'dance_boyfriend', 'dance_drinks',
              'dance_stranger_1', 'dance_stranger_2', 'dance_stranger_3', 'dance_stranger_4', 'dance_stranger_5',
              'bar_drinker_1', 'bar_drinker_2', 'bar_drinker_3', 'bar_drinker_4', 'bar_drinker_5', 'bar_drinker_6')}}
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in SPRITES.items(): fn().save(os.path.join(OUT, name + '.png'))
    print('wrote', len(SPRITES), 'sprites to', os.path.normpath(OUT))
