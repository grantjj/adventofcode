import collections
# INITIAL CONDITIONS ---------------------------------------
import_dir = "C:/Users/jgrant/Dropbox/adventofcode/import/"
sleep_file = import_dir + "sleep_times.txt"
guards = collections.defaultdict(list)
times = collections.defaultdict(int)

# # FUNCTIONS ------------------------------------------------

#
#
# # MAIN PROGRAM ---------------------------------------------
for line in sorted(open(sleep_file).read().splitlines()):
	dtm, action = line.replace('[', '').split('] ')
	if action.startswith('Guard'):
		guard_id = int(action.replace('#', '').split()[1])
	elif action == 'falls asleep':
		fell_asleep = int(dtm[-2:])
	elif action == 'wakes up':
		woke_up = int(dtm[-2:])
		guards[guard_id].append([fell_asleep, woke_up])
		times[guard_id] += (woke_up - fell_asleep)

(guard, time) = max(times.items(), key=lambda i: i[1])
minute_counts = [(minute, sum(1 for start, end in guards[guard] if start <= minute < end))
				 for minute in range(60)]
(minute, count) = max(minute_counts, key=lambda i: i[1])

print(guard, minute, count)
print(guard*minute)

# part2
guard_counts = [(guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
				 for minute in range(60) for guard in guards]
(guard, minute, count) = max(guard_counts, key = lambda i: i[2])
print(guard, minute, count)
print(guard*minute)
