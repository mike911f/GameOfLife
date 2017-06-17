from random import *

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

	def rand_state(self):
		i = -1
		for line in range(self.height):
			for cell in range(self.width):
				i = random.randrange(0,1)
				self.state[line][cell].append(i)
			
