import string
# INITIAL CONDITIONS ---------------------------------------
import_dir = "C:/Users/jgrant/Dropbox/adventofcode/adventofcode2018/import/"
polymer_file = import_dir + "polymer.txt"

# MAIN PROGRAM ---------------------------------------------
polymer = open(polymer_file).read()
pair_list = []

for n in range(26):
	lower = string.ascii_lowercase[n]
	upper = string.ascii_uppercase[n]
	pair_list.insert(n, upper + lower)
	pair_list.insert(n + 26, lower + upper)

has_pairs = 26
while has_pairs > 0:
	has_pairs = 0
	for pair in pair_list:
		if polymer.find(pair) >= 0:
			polymer = polymer.replace(pair,'')
			has_pairs += 1
		print(has_pairs)

print(len(polymer))
