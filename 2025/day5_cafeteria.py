from bisect import bisect_left, bisect_right
from itertools import pairwise
from operator import itemgetter

from helpers import Puzzle

# puzzle = Puzzle(day_number=5, run_example=True)
puzzle = Puzzle(day_number=5)
with puzzle.read_input_file() as f:
    database = [section.splitlines() for section in f.read().split("\n\n")]

# print(database)
id_ranges = sorted(
    set(tuple(map(int, x.split("-"))) for x in database[0]), key=itemgetter(0, 1)
)
# print(id_ranges)
available_ids = list(map(int, database[1]))


# range cases
# non overlapping, [3,5] and [10,14]
# equal, [3,5] and [3,5] -> make it a set before sorting
# same start, [3,5] and [3,8]
# same end, [10, 14] and [12, 14]
# partial overlap, [12, 18] and [16,20]
# entire overlap, [12, 18] and [13, 15]

# EXPECTED SORT [3,5], [3,8], [10,14], [12,14], [12,18], [13,15], [16,20]
i = 0
while True:
    ranges_to_merge = set()
    overlapping_range = []
    for r0, r1 in pairwise(id_ranges):
        if r0[1] >= r1[0]:
            ranges_to_merge.add(r0)
            ranges_to_merge.add(r1)
            # print(r0, r1, "overlap", (r0[0], max(r0[1], r1[1])))
            overlapping_range.append((r0[0], max(r0[1], r1[1])))

    # print(f"{id_ranges=}")
    # print(f"{ranges_to_merge=}")
    # print(f"{overlapping_range=}")
    if not ranges_to_merge:
        break

    for r in ranges_to_merge:
        id_ranges.pop(id_ranges.index(r))

    # print(id_ranges)
    id_ranges.extend(overlapping_range)
    id_ranges = sorted(set(id_ranges), key=itemgetter(0))
    # print(id_ranges)

fresh_ingredients = []
for ingredient_id in available_ids:
    highest_bound = bisect_right(id_ranges, ingredient_id, key=itemgetter(0))
    # print(ingredient_id, highest_bound - 1, id_ranges[highest_bound - 1])
    id_range = id_ranges[highest_bound - 1]
    if ingredient_id >= id_range[0] and ingredient_id <= id_range[1]:
        # print(ingredient_id, id_range)
        fresh_ingredients.append(ingredient_id)

print(len(fresh_ingredients))  # part 1 answer

# print("---")
# print(id_ranges)
total_fresh_ingredients = 0
for id_range in id_ranges:
    total_fresh_ingredients += len(range(id_range[0], id_range[1] + 1))

print(total_fresh_ingredients)  # part 2 answer
