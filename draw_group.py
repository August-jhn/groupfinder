from pgl import GWindow, GImage, GLine, GRect, COLOR_TABLE

from group import*
from math import*

WIDTH = 800

def draw_group(group, r, displacement = 0, colored = True):


    rainbow = ["Red","Orange", "Yellow", "Green","Blue", "Purple","Pink", "White", "skyblue", "coral","aquamarine","forestgreen","magenta", "hotpink", "lime","orchid","olive"]
    """draws group on GWindow in a circular multicolored fashion
    inputs: Group """
    elements = group.get_elements()
    element_poss = []
    pairs = group.get_pairs()
    k = len(elements)
    print(k)
    for i in range(k):
        theta = (2*pi*i)/k
        element_poss.append((r*cos(theta), r*sin(theta)))
    gw = GWindow(WIDTH,WIDTH)
    if colored:
        bg = GRect(WIDTH,WIDTH)
        bg.set_filled(True)
        gw.add(bg)
    for pos in element_poss:
        print(pos)
        gw.add(GRect(pos[0]+250,pos[1]+250,1,1))
    element_indexes = {}
    index = 0
    for e in elements:
        element_indexes[e] = index
        index += 1
    for i in range(k):
        for j in range(k):
            e1 = elements[i]
            e2 = elements[j]
            e3 = pairs[(e1,e2)]
            x1,y1 = element_poss[i]
            x2,y2 = element_poss[j]
            x3,y3 = (element_poss[element_indexes[e3]][0]*displacement,element_poss[element_indexes[e3]][1]*displacement)
            l1 = GLine(x1+WIDTH/2,y1+WIDTH/2,x3+WIDTH/2,y3+WIDTH/2)
            
            
            l2 = GLine(x2+WIDTH/2,y2+WIDTH/2,x3+WIDTH/2,y3+WIDTH/2)
            

            if colored:
                color = rainbow[element_indexes[e3] % 16]
                l1.set_color(color)
                l2.set_color(color)

            gw.add(l1)
            gw.add(l2)
