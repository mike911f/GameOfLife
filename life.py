class Game:

	def __init__(self, width, height):
		self.width = []
		self.height = []
		self.state = []

	def step(self):
		self.new_state = [[]*self.height]

		for line in range(self.height):
			for cell in range(self.width):
				if self.state[line][cell] == 1:
					neighbours_number=

				#    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
				#    Any live cell with two or three live neighbours lives on to the next generation.
				#    Any live cell with more than three live neighbours dies, as if by overpopulation.
				#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
