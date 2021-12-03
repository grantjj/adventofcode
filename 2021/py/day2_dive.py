import helper_methods as hm
from functools import partial

class Submarine1:

	def __init__(self, initial_bearing=None):

		if initial_bearing is None:
			self.initial_bearing = [0, 0]

		self.horizontal = self.initial_bearing[0]
		self.depth = self.initial_bearing[1]

	def up(self, magnitude):
		self.depth -= magnitude

	def down(self, magnitude):
		self.depth += magnitude

	def forward(self, magnitude):
		self.horizontal += magnitude



class Submarine2:

	def __init__(self, initial_bearing=None):

		if initial_bearing is None:
			self.initial_bearing = [0, 0, 0]

		self.horizontal = self.initial_bearing[0]
		self.depth = self.initial_bearing[1]
		self.aim = self.initial_bearing[2]

	def up(self, magnitude):
		self.aim -= magnitude

	def down(self, magnitude):
		self.aim += magnitude

	def forward(self, magnitude):
		self.depth += self.aim * magnitude
		self.horizontal += magnitude


if __name__=="__main__":

	'''
	Call this file using the following
		python <path_to_file> --part X --example
	or if you want to run for real soltuion
		python <path_to_file> --part X
	'''

	puzzle_data_file, input_args = hm.setup(__file__)
	payload = hm.read_data(puzzle_data_file)
	plotted_course = [n.split() for n in payload.split('\n')]

	if input_args.part == 1:
		sub = Submarine1()
		solution_key = [150, 1604850]
	elif input_args.part == 2:
		sub = Submarine2()
		solution_key = [900, 1685186100]

	for bearing in plotted_course:

		direction = bearing[0]
		magnitude = int(bearing[1])

		sub_command = {
			"up": partial(sub.up, magnitude),
			"down": partial(sub.down, magnitude),
			"forward": partial(sub.forward, magnitude)
		}

		sub_command[direction]()

	solution = sub.horizontal * sub.depth

	print(f">>> PART {input_args.part}: The product of the final depth and horizontal position is {solution}")

	hm.check_answer(solution, solution_key, input_args)
