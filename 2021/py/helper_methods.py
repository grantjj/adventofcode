import argparse

def setup(current_file):

	# get arg from cmdline for example dataset or not
	parser = argparse.ArgumentParser()
	parser.add_argument('--example', dest='example', action='store_true')
	parser.add_argument('--part', nargs='?', type=int, default=1)
	args = parser.parse_args()

	# grab everything up to the extension
	py_file = current_file[0:current_file.rfind('.')]

	#if we want to run examples, use the example file
	puzzle_data_file = py_file.replace('py','import')
	if args.example is True:
		puzzle_data_file += '_example'

	return puzzle_data_file, args


def read_data(data_file_name, filetype='txt'):

	path = f"{data_file_name}.{filetype}"

	if filetype == 'txt':
		with open(path, 'r') as f:
			payload = f.read()

	return payload


def check_answer(solution, solution_key, args):

	if args.example:
		target = solution_key[0]
	else:
		target = solution_key[1]

	assert solution == target, f"the example data should return {target}"
	print(f">>> PART {args.part} PASS")