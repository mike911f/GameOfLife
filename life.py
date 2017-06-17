
import random

class Game:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.state = []
	def getPos(self, x, y):
		return y*self.width + x
	def step(self):
		self.new_state = []

		for line in range(self.height):
			for cell in range(self.width):
				#Any live cell
				# CALCULATE NEIGBOUR NUMBER
				n_number = self.get_neighbour(line,cell)
				if self.state[self.getPos(line, cell)] == 1:
					#with fewer than two live neighbours dies, as if caused by underpopulation.
					if n_number<2:
						self.new_state.append(0)
					# with two or three live neighbours lives on to the next generation.
					elif n_number>=2 and \
						n_number<=3:
						self.new_state.append(1)
					#with more than three live neighbours dies, as if by overpopulation.
					elif n_number>3:
						self.new_state.append(0)
					else:
						self.new_state.append(self.state[self.getPos(line, cell)])

				else:
				# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
					if n_number == 3:
						self.new_state.append(1)
					else:
						self.new_state.append(self.state[self.getPos(line, cell)])

		self.state = self.new_state

	def get_neighbour(self, x, y):
		count = 0

		if y > 0 and x > 0 and self.state[self.getPos(y - 1, x - 1)] == 1:
			count += 1
		if y > 0 and self.state[self.getPos(y-1, x)] == 1:
			count += 1
		if y > 0 and x < self.width-1 and self.state[self.getPos(y-1, x+1)] == 1:
			count += 1
		if x > 0 and self.state[self.getPos(y, x-1)] == 1:
			count += 1
		if x < self.width-1 and self.state[self.getPos(y, x+1)] == 1:
			count += 1
		if y < self.height-1 and x > 0 and self.state[self.getPos(y+1, x-1)] == 1:
			count += 1
		if y < self.height-1 and self.state[self.getPos(y+1, x)] == 1:
			count += 1
		if y < self.height-1 and x < self.width-1 and self.state[self.getPos(y+1, x+1)] == 1:
			count += 1

		return count


	def rand_state(self):
		i = -1
		for line in range(0, self.height):
			for cell in range(0, self.width):
				i = random.randrange(0,2)
				self.state.append(i)
