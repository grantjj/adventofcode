# from helpers import Direction, PuzzleInput, create_grid_from_input, print_grid
from enum import StrEnum

from helpers import Grid2D, Puzzle


class Legend(StrEnum):
    ROLL = "@"
    NO_ROLL = "."
    REMOVED_ROLL = "x"


def part1(puzzle_input):
    grid = Grid2D.from_file(puzzle_input.input_file)
    # print(grid)

    target_rolls = 0
    for point in grid:
        if grid[point] == Legend.ROLL:
            adjacent_rolls = [
                grid.get(n)
                for n in grid.neighbours(point)
                if grid.get(n) == Legend.ROLL
            ]

            if len(adjacent_rolls) < 4:
                target_rolls += 1

    return target_rolls


def part2(puzzle_input):
    grid = Grid2D.from_file(puzzle_input.input_file)
    forklifting = True
    while forklifting:
        targeted_rolls = []
        for point in grid:
            if grid[point] == Legend.ROLL:
                adjacent_rolls = [
                    grid.get(n)
                    for n in grid.neighbours(point)
                    if grid.get(n) == Legend.ROLL
                ]
                if len(adjacent_rolls) < 4:
                    targeted_rolls.append(point)

        if not targeted_rolls:
            forklifting = False
        else:
            for t in targeted_rolls:
                grid[t] = Legend.REMOVED_ROLL
            rolls_removed = list(grid.values()).count(Legend.REMOVED_ROLL)

    return rolls_removed


def main():
    # # Part 1 Example
    # puzzle_input = PuzzleInput(day_number=4, run_example=True)
    # puzzle_input.example_solution = 13
    # output = part1(puzzle_input)
    # puzzle_input.check_solution(output)

    # # Part 1
    # puzzle_input = PuzzleInput(day_number=4)
    # part1_output = part1(puzzle_input)
    # print(f"Day 4, Part 1: Solution is {part1_output}")

    # Part 2 Example
    puzzle_input = Puzzle(day_number=4, run_example=True)
    puzzle_input.example_solution = 43
    output = part2(puzzle_input)
    puzzle_input.check_solution(output)

    # Part 2
    puzzle_input = Puzzle(day_number=4)
    part2_output = part2(puzzle_input)
    print(f"Day 4, Part 2: Solution is {part2_output}")


if __name__ == "__main__":
    main()
