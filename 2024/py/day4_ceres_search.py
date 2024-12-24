from collections import defaultdict
from enum import Enum

import helpers

data_file = helpers.get_data_file_name("wordsearch", use_demo_set=False)


class Direction(Enum):
    NORTH = (0, 1)
    NORTHEAST = (1, 1)
    EAST = (1, 0)
    SOUTHEAST = (1, -1)
    SOUTH = (0, -1)
    SOUTHWEST = (-1, -1)
    WEST = (-1, 0)
    NORTHWEST = (-1, 1)

    @classmethod
    def cardinals(cls):
        return [cls.NORTH, cls.EAST, cls.SOUTH, cls.WEST]

    @classmethod
    def intermediates(cls):
        return [cls.NORTHEAST, cls.SOUTHEAST, cls.SOUTHWEST, cls.NORTHWEST]


def diagonal(pos, direction, depth):
    x0, y0 = pos
    dx, dy = direction
    diagonal = [(x0 + d * dx, y0 + d * dy) for d in range(0, depth)]
    return diagonal


grid = defaultdict(str)
with open(data_file, "r") as input:
    raw_data = input.read()

grid = {
    (x, y): val
    for y, line in enumerate(raw_data.split("\n"))
    for x, val in enumerate(line)
}

# position = (9, 9)
depth = len("XMAS")
xmas_count = 0

for position in grid:
    if grid[position] == "X":
        for direction in Direction:
            diag = diagonal(position, direction.value, depth)
            word = "".join([grid[p] for p in diag if p in grid])
            if word == "XMAS":
                xmas_count += 1

print(xmas_count)

sam_count = 0
words = list("MAS"), list("SAM")
for position in grid:
    x0, y0 = position
    candidates = [
        [grid[x0 + d, y0 + d] for d in (-1, 0, 1) if (x0 + d, y0 + d) in grid],
        [grid[x0 + d, y0 - d] for d in (-1, 0, 1) if (x0 + d, y0 - d) in grid],
    ]
    if candidates[0] in words and candidates[1] in words:
        sam_count += 1

print(sam_count)
# for position in grid:
#     if grid[position] == "A":
#         for direction in Direction.intermediates():
#             diag = diagonal(position, direction.value, 1)
#             print([grid[p] for p in diag if p in grid])
