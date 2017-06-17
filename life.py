class Game:

	def __init__(self, width, height):
		self.width = []
		self.height = []
		self.state = []

	def step(self):
		self.new_state = [[]*self.height]

		for line in range(self.height):
			for cell in range(self.width):
				#Any live cell
				if self.state[line][cell] == 1:
					#with fewer than two live neighbours dies, as if caused by underpopulation.
					if self.get_neighbours_number(line,cell)<2:
						self.new_state[line][cell] = 0
					# with two or three live neighbours lives on to the next generation.
					if self.get_neighbours_number(line,cell)>=2 and \
						self.get_neighbours_number(line,cell)<=3:
						self.new_state[line][cell] = 1
					#with more than three live neighbours dies, as if by overpopulation.
					if self.get_neighbours_number(line,cell)>3:
						self.new_state[line][cell] = 0
				else:
				# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
					if self.get_neighbours_number(line,cell)=3:
						self.new_state[line][cell] = 1

	def draw(self):
		win_max = 750
		win = GraphWin("Game Of Life", win_max, win_max)
		
		for [line] :
			for [cell] :
				
				if self.new_state[line][cell] == 0 :
					win.plotPixel(line, cell, color="white")
				else :
					win.plotPixel(line, cell, color="black")
		win.getMouse()
		win.close()
		
