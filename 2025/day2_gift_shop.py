from itertools import batched

from helpers import PuzzleInput


def get_full_range(id_pair):
    id_boundaries = [int(id) for id in id_pair.split("-")]
    id_range = range(id_boundaries[0], 1 + id_boundaries[1])
    return [id for id in id_range]


def divisors(id):
    digits = len(str(id))
    divisors = [i for i in range(1, digits) if digits % i == 0]
    return divisors


def validate_id_part1(id):
    id_str = str(id)
    midpoint, even_or_odd = divmod(len(id_str), 2)
    halves = [id_str[:midpoint], id_str[midpoint:]]
    if halves[0] == halves[1]:
        return "Invalid"
    else:
        return "Valid"


def validate_id_part2(id):
    divs = divisors(id)
    for div in divs:
        groups = batched([*str(id)], div)
        if len(set(groups)) == 1:
            return "Invalid"

    return "Valid"


def part1(puzzle_input, validate_id: callable):
    with puzzle_input.read_input_file() as f:
        raw_input = f.read().split(",")

    invalid_ids = []
    id_ranges = (get_full_range(id_pair) for id_pair in raw_input)
    for id_range in id_ranges:
        invalid_ids.extend([id for id in id_range if validate_id(id) == "Invalid"])
    # print(invalid_ids)
    return sum(invalid_ids)


def part2(puzzle_input, validate_id: callable):
    with puzzle_input.read_input_file() as f:
        raw_input = f.read().split(",")

    invalid_ids = []
    id_ranges = (get_full_range(id_pair) for id_pair in raw_input)
    # id_range = next(id_ranges)
    for id_range in id_ranges:
        invalid_ids.extend([id for id in id_range if validate_id(id) == "Invalid"])

    return sum(invalid_ids)


def main():
    # Part 1 Example
    puzzle_input = PuzzleInput(day_number=2, run_example=True)
    puzzle_input.example_solution = 1227775554
    day2_output = part1(puzzle_input, validate_id_part1)
    puzzle_input.check_solution(day2_output)

    # Part 1
    puzzle_input = PuzzleInput(day_number=2)
    day2_output = part1(puzzle_input, validate_id_part1)
    print(f"Day 2, Part 1: Solution is {day2_output}")

    # Part 2 Example
    puzzle_input = PuzzleInput(day_number=2, run_example=True)
    puzzle_input.example_solution = 4174379265
    day2_output = part2(puzzle_input, validate_id_part2)
    puzzle_input.check_solution(day2_output)

    # Part 2
    puzzle_input = PuzzleInput(day_number=2)
    day2_output = part2(puzzle_input, validate_id_part2)
    print(f"Day 2, Part 2: Solution is {day2_output}")


if __name__ == "__main__":
    main()
