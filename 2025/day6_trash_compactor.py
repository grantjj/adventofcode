from bisect import bisect_left, bisect_right
from itertools import pairwise
from operator import itemgetter
from pprint import pprint

from helpers import Grid2D, Puzzle


def part1(puzzle):
    math_grid = Grid2D.from_puzzle(puzzle, sep=None)
    cumulative_total = 0
    for column in math_grid.columns.values():
        problem = column[-1].join([n for n in column[:-1]])
        cumulative_total += eval(problem)

    return cumulative_total


def part2(puzzle):
    math_grid = Grid2D.from_puzzle(puzzle)
    problems = []
    last_empty_column = 0
    for col, valu in math_grid.columns.items():
        # print(col, math_grid._ymax)
        if valu.count(" ") == math_grid._ymax + 1 or col == math_grid._xmax:
            x_end = col + 1 if col == math_grid._xmax else col
            problem = Grid2D.subset_grid(
                math_grid, range(last_empty_column, x_end), math_grid._yrange
            )
            # print(problem)
            problems.append(problem)
            last_empty_column = col + 1

    cumulative_total = 0
    for p in problems:
        # print(p)
        columns = [column[0:-1] for column in list(p.columns.values())]
        numbers = [("".join([digit for digit in number])).strip() for number in columns]
        arithmetic_operator = (
            "".join([column[-1] for column in list(p.columns.values())])
        ).strip()
        problem = arithmetic_operator.join([n for n in numbers])
        cumulative_total += eval(problem)

    return cumulative_total


def main():
    # puzzle = Puzzle(day_number=6, run_example=True)
    # puzzle.example_solution = 4277556
    # output = part1(puzzle)
    # puzzle.check_solution(output)

    # puzzle = Puzzle(day_number=6)
    # output = part1(puzzle)
    # puzzle.check_solution(output)

    puzzle = Puzzle(day_number=6, run_example=True)
    puzzle.example_solution = 3263827
    output = part2(puzzle)
    puzzle.check_solution(output)

    puzzle = Puzzle(day_number=6)
    output = part2(puzzle)
    puzzle.check_solution(output)


if __name__ == "__main__":
    main()
