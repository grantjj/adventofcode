
import helper_methods as hm

def calculate_final_position(course_commands, command_lookup, initial_position=None):

	if initial_position is None:
		initial_position = [0, 0]

	sub_position = initial_position
	for command in course_commands:
		direction = command[0]
		amplitude = int(command[1])
		delta = [amplitude * c for c in  command_lookup[direction]]
		# using a list in the list definition...sketchy
		sub_position = [sub + delta for sub, delta in zip(sub_position, delta)]

	return sub_position


if __name__=="__main__":

	puzzle_data_file, example_flg = hm.setup(__file__)
	payload = hm.read_data(puzzle_data_file)
	course_commands = [n.split() for n in payload.split('\n')]
	command_lookup = {
		'forward': [1, 0],
		'down': [0, 1],
		'up': [0, -1]
	}

	# Part 1
	final_position = calculate_final_position(course_commands, command_lookup)
	ans = final_position[0] * final_position[1]

	print(f">>> PART 1: The product of the final depth and horizontal position is {ans}")

	if example_flg:
		assert ans == 150, "the example data should return 150"
		print(">>> PART 1 PASS")
	else:
		assert ans == 1604850, "the puzzle data should return 1604850"
		print(">>> PART 1 PASS")

	# Part 2
	# [horizontal, depth, aim] is now the definition, movemnt only happens on forward
	# breaks our previous function though
	command_lookup = {
		'forward': [1, 1, 0],
		'down': [0, 0, 1],
		'up': [0, 0, -1]
	}

	sub_position = [0, 0, 0]
	plotted_course = []
	for command in course_commands:
		direction = command[0]
		amplitude = int(command[1])
		if direction == 'down':
			sub_position[2] += amplitude
		elif direction == 'up':
			sub_position[2] -= amplitude
		elif direction == 'forward':
			sub_position[0] += amplitude
			sub_position[1] += amplitude * sub_position[2]
		# print(sub_position)

	ans = sub_position[0] * sub_position[1]

	print(f">>> PART 1: The product of the final depth and horizontal position is {ans}")

	if example_flg:
		assert ans == 900, "the example data should return 900"
		print(">>> PART 1 PASS")
	else:
		assert ans == 1685186100, "the puzzle data should return 1685186100"
		print(">>> PART 1 PASS")