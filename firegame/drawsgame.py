import pygame

from settings import GAMESIZE, ZOOM, DISPLAY

def drawlines(screen,line1,line2):
    for i in range(GAMESIZE+1):
        pygame.draw.line(screen, (255,0,0), line1[i][0],line1[i][1])
        pygame.draw.line(screen, (255,0,0), line2[i][0], line2[i][1])

def drawobjects(gamemap, mymap, fmymap,fcolumns, frows, fobjects, scale):
    for i in range(GAMESIZE*GAMESIZE):
        if fmymap[i][2][0]+ZOOM*scale>0 and fmymap[i][2][1]+ZOOM*scale>0:
            if fmymap[i][0][0]-ZOOM*scale<DISPLAY[0] and fmymap[i][0][1]-ZOOM*scale<DISPLAY[1]:
                pygame.draw.polygon(gamemap, mymap[i][0], fmymap[i])     
    drawlines(gamemap,fcolumns,frows)
    for obj in fobjects:
        pygame.draw.polygon(gamemap, (0,0,0), obj)