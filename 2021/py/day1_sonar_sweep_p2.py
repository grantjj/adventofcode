import helper_methods as hm
import helper_classes as hc

import itertools
from collections import defaultdict

example = False

data_file_nm = hm.get_data_file_nm(__file__, example=example)

def def_value():
	return []

payload = defaultdict(def_value)
with open(data_file_nm, 'r') as f:
	for line in f:
		l = line.strip('\n').split()
		payload[l[0]] += l[1:]

# probably shouldn't mash this many methods together, but get the distinct window values
distinct_windows = sorted(set(itertools.chain(*(v for v in payload.values()))))

window_measurements = {k:[] for k in distinct_windows}

for k,v in payload.items():
	for window in v:
		window_measurements[window].append(int(k))

window_summary = {k:sum(v) for k,v in window_measurements.items()}

depths = [v for v in window_summary.values()]
count = 0
for n, depth in enumerate(depths):
	# skip the first
	if n > 0:
		if depth > depths[n-1]:
			count += 1

print(f"The number of depth measurements that are larger than the previous is {count}")

if example:
	assert count == 5, "example set should produce 5"
	print("passed")


# Well I misunderstood the problem, which is annoying, go back to p1