# INITIAL CONDITIONS ---------------------------------------
import_dir = "C:/Users/jgrant/Dropbox/adventofcode/import/"
claim_file = import_dir + "cloth_areas.txt"

# claim_list = []


# FUNCTIONS ------------------------------------------------

# def running_total(rt_list, val):
def bring_in_file(file_nm):
    out_list = []
    with open(file_nm) as txt:
        n = 0
        for line in txt:
            out_list.insert(n, line.rstrip())
            n += 1
    return out_list


# MAIN PROGRAM ---------------------------------------------
claim_list = bring_in_file(claim_file)
replace_strings = (' ', ''), ('#', ''), (',', ':'), ('x', ':')

for id, claim in enumerate(claim_list):
    for rep in replace_strings:
        claim_list[id] = claim_list[id].replace(*rep)
    claim_list[id] = claim_list[id].split('@')
    claim_list[id][0] = (int(claim_list[id][0]))
    claim_list[id][1] = [int(i) for i in claim_list[id][1].split(':')]

claims = dict(claim_list)
# claims = {k: claims[k] for k in list(claims)[:3]}

# part 1
# find min and max
right_max = 0
bottom_max = 0
for v in claims.values():
    right_coords = (v[0] + v[2])
    bottom_coords = (v[1] + v[3])
    if right_coords > right_max:
        right_max = right_coords
    if bottom_coords > bottom_max:
        bottom_max = bottom_coords

print("right: " + str(right_max), "bottom: " + str(bottom_max))
area_chart = [[0 for x in range(right_max)] for y in range(bottom_max)]

for v in claims.values():
    x1 = v[0] - 1
    x2 = x1 + v[2]
    y1 = v[1] - 1
    y2 = y1 + v[3]
    # print(v)
    for y in range(y1, y2):
        for x in range(x1, x2):
            area_chart[y][x] += 1

t = 0
for row in area_chart:
    for item in row:
        if item >= 2:
            t += 1
print(t)

# part 2
area_chart = [[0 for x in range(right_max)] for y in range(bottom_max)]
overlap_claims = set([])

for k, v in claims.items():
    x1 = v[0] - 1
    x2 = x1 + v[2]
    y1 = v[1] - 1
    y2 = y1 + v[3]
    # print(v)
    for y in range(y1, y2):
        for x in range(x1, x2):
            if area_chart[y][x] == 0:
                area_chart[y][x] = k
            elif area_chart[y][x] > 0:
                overlap_claims.add(area_chart[y][x])
                overlap_claims.add(k)

for k in claims.keys():
    if not (k in overlap_claims):
        print(k)
