def main():
	win_max = 750
    	win = GraphWin("Game Of Life", win_max, win_max)
	
	while True:
		i = 0
		pos_x = random.randrange(0,750)
		pos_y = random.randrange(0,750)
		
		live = random.randrange(1,2)
		
		if (live):
			win.plotPixel(pos_x, pos_y, color="black")
		else:
			win.plotPixel(pos_x, pos_y, color="white")
		i = i+1
		if i==200: False
	win.getMouse()
	win.close()
	
main()
