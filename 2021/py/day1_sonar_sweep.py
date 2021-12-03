import helper_methods as hm

def count_next_value_increases(data):

	count = [1 for n0, n1 in zip(data[:-1], data[1:]) if n1 > n0]

	return sum(count)


def part_1(data, example_flg):

	data_list = [int(n) for n in data.split('\n')]
	count = count_next_value_increases(data_list)

	print(f">>> PART 1: The number of depth measurements that are larger than the previous is {count}")

	if example_flg:
		assert count == 7, "the example data should return 7"
		print(">>> PART 1 PASS")
	else:
		assert count == 1475, "the puzzle data should return 1475"
		print(">>> PART 1 PASS")


def part_2(data, example_flg):

	data_list = [int(n) for n in data.split('\n')]
	window_size = 3
	end_of_list = window_size - 1

	window_summary = []
	for n, depth in enumerate(data_list[:-end_of_list]):
		window = data_list[n:n+window_size]
		window_summary.append(sum(window))

	count = count_next_value_increases(window_summary)

	print(f">>> PART 2: The number of sums that are larger than the previous is {count}")

	if example_flg:
		assert count == 5, "the example data should return 5"
		print(">>> PART 2 PASS")
	else:
		assert count == 1516, "the puzzle data should return 1516"
		print(">>> PART 2 PASS")


if __name__=="__main__":

	puzzle_data_file, example_flg = hm.setup(__file__)
	payload = hm.read_data(puzzle_data_file)

	part_1(payload, example_flg)
	part_2(payload, example_flg)