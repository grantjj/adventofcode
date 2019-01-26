import string
# INITIAL CONDITIONS ---------------------------------------
#import_dir = "C:/Users/jgrant/Dropbox/adventofcode/adventofcode2018/import/"
import_dir = "D:/jgrant/Dropbox/adventofcode/adventofcode2018/import/"
polymer_file = import_dir + "polymer.txt"


# DEFINE FUNCTIONS -----------------------------------------

def condensePolymer(polymer):
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
			# print(has_pairs)

	return polymer

# PART 1 ---------------------------------------------
initial_polymer = open(polymer_file).read()
reduced_polymer = condensePolymer(initial_polymer)
print(len(reduced_polymer))

# PART 2 ---------------------------------------------
polymer_list = []

for remove in range(26):
	lower = string.ascii_lowercase[remove]
	upper = string.ascii_uppercase[remove]
	polymer_removed = initial_polymer.replace(lower,'')
	polymer_removed = polymer_removed.replace(upper,'')
	polymer_list.insert(remove, polymer_removed)

reduced_list = []
length_list = []

for remove in range(26):
	reduced_polymer = condensePolymer(polymer_list[remove])
	reduced_list.insert(remove, reduced_polymer)
	length_list.insert(remove, len(reduced_polymer))

problem_unit = string.ascii_uppercase[length_list.index(min(length_list))]

print(problem_unit, min(length_list))