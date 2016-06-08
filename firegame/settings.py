import pygame
import os

    #DISPLAY
#resolution
WIN_WIDTH = 900 
WIN_HEIGHT = 500
WIN_CENTER = [WIN_WIDTH/2, WIN_HEIGHT/2]

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

#size parts
GAMESIZE = 20
# map size in objects
X = 10
# platfoorm size
ZOOM = 40
# map size in pixel
REZSIZE = ZOOM*GAMESIZE
REZSIZE2 = REZSIZE/2
# map
MYBACKGR = ((WIN_CENTER[0]-REZSIZE2,WIN_CENTER[1]-REZSIZE2),
            (WIN_CENTER[0] + REZSIZE2, WIN_CENTER[1]-REZSIZE2),
            (WIN_CENTER[0] + REZSIZE2, WIN_CENTER[1] + REZSIZE2),
            (WIN_CENTER[0] - REZSIZE2, WIN_CENTER[1] + REZSIZE2))

# SCALE
MAXSCALE = 3
MINSCALE = 0.2
#zoom parts distance
OBJKOF = 1.2

    #Colors of objects
# back ground color  
BACKGROUND_COLOR = (100,100,100)

BLUE = (0,150,255)
YELLOW = (255,255,0)
GREEN = (255,0,0)
RED = (0,0,255)