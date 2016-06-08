from settings import GAMESIZE, REZSIZE2, WIN_CENTER, ZOOM

def borders():
    
    # game colomns
    bordx = WIN_CENTER[0] - REZSIZE2
    bordy1 = WIN_CENTER[1] - REZSIZE2
    bordy2 = WIN_CENTER[1] + REZSIZE2

    gcolumns = []
    for i in range(GAMESIZE+1):
        gcolumns.append(((bordx,bordy1), (bordx,bordy2)))
        bordx+=ZOOM  

    #game rows
    bordy = WIN_CENTER[1] - REZSIZE2
    bordx1 = WIN_CENTER[0] - REZSIZE2
    bordx2 = WIN_CENTER[0] + REZSIZE2

    grows = []
    for i in range(GAMESIZE+1):
        grows.append(((bordx1,bordy), (bordx2,bordy)))
        bordy+=ZOOM


    return grows, gcolumns
