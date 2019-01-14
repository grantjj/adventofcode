import string

#INITIAL CONDITIONS ---------------------------------------
import_dir = "C:/Users/jgrant/Dropbox/adventofcode/import/"
box_id_file = import_dir + "box_ids.txt"

box_id_list = []


#FUNCTIONS ------------------------------------------------

# def running_total(rt_list, val):
def bring_in_file(file_nm):
	out_list = []
	with open(file_nm) as txt:
		n = 0
		for line in txt:
			out_list.insert(n, line.rstrip())
			n += 1
	return out_list


#MAIN PROGRAM ---------------------------------------------	

#part 1
box_id_list = bring_in_file(box_id_file)
n_ids = len(box_id_list)
letters = string.ascii_lowercase
letter_count = {letter: [0 for i in range(n_ids)] for letter in letters}
double_letters = [0 for i in range(n_ids)]
triple_letters = [0 for i in range(n_ids)]

for i, id in enumerate(box_id_list):
	for s in id:
		letter_count[s][i] += 1

for id in range(n_ids):
	for s in letters:
		if letter_count[s][id] == 2:
			double_letters[id] = 1
		elif letter_count[s][id] == 3:
			triple_letters[id] = 1

checksum = sum(double_letters) * sum(triple_letters)
print("The checksum is " + str(checksum))

#part2
match = {id: [0 for i in range(n_ids)] for id in box_id_list}
shared_letters = {id: ['' for i in range(n_ids)] for id in box_id_list}
for id in box_id_list:
	n = 0
	for next_id in box_id_list:
		total = 0
		string = ''
		for letter in range(26):
			if id[letter] == next_id[letter]:
				total += 1
				string = string + id[letter]
		match[id][n] = total
		shared_letters[id][n] = string
		n += 1

id_pair = []
for k, v in match.items():
	n = 0
	for num in v:
		if num == 25:
			id_pair.append([k, shared_letters[k][n]])
		n += 1
print("The shared letters in the ids are " + id_pair[0][1])
#jiwamotgsfrudclzbyzkhlrvp