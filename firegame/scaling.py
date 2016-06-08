from settings import WIN_CENTER, ZOOM

#scalling (((x1,y1),(x2,y2)), ((x1,y1),(x2,y2)), ... )
def scalinglines(cords, scale, center):
    rez = []
    for cord in cords:
        x1 =  cord[0][0] - center[0]
        x1 = x1* scale;
        
        x2 =  cord[1][0] - center[0]
        x2 = x2* scale;

        y1 =  cord[0][1] - center[1]
        y1 = y1* scale;

        y2 =  cord[1][1] - center[1]
        y2 = y2* scale;
        
        rez.append(((center[0]+x1, center[1]+y1),
                   (center[0]+x2, center[1]+y2)))  
    return rez    

# scalling ((x,y),(x,y), ... )    
def scalingpoints(cords, scale, center):
    rez = []
    for cord in cords:
        x =  cord[0] - center[0]
        x = x* scale;

        y =  cord[1] - center[1]
        y = y* scale;

        rez.append((center[0]+x, center[1]+y))
    return rez
