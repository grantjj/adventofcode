import helper_methods as hm
from collections import Counter


class Power:

	def __init__(self):
		self.gamma_rate = 0
		self.epsilon_rate = 0

	def consumption(self):
		return self.gamma_rate * self.epsilon_rate

	def gamma(self, bits):
		freq = self.bit_frequency(bits)
		mfd = max(freq, key=freq.get)
		# this shifts the bits over by 1 and then adds the most frequent digit to the right
		self.gamma_rate = (self.gamma_rate << 1) | mfd

	def epsilon(self, bits):
		freq = self.bit_frequency(bits)
		lfd = min(freq, key=freq.get)
		# this shifts the bits over by 1 and then adds the least frequent digit to the right
		self.epsilon_rate = (self.epsilon_rate << 1) | lfd

	def bit_frequency(self, bits):
		return Counter(bits)


if __name__=="__main__":

	'''
	Call this file using the following
		python <path_to_file> --part X --example
	or if you want to run for real soltuion
		python <path_to_file> --part X

	BINARY STUFF
	https://wiki.python.org/moin/BitwiseOperators
	'''

	puzzle_data_file, input_args = hm.setup(__file__)
	payload = hm.read_data(puzzle_data_file)

	if input_args.part == 1:
		solution_key = [198, 775304]
	elif input_args.part == 2:
		sub = Submarine2()
		solution_key = [900, 1685186100]

	diagnostic_report = [[int(digit) for digit in n] for n in payload.splitlines()]
	verticals = list(zip(*diagnostic_report))

	sub = Power()
	for vertical in verticals:
		sub.gamma(vertical)
		sub.epsilon(vertical)

	solution = sub.consumption()

	print(f">>> PART {input_args.part}: The power consumption of the submarine is {solution}")

	hm.check_answer(solution, solution_key, input_args)
