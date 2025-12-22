from collections import defaultdict
from operator import itemgetter
from pprint import pprint

from helpers import Puzzle

GridPoint = tuple[int, int, int]


def straight_line_distance(p0: GridPoint, p1: GridPoint):
    d = sum([(i1 - i2) ** 2 for i1, i2 in zip(p0, p1)]) ** 0.5
    return d


def part1(puzzle: Puzzle):
    with puzzle.read_input_file() as f:
        raw_data = f.read().splitlines()

    box_coords = [tuple(list(map(int, j.split(",")))) for j in raw_data]
    print(box_coords)

    nearest_neighbours = []
    for box, coords in enumerate(box_coords):
        # print(box, coords)
        for box_n in range(box + 1, len(box_coords)):
            d = straight_line_distance(coords, box_coords[box_n])
            nearest_neighbours.append([coords, box_coords[box_n], d])

    nearest_neighbours.sort(key=itemgetter(2))
    # pprint(nearest_neighbours[:10])

    circuits = [{box} for box in range(len(box_coords))]

    # for cnxn in nearest_neighbours[:10]:
    #     box1, box2, _ = cnxn

    print(circuits)


def main():
    puzzle = Puzzle(day_number=8, run_example=True)
    puzzle.example_solution = 40
    output = part1(puzzle)
    # puzzle.check_solution(output)

    # puzzle = Puzzle(day_number=7)
    # output = part1(puzzle)
    # puzzle.check_solution(output)

    # puzzle = Puzzle(day_number=7, run_example=True)
    # puzzle.example_solution = 40
    # output = part2(puzzle)
    # puzzle.check_solution(output)

    # puzzle = Puzzle(day_number=7)
    # output = part2(puzzle)
    # puzzle.check_solution(output)


if __name__ == "__main__":
    main()
