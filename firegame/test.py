import pygame.gfxdraw
from   pygame.locals import *
import sys
import math

from settings  import *
from menu      import Menu, mennu
from scaling   import scalinglines, scalingpoints
from rotating  import rotatepoints
from drawsgame import drawlines, drawobjects
from rotozoom  import rotozoom3d, rotozoom3d1 
from borders   import borders
from cursor    import cursor
from mapgenerator import mapgen

# draw information and fps  
def drawtext(screen, timer):
    surf =  pygame.Surface((100, 100))
    surf.fill((255,255,255))
    screen.blit(surf, (0, 0))
    mytext = pygame.font.SysFont("monospace", 15)
    timer.tick(100)
    text = mytext.render("FPS "+str(timer.get_fps()), 1, (10, 10, 10))
    screen.blit(text, (5, 0))

def updateobjects(gamemap, scale, sina, cosa, mybeta3d, grows, gcolumns, mymap, objects):
    (frows,fcolumns) = rotozoom3d(grows, gcolumns, scale,
                                  sina, cosa, mybeta3d)
    fobjects = []
    for obj in objects:
        fobjects.append(rotozoom3d1(obj, scale,sina, cosa, mybeta3d))
    fmymap = []    
    for i in range(GAMESIZE*GAMESIZE):
        fmymap.append(rotozoom3d1(mymap[i][1], scale, sina, cosa, mybeta3d))
    #draw background on the screen 
    gamemap.fill(BACKGROUND_COLOR)
    #update game map
    drawobjects(gamemap, mymap, fmymap,fcolumns, frows, fobjects, scale)
    return frows, fcolumns, fobjects, fmymap

# main function
def main():
    pygame.init()
    # menu check server or client
    mennu()
    screen = pygame.display.set_mode(DISPLAY) 
    timer = pygame.time.Clock()

    # klavisha press
    iszoomincres    = False
    iszoomdecres    = False
    isrotaterigth   = False
    isrotateleft    = False
    isrotateup      = False
    isrotatedown    = False
    ismovecamup     = False
    ismovecamdown   = False
    ismovecamleft   = False
    ismovecamrigth  = False
    isinventar      = False
    
    #black rectanges in the map
    objects = []
    fobjects = []
    
    #for borders lines (rows and columns)
    grows, gcolumns = borders()
    #map with borders
    mymap = mapgen(screen, grows, gcolumns)
    fmymap = []
    for obj in mymap:
        fmymap.append(obj[1])
    frows =    []
    fcolumns = []
    trows =    []
    tcolumns = []

    for i in range(GAMESIZE+1): 
        frows.append(grows[i])
        fcolumns.append(gcolumns[i])
        trows.append(grows[i])
        tcolumns.append(gcolumns[i])
        
    #start angle2d, angle3d and scale
    myalfa2d = 0
    cosa = 1
    sina = 0  
    mybeta3d = 0
    scale = 1
    zoom = ZOOM + 0.0
      
    pos = WIN_CENTER
    center = WIN_CENTER
    move = [WIN_CENTER[0]-8, WIN_CENTER[1]-35]
    #loop
    gamemap = pygame.Surface(DISPLAY)
    gamemap.fill((250, 250, 250))

    while True:
        # zooming
        if iszoomincres   == True:
            if scale<MAXSCALE:
                zoom += 2
                scale = zoom/ZOOM
                (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale, sina, cosa, mybeta3d, 
                                                               grows, gcolumns, mymap, objects)
                
        elif iszoomdecres == True:
            if scale>MINSCALE:
                zoom -= 2
                scale = zoom/ZOOM
                (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale,  sina, cosa, mybeta3d, 
                                                                  grows, gcolumns, mymap, objects)
                
        #map rotating
        if isrotaterigth  == True:
            myalfa2d+=1
            sina = math.sin(myalfa2d*math.pi/180)
            cosa = math.cos(myalfa2d*math.pi/180)
    
            (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale, sina, cosa, mybeta3d, 
                                                               grows, gcolumns, mymap, objects)
           
        elif isrotateleft == True:
            myalfa2d-=1
            sina = math.sin(myalfa2d*math.pi/180)
            cosa = math.cos(myalfa2d*math.pi/180)
            (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale, sina, cosa, mybeta3d, 
                                                               grows, gcolumns, mymap, objects)
             
        if isrotateup   == True:
            if mybeta3d > -80:
                mybeta3d-=1
                (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale,  sina, cosa, mybeta3d, 
                                                                   grows, gcolumns, mymap, objects)
                
        if isrotatedown == True:
            if mybeta3d < 0:
                mybeta3d+=1
                (frows,fcolumns, fobjects, fmymap) = updateobjects(gamemap, scale,  sina, cosa, mybeta3d, 
                                                                   grows, gcolumns, mymap, objects)
                xbool = True
                ybool = False
                gamemap = pygame.transform.flip(gamemap, xbool, ybool) 
        #camera fbackgr
        if ismovecamup    == True:
            center[1]+=10
            (frows,fcolumns) = rotozoom3d(grows, gcolumns, scale,
                                          sina, cosa, mybeta3d)
            fobjects = []
            for obj in objects:
                fobjects.append(rotozoom3d1(obj, scale,sina, cosa, mybeta3d))
            
        if ismovecamdown  == True:
            center[1]-=10
            (frows,fcolumns) = rotozoom3d(grows, gcolumns, scale,
                                          sina, cosa, mybeta3d)
            fobjects = []
            for obj in objects:
                fobjects.append(rotozoom3d1(obj, scale, sina, cosa, mybeta3d))
            
        if ismovecamleft  == True:
            center[0]-=10
            (frows,fcolumns) = rotozoom3d(grows, gcolumns, scale,
                                          sina, cosa, mybeta3d)
            fobjects = []
            for obj in objects:
                fobjects.append(rotozoom3d1(obj, scale, sina, cosa, mybeta3d))
               
        if ismovecamrigth == True:
            center[0]+=10
            (frows,fcolumns) = rotozoom3d(grows, gcolumns, scale,
                                          sina, cosa, mybeta3d)
            fobjects = []
            for obj in objects:
                fobjects.append(rotozoom3d1(obj, scale,sina, cosa, mybeta3d))

            
                 
        # ALL EVENTS for gamemode
        for e in pygame.event.get():
            # check multipress 
            keystate = pygame.key.get_pressed()
        
            # exit
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
 
            # start moving and rotating
            elif e.type == KEYDOWN:
                if keystate[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
                if keystate[K_UP]:
                    isrotateup     = True
                if keystate[K_DOWN]:
                    isrotatedown   = True
                if keystate[K_LEFT]:
                    isrotateleft   = True
                if keystate[K_RIGHT]:
                    isrotaterigth  = True
                if keystate[K_1]:
                    iszoomincres   = True
                if keystate[K_2]:
                    iszoomdecres   = True
                if keystate[K_w]:
                    ismovecamup    = True
                if keystate[K_s]:
                    ismovecamdown  = True
                if keystate[K_a]:
                    ismovecamleft  = True 
                if keystate[K_d]:
                    ismovecamrigth = True 
                if keystate[K_i]:
                    isinventar     = True           

            # stop moving and rotating        
            elif e.type == KEYUP:
                if e.key == K_UP:
                    isrotateup     = False
                if e.key == K_DOWN:
                    isrotatedown   = False
                if e.key == K_LEFT:
                    isrotateleft   = False
                if e.key == K_RIGHT:
                    isrotaterigth  = False
                if e.key == K_1:
                    iszoomincres   = False
                if e.key == K_2:
                    iszoomdecres   = False
                if e.key == K_w:
                    ismovecamup    = False
                if e.key == K_s:
                    ismovecamdown  = False
                if e.key == K_a:
                    ismovecamleft  = False       
                if e.key == K_d:
                    ismovecamrigth = False
                if e.key == K_i:
                    isinventar     = False    

            #cursor    
            elif e.type == pygame.MOUSEBUTTONDOWN:        
                fobjects = cursor( scale, sina, cosa, myalfa2d, mybeta3d, gcolumns, 
                                  grows, objects, fobjects)
                drawobjects(gamemap, mymap, fmymap,fcolumns, frows, fobjects, scale)
               
        drawtext(gamemap, timer)
        screen.blit(gamemap,(0,0))
        pygame.display.flip()

# main fuction                
if __name__ == "__main__":
    main()
    
