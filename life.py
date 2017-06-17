from random import *

class Game:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.state = [[]*self.height]

	def step(self):
		self.new_state = [[]*self.height]

		for line in range(self.height):
			for cell in range(self.width):
				#Any live cell
				if self.state[line][cell] == 1:
					#with fewer than two live neighbours dies, as if caused by underpopulation.
					if self.get_neighbour(line,cell)<2:
						self.new_state[line][cell] = 0
					# with two or three live neighbours lives on to the next generation.
					if self.get_neighbour(line,cell)>=2 and \
						self.get_neighbour(line,cell)<=3:
						self.new_state[line][cell] = 1
					#with more than three live neighbours dies, as if by overpopulation.
					if self.get_neighbour(line,cell)>3:
						self.new_state[line][cell] = 0
				else:
				# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
					if self.get_neighbour(line,cell)=3:
						self.new_state[line][cell] = 1

		self.state = self.new_state

	def get_neighbour(self, x, y):
		count = 0

		if y > 0 and x > 0 and self.state[y-1][x-1] == 1:
			count += 1
		if y > 0 and self.state[y-1][x] == 1:
			count += 1
		if y > 0 and x < self.width-1 and self.state[y-1][x+1] == 1:
			count += 1
		if x > 0 and self.state[y][x-1] == 1:
			count += 1
		if x < self.width-1 and self.state[y][x+1] == 1:
			count += 1
		if y < self.height-1 and x > 0 and self.state[y+1][x-1] == 1:
			count += 1
		if y < self.height-1 and self.state[y+1][x] == 1:
			count += 1
		if y < self.height-1 and x < self.width-1 and self.state[y+1][x+1] == 1:
			count += 1

		return count


	def rand_state(self):
		i = -1
		for line in range(self.height):
			for cell in range(self.width):
				i = random.randrange(0,1)
				self.state[line].append(i)
