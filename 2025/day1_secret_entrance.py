from dataclasses import dataclass, field

from helpers import PuzzleInput


@dataclass
class Dial:
    range: int = 100
    starting_position: int = 50
    number_line: list = field(default_factory=list)
    position_log: list = field(default_factory=list, init=False)
    _is_starting_position: bool = field(init=False, default=True)

    def __post_init__(self):
        self.number_line = range(self.range)
        self.position = self.starting_position
        self._clicks = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        if self._is_starting_position:
            self._is_starting_position = False
        else:
            self._position_log(value)

    @property
    def clicks(self):
        return self._clicks

    @clicks.setter
    def clicks(self, value):
        self._clicks += value

    @classmethod
    def apply_rotation(cls, dial_instance, rotation_value):
        rotation_direction = int(rotation_value / abs(rotation_value))

        rotation_revolutions, net_rotation = divmod(
            abs(rotation_value), dial_instance.range
        )

        new_position = (
            dial_instance.position + net_rotation * rotation_direction
        ) % dial_instance.range

        rotation_ticks = [
            r % dial_instance.range
            for r in range(
                dial_instance.position + rotation_direction,
                dial_instance.position + net_rotation * rotation_direction,
                rotation_direction,
            )
        ]
        dial_instance.clicks = rotation_ticks.count(0) + rotation_revolutions
        dial_instance.position = new_position

    def _position_log(self, value):
        self.position_log.append(value)


def part1(puzzle_input):
    with puzzle_input.read_input_file() as f:
        steps = f.read().splitlines()

    dial_rotations = [int(step.replace("L", "-").replace("R", "+")) for step in steps]
    safe_dial = Dial()
    for rotation in dial_rotations:
        Dial.apply_rotation(safe_dial, rotation)

    return safe_dial.position_log.count(0)


def part2(puzzle_input):
    with puzzle_input.read_input_file() as f:
        steps = f.read().splitlines()

    dial_rotations = [int(step.replace("L", "-").replace("R", "+")) for step in steps]
    safe_dial = Dial()
    for rotation in dial_rotations:
        Dial.apply_rotation(safe_dial, rotation)

    return safe_dial.clicks + safe_dial.position_log.count(0)


def main():
    # Example puzzle
    puzzle_input = PuzzleInput(day_number=1, run_example=True)
    puzzle_input.example_solution = 3
    day1_output = part1(puzzle_input)
    puzzle_input.check_solution(day1_output)

    # Main puzzle
    puzzle_input = PuzzleInput(day_number=1)
    day1_output = part1(puzzle_input)
    print(f"Part 1 Solution is {day1_output}.")

    # Example puzzle
    puzzle_input = PuzzleInput(day_number=1, run_example=True)
    puzzle_input.example_solution = 6
    day2_output = part2(puzzle_input)
    puzzle_input.check_solution(day2_output)

    # Main puzzle
    puzzle_input = PuzzleInput(day_number=1)
    day1_output = part2(puzzle_input)
    print(f"Part 2 Solution is {day1_output}.")


if __name__ == "__main__":
    main()
