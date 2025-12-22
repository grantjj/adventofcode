from collections import defaultdict
from enum import StrEnum

from helpers import Direction, Grid2D, Puzzle


class Legend(StrEnum):
    ENTRY = "S"
    SPLITTER = "^"
    EMPTY = "."
    BEAM = "|"


def part1(puzzle: Puzzle):
    manifold = Grid2D.from_puzzle(puzzle)
    beam_entry = (manifold.rows[0].index(Legend.ENTRY), 0)
    splitter_count = 0

    for y in range(0, manifold._ymax):
        if y == 0:
            beam_points = [beam_entry]
        else:
            beam_points = [
                (x, y) for x in manifold._xrange if manifold.get((x, y)) == Legend.BEAM
            ]
        # Check next step
        for p in beam_points:
            dd = manifold.step(p, Direction.SOUTH)
            if manifold[dd] == Legend.SPLITTER:
                d1 = manifold.step(dd, Direction.WEST)
                d2 = manifold.step(dd, Direction.EAST)
                manifold[d1] = Legend.BEAM
                manifold[d2] = Legend.BEAM
                splitter_count += 1
            else:
                manifold[dd] = Legend.BEAM

    return splitter_count


def part2(puzzle: Puzzle):
    manifold = Grid2D.from_puzzle(puzzle)

    # print(manifold)
    beams = defaultdict(int)
    beams[manifold.rows[0].index(Legend.ENTRY)] = 1
    for row in manifold.rows:
        for b in tuple(beams.keys()):
            if manifold[(b, row)] == Legend.SPLITTER:
                beams[b - 1] += beams[b]
                beams[b + 1] += beams[b]
                beams.pop(b)

    return sum(beams.values())


def main():
    # puzzle = Puzzle(day_number=7, run_example=True)
    # puzzle.example_solution = 21
    # output = part1(puzzle)
    # puzzle.check_solution(output)

    # puzzle = Puzzle(day_number=7)
    # output = part1(puzzle)
    # puzzle.check_solution(output)

    puzzle = Puzzle(day_number=7, run_example=True)
    puzzle.example_solution = 40
    output = part2(puzzle)
    puzzle.check_solution(output)

    puzzle = Puzzle(day_number=7)
    output = part2(puzzle)
    puzzle.check_solution(output)


if __name__ == "__main__":
    main()
