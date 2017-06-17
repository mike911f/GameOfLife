
from graphics import *
import random
import life



def main():
    win_max = 750

    win = GraphWin("Game Of Life", win_max, win_max)
    
    obj = life.Game(win_max, win_max)
    obj.rand_state()
    
    while True:
        obj.step()
        for line in range(obj.height):
			    for cell in range(obj.width):
				    if obj.state[line][cell] == 0 :
				    	win.plotPixel(line, cell, color="white")
				    else :
				    	win.plotPixel(line, cell, color="black")

    win.getMouse()
    win.close()


main()
