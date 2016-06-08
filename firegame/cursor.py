import pygame
from rotozoom import rotozoom3d1, rotocusor3d1, rotoX

def cursor(scale, sina, cosa, alfa, mybeta3d, gcolumns, grows, objects, fobjects):

  pos = pygame.mouse.get_pos()
  x = pos
  temp = rotocusor3d1([pos], alfa, mybeta3d)
  pos = [0,0]
  pos[0] = temp[0][0]
  pos[1] = temp[0][1]    
                
  (trows, tcolumns) = rotoX(scale, grows, gcolumns, mybeta3d)
  for i in range(len(tcolumns)-1):
      if pos[0]> tcolumns[i][0][0]:
          if pos[0] < tcolumns[i+1][0][0]:
              for j in range(len(trows)-1):
                  if pos[1] > trows[j][0][1]:
                      if pos[1] < trows[j+1][0][1]:
                          isheres = False 
                          
                          for obj in objects:
                              print 
                              print "obj", obj[0][0], obj[0][1]
                              if gcolumns[i][0][0] ==  obj[0][0] and grows[j][0][1] == obj[0][1]: 
                                  isheres = True
                          if isheres == False:
                              print "add"
                              obj = ((gcolumns[i][0][0], grows[j][0][1]),
                                     (gcolumns[i][0][0], grows[j+1][0][1]),
                                     (gcolumns[i+1][0][0], grows[j+1][0][1]),
                                     (gcolumns[i+1][0][0], grows[j][0][1]))
                              objects.append(obj)
                              fobjects.append(rotozoom3d1(obj, scale,sina,cosa, mybeta3d))
                              break
  return  fobjects                                  