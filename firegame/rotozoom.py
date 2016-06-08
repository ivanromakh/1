from scaling import scalinglines, scalingpoints
from rotating import rotatepoints, rotatepoints3d, rotaterow3dX, rotatecol3dX, rotatepointsxx
from settings import WIN_CENTER, GAMESIZE, MYBACKGR

def rotozoom3d(rows, columns, scale, sina, cosa, beta3d):
    trows = []
    tcolumns = []

    frows = []
    fcolumns = []
    
    rows3d = []
    columns3d = []
    
    trows = scalinglines(rows,scale, WIN_CENTER)
    tcolumns = scalinglines(columns,scale, WIN_CENTER)

    for i in range(GAMESIZE+1):     
        frows.append(rotatepoints(WIN_CENTER, trows[i],   sina, cosa))
        fcolumns.append(rotatepoints(WIN_CENTER, tcolumns[i], sina, cosa))

    for i in range(GAMESIZE+1):     
        rows3d.append(rotatepoints3d(WIN_CENTER, frows[i],    beta3d))
        columns3d.append(rotatepoints3d(WIN_CENTER, fcolumns[i], beta3d))
    rows3d = tuple(rows3d)
    columns3d = tuple(columns3d)
    return rows3d, columns3d

def rotozoom3d1(obj, scale, sina, cosa, beta3d):
    fobj  = scalingpoints(obj, scale, WIN_CENTER)
    tobj  = rotatepoints(WIN_CENTER, fobj, sina, cosa)
    obj3d = rotatepoints3d(WIN_CENTER, tobj, beta3d)
    obj3d = tuple(obj3d)
    return  obj3d 

def rotocusor3d1(curs, alfa2d, beta3d):
    tcurs  = rotatepointsxx(WIN_CENTER, curs, -alfa2d, beta3d)
    return  tcurs       

def rotoY(rows, columns, beta3d):
    trows = []
    tcolumns = []
    for i in range(GAMESIZE+1):     
        trows.append(rotatepoints3d(WIN_CENTER, rows[i],    beta3d))
        tcolumns.append(rotatepoints3d(WIN_CENTER, columns[i], beta3d))
    return trows, tcolumns

def rotoX(scale, rows, columns, beta3d):
    trows = []
    tcolumns = []

    for i in range(GAMESIZE+1):
        trows.append(scalingpoints(rows[i], scale, WIN_CENTER))     
        trows[i] = rotaterow3dX(WIN_CENTER, trows[i], beta3d)
        tcolumns.append(scalingpoints(columns[i], scale, WIN_CENTER))
        tcolumns[i] = rotatecol3dX(WIN_CENTER, tcolumns[i], beta3d)
    return trows, tcolumns

def cameramove(scale, alfa2d, beta3d, center):
    fbackgr  = scalingpoints(MYBACKGR, scale, WIN_CENTER)
    tbackgr  = rotatepoints(center, fbackgr, alfa2d)
    backgr3d = rotatepoints3d(center, tbackgr, beta3d)
    return backgr3d


