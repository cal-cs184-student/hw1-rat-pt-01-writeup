"""Generate Berkeley at Night using rectangles and straight-sided polygons."""
from pathlib import Path
import math
import random
import xml.etree.ElementTree as ET

svg = ET.Element('svg', xmlns='http://www.w3.org/2000/svg', width='800', height='800')


def rect(x, y, w, h, color):
    ET.SubElement(svg, 'rect', x=str(x), y=str(y), width=str(w), height=str(h), fill=color)


def polygon(points, color):
    ET.SubElement(svg, 'polygon', points=' '.join(f'{x:.2f},{y:.2f}' for x, y in points), fill=color)


def diamond(x, y, r, color):
    polygon([(x, y-r), (x+r, y), (x, y+r), (x-r, y)], color)


# Solid bands suggest dusk without SVG gradients.
colors = ['#101b38', '#14213e', '#1b2948', '#253151', '#343859',
          '#464160', '#5c4b67', '#75566b', '#916571', '#ad797c']
for i, color in enumerate(colors):
    rect(0, i * 60, 800, 60, color)

# A fixed seed keeps the stars identical each time.
rng = random.Random(184)
for i in range(65):
    x, y = rng.randint(30, 770), rng.randint(25, 420)
    if 340 < x < 480 or (x-640)**2 + (y-145)**2 < 75**2:
        continue
    diamond(x, y, rng.choice([1.2, 1.8, 2.5]), rng.choice(['#b7c5d4', '#e8d6ad']))
for x, y in [(126, 122), (266, 236), (552, 66)]:
    polygon([(x, y-8), (x+2, y-2), (x+8, y), (x+2, y+2),
             (x, y+8), (x-2, y+2), (x-8, y), (x-2, y-2)], '#f5deb1')

# The moon is a twelve-sided polygon, not a circle or curve.
polygon([(640+48*math.cos(i*math.pi/6), 145+48*math.sin(i*math.pi/6))
         for i in range(12)], '#eedbbb')
polygon([(617, 106), (598, 121), (592, 145), (598, 169), (617, 184),
         (608, 152), (609, 128)], '#d0bca2')

# Distant hills and campus roofs.
polygon([(0, 540), (85, 500), (166, 524), (268, 481), (390, 525),
         (530, 480), (652, 512), (740, 470), (800, 490), (800, 650), (0, 650)], '#41465d')
rect(0, 593, 800, 207, '#101f30')
for x, y, w in [(0, 550, 160), (170, 576, 136), (494, 569, 130), (635, 536, 165)]:
    rect(x, y, w, 105, '#243247')
    polygon([(x-8, y), (x+w/2, y-25), (x+w+8, y)], '#18283c')
    for wx in range(x+16, x+w-10, 24):
        rect(wx, y+22, 7, 14, '#c39c6a')
        rect(wx, y+50, 7, 14, '#657080')

# Campanile: narrow stone shaft, clock, open belfry, pyramidal roof.
rect(362, 306, 69, 320, '#d7b78d')
polygon([(431, 306), (460, 318), (460, 626), (431, 626)], '#937e75')
rect(365, 310, 7, 312, '#f1d4a3')
rect(421, 310, 6, 312, '#b3967c')
for y in [380, 454, 528]:
    rect(389, y, 14, 40, '#746f70')
    rect(393, y+4, 6, 32, '#f2c980')
    polygon([(439, y+5), (449, y+9), (449, y+43), (439, y+39)], '#535663')
rect(354, 294, 82, 14, '#f1d1a0')
polygon([(436, 294), (465, 306), (465, 320), (436, 308)], '#ac8e78')
rect(363, 223, 68, 71, '#dec398')
polygon([(431, 223), (460, 235), (460, 306), (431, 294)], '#a88d77')
for x in [372, 393, 414]:
    polygon([(x, 283), (x, 247), (x+5, 238), (x+10, 247), (x+10, 283)], '#293546')
    rect(x+3, 250, 3, 28, '#b89462')
polygon([(440, 290), (440, 253), (445, 247), (451, 257), (451, 295)], '#35404b')
rect(355, 214, 81, 10, '#f5d7a7')
polygon([(436, 214), (466, 227), (460, 237), (431, 224)], '#aa907b')
polygon([(354, 214), (403, 143), (436, 214)], '#7c9999')
polygon([(403, 143), (466, 227), (436, 214)], '#455f70')
rect(402, 130, 3, 17, '#e7c798')
diamond(403.5, 130, 4, '#e7c798')
# Octagonal clock face with rectangular hands.
polygon([(396+18*math.cos(i*math.pi/4), 338+18*math.sin(i*math.pi/4))
         for i in range(8)], '#8b776a')
polygon([(396+15*math.cos(i*math.pi/4), 338+15*math.sin(i*math.pi/4))
         for i in range(8)], '#f6deb0')
rect(395, 325, 2, 14, '#384352')
rect(396, 337, 10, 2, '#384352')
for y, x, w in [(622, 351, 122), (634, 340, 145), (646, 328, 169)]:
    rect(x, y, w, 12, '#aa927e')

# A perspective walkway leads toward the tower.
polygon([(369, 658), (447, 658), (649, 800), (148, 800)], '#46505c')
polygon([(387, 658), (418, 658), (456, 800), (300, 800)], '#69666a')
for y, half_width in [(679, 60), (711, 100), (757, 159)]:
    rect(403-half_width, y, half_width*2, 3, '#929088')

# Angular evergreens frame the architecture.
for x, y, size in [(50, 646, 120), (125, 669, 90), (714, 658, 126), (778, 689, 100)]:
    rect(x-5, y-25, 10, 95, '#0b1928')
    for level in range(3):
        tip = y-size + level*size/4
        half = size*(0.22+level*0.07)
        polygon([(x, tip), (x+half, tip+size*0.55), (x-half, tip+size*0.55)], '#0b1928')

# Low gate-like foreground and warm lamps, with an open central walkway.
for left, right in [(0, 233), (577, 800)]:
    rect(left, 728, right-left, 9, '#091723')
    rect(left, 775, right-left, 9, '#091723')
    for x in range(left+12, right, 18):
        rect(x, 729, 4, 71, '#091723')
        diamond(x+2, 723, 5, '#091723')
for x in [233, 577]:
    rect(x-14, 721, 28, 79, '#253344')
    rect(x-18, 715, 36, 9, '#59606a')
    rect(x-3, 678, 6, 37, '#101e2d')
    rect(x-10, 655, 20, 25, '#e9bb73')
    rect(x-2, 655, 4, 25, '#263444')
    polygon([(x-15, 655), (x, 643), (x+15, 655)], '#182738')
    rect(x-12, 679, 24, 4, '#182738')

ET.indent(svg)
output = Path(__file__).resolve().parents[1] / 'competition.svg'
ET.ElementTree(svg).write(output, encoding='utf-8', xml_declaration=True)
print(output)
