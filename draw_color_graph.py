from pgl import GWindow, GImage, GLine, GRect, COLOR_TABLE, GLabel

from group import*
from math import*

WIDTH = 800

def draw_graph(group, gen,graph, r, displacement = 0, colored = True):


    rainbow = ["Red","Orange", "Yellow", "Green","Blue", "Purple","Pink", "White", "skyblue", "coral","aquamarine","forestgreen","magenta", "hotpink", "lime","orchid","olive"]
    """draws group on GWindow in a circular multicolored fashion
    inputs: Group """
    elements = group.get_elements()
    gw = GWindow(WIDTH,WIDTH)
    bg = GRect(0,0,WIDTH,WIDTH)
    bg.set_filled(True)
    gw.add(bg)
    poss = {}
    colors = {}
    i = 0
    for e in gen:
        theta = 2*pi*i/len(gen)
        poss[e] = (r*cos(theta),r*sin(theta))
        gw.add(GRect(poss[e][0] + WIDTH/2,poss[e][1]+ WIDTH/2,1,1))
        colors[e] = rainbow[i % len(rainbow)]
        i += 1
        
    others = group.get_elements_set()-gen
    i = 0
    for e in others:
        theta = 2*pi*i/len(others)
        poss[e] = ((r+displacement)*cos(theta),(r+displacement)*sin(theta))
        gw.add(GRect(poss[e][0] + WIDTH/2,poss[e][1]+ WIDTH/2,1,1))
        colors[e] = rainbow[(i + len(gen))% len(rainbow)]
        i += 1
    for e in elements:
        label = GLabel(e)
        label.set_color(colors[e])
        gw.add(label,poss[e][0] + WIDTH/2, poss[e][1] + WIDTH/2)

    for edge in graph:

        line = GLine(poss[edge[0]][0] + WIDTH/2,poss[edge[0]][1]+ WIDTH/2,poss[edge[1]][0]+ WIDTH/2,poss[edge[1]][1]+ WIDTH/2)
        line.set_color(colors[edge[1]])
        gw.add(line)
