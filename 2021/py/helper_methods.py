import argparse

def setup(current_file):

	# get arg from cmdline for example dataset or not
	parser = argparse.ArgumentParser()
	parser.add_argument('--example', dest='example', action='store_true')
	args = parser.parse_args()

	# grab everything up to the extension
	py_file = current_file[0:current_file.rfind('.')]

	#if we want to run examples, use the example file
	puzzle_data_file = py_file.replace('py','import')
	if args.example is True:
		puzzle_data_file += '_example'

	return puzzle_data_file, args.example


def read_data(data_file_name, filetype='txt'):

	path = f"{data_file_name}.{filetype}"

	if filetype == 'txt':
		with open(path, 'r') as f:
			payload = f.read()

	return payload


