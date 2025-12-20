from itertools import combinations

from helpers import PuzzleInput


def get_possible_joltage_pairs(bank):
    n_batteries = len(bank)
    return [
        int(bank[j1] + bank[j2])
        for j1 in range(n_batteries)
        for j2 in range(j1 + 1, n_batteries)
    ]


def batteries_by_the_dozen(bank):
    dozens = [int("".join(t)) for t in list(combinations(bank, 12))]
    return dozens


def part1(puzzle_input):
    with puzzle_input.read_input_file() as f:
        battery_banks = f.read().splitlines()

    output_joltages = [max(get_possible_joltage_pairs(bank)) for bank in battery_banks]
    return sum(output_joltages)


def part2(puzzle_input):
    with puzzle_input.read_input_file() as f:
        battery_banks = f.read().splitlines()

    joltage = []
    batteries_needed = 12
    for battery_bank in battery_banks:
        # print("------")
        bank = [int(j) for j in list(battery_bank)]
        # print(bank)
        selected_batteries = []
        n_batteries = len(bank)
        window_start_index = 0
        while len(selected_batteries) != 12:
            sliding_window = [
                window_start_index,
                n_batteries - (batteries_needed - len(selected_batteries)) + 1,
            ]
            battery_window = bank[sliding_window[0] : sliding_window[1]]
            largest_battery_in_window = max(battery_window)
            battery_index = battery_window.index(largest_battery_in_window)

            selected_batteries.append(largest_battery_in_window)
            # print(sliding_window, battery_window, selected_batteries)
            window_start_index = sliding_window[0] + battery_index + 1

        joltage.append(int("".join(map(str, selected_batteries))))

    print(f"{joltage=}")
    return sum(joltage)


def main():
    # # Part 1 Example
    # puzzle_input = PuzzleInput(day_number=3, run_example=True)
    # puzzle_input.example_solution = 357
    # puzzle_input.check_solution(part1(puzzle_input))

    # # Part 1
    # puzzle_input = PuzzleInput(day_number=3)
    # part1_output = part1(puzzle_input)
    # print(f"Day 3, Part 1: Solution is {part1_output}")

    # Part 2 Example
    puzzle_input = PuzzleInput(day_number=3, run_example=True)
    puzzle_input.example_solution = 3121910778619
    output = part2(puzzle_input)
    puzzle_input.check_solution(output)

    # Part 2
    puzzle_input = PuzzleInput(day_number=3)
    part2_output = part2(puzzle_input)
    print(f"Day 3, Part 2: Solution is {part2_output}")


if __name__ == "__main__":
    main()
