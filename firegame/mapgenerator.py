from settings import GAMESIZE, YELLOW, RED, BLUE, GREEN
import random

def mapgen(screen, grows, gcolumns):
	mymap = []
	for i in range(GAMESIZE):
		for j in range(GAMESIZE):
			pl = random.randint(0,3)
			if pl == 0:
				mymap.append((YELLOW, ((gcolumns[j][0][0],     grows[i][0][1]),
								 	  (gcolumns[j+1][0][0], grows[i][0][1]),
									  (gcolumns[j+1][0][0], grows[i+1][0][1]),
									  (gcolumns[j][0][0],   grows[i+1][0][1]))))
			if pl == 1:
				mymap.append((RED, ((gcolumns[j][0][0],     grows[i][0][1]),
								 	  (gcolumns[j+1][0][0], grows[i][0][1]),
									  (gcolumns[j+1][0][0], grows[i+1][0][1]),
									  (gcolumns[j][0][0],   grows[i+1][0][1]))))
			if pl == 2:
				mymap.append((BLUE, ((gcolumns[j][0][0],     grows[i][0][1]),
								 	  (gcolumns[j+1][0][0], grows[i][0][1]),
									  (gcolumns[j+1][0][0], grows[i+1][0][1]),
									  (gcolumns[j][0][0],   grows[i+1][0][1]))))	
			if pl == 3:
				mymap.append((GREEN, ((gcolumns[j][0][0],     grows[i][0][1]),
								 	  (gcolumns[j+1][0][0], grows[i][0][1]),
									  (gcolumns[j+1][0][0], grows[i+1][0][1]),
									  (gcolumns[j][0][0],   grows[i+1][0][1]))))
	return mymap	
