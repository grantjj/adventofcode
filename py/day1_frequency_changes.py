# INITIAL CONDITIONS ---------------------------------------
import_dir = "C:/Users/jgrant/Dropbox/adventofcode/import/"
freq_change_file = import_dir + "frequency_changes.txt"
start_frequency = 0
delta_list = []

# FUNCTIONS ------------------------------------------------

# def running_total(rt_list, val):


# MAIN PROGRAM ---------------------------------------------

# part 1
with open(freq_change_file) as txt:
	n = 0
	for line in txt:
		delta_list.insert(n, int(line.rstrip().strip('+')))
		# print(n, int(line.rstrip().strip('+')))
		n += 1

total_delta = sum(delta_list)
print("The resulting frequency is " + str(total_delta))

# part 2
# delta_list = [-6, 3, 8, 5, -6]
# delta_list = [7, 7, -2, -7, -4]
dup = None
rt_set = set([])
running_total = start_frequency
while not dup:
	for ind, val in enumerate(delta_list):
		running_total += val
		current_set_length = len(rt_set)
		rt_set.add(running_total)
		if len(rt_set) == current_set_length:
			dup = True
			repeat_freq = running_total
			print(running_total)
			break
print("The first duplicate frequency is " + str(repeat_freq))
