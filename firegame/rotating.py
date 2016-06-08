import math
import pygame
from pygame import *

from settings import *

# rotate all points around the center    
def rotatepoints(c, points, sina, cosa):
    respoints = []
    for p in points:
        # distance 
        tempx = p[0] - c[0]
        tempy = p[1] - c[1]
        
        # zmichennia
        x = tempx*cosa - tempy*sina
        y = tempx*sina + tempy*cosa
        
        #update distance 
        respoints.append((c[0] + x, c[1] + y))
    respoints = tuple(respoints)
    return respoints

# rotate all points around the center    
def rotatepoints3d(c, points, beta):
    cs = math.cos(beta*math.pi/180)
    respoints = []
    for p in points:
        # distance 
        tempy = p[1] - c[1]
        y = tempy*cs
        #update distance 
        respoints.append((p[0], c[1] + y))
    return respoints

def rotatecol3dX(c, points, beta):
    s = math.sin(beta*math.pi/180)
    cs = math.cos(beta*math.pi/180)
    respoints = []
    for p in points:
        # distance 
        tempx = p[0] - c[0]
        tempy = p[1] - c[1]

        # zmichennia
        x = tempx*cs  
        y = tempy*cs  
        #update distance 
        respoints.append((p[0], c[1] + y))
    return respoints

def rotaterow3dX(c, points, beta):
    s = math.sin(beta*math.pi/180)
    cs = math.cos(beta*math.pi/180)
    respoints = []
    for p in points:
        # distance 
        tempx = p[0] - c[0]
        tempy = p[1] - c[1]

        # zmichennia
        x = tempx*cs - tempx*s 
        y = tempy*cs  
        #update distance 
        respoints.append((p[0], c[1] + y))
    return respoints

# rotate all points around the center    
def rotatepointsxx(c, points, alfa, beta):
    scb = math.cos((beta)*math.pi/180)
    sb = math.sin((beta)*math.pi/180)
    s  = math.sin(alfa*math.pi/180)
    cs = math.cos(alfa*math.pi/180)
    
    respoints = []
    for p in points:
        # distance 
        tempx = (p[0] - c[0])
        tempy = (p[1] - c[1])
        
        # zmichennia
        x = tempx*cs   - tempy*s/scb
        y = tempx*s*scb + tempy*cs
        #update distance 
        respoints.append((c[0]+x, c[1]+y))
    return respoints

