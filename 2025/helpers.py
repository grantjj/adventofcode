from contextlib import contextmanager
from dataclasses import dataclass
from itertools import product
from operator import itemgetter
from pathlib import Path
from typing import Any, Self

GridPoint = tuple[int, int]
Grid = dict[GridPoint, Any]


@dataclass
class PuzzleInput:
    day_number: int = 1
    run_example: bool = False

    @property
    def input_suffix(self):
        return "example" if self.run_example else "input"

    @property
    def input_file(self):
        data_path = Path.cwd() / "data"
        data_files = list(data_path.glob(f"day{self.day_number}_{self.input_suffix}*"))
        if len(data_files) > 1:
            print("TOO MANY FILES FOUND", data_files)
        return data_files[0]

    @property
    def example_solution(self):
        return self._solution

    @example_solution.setter
    def example_solution(self, value):
        self._solution = value

    def check_solution(self, value):
        print(
            f"Expected solution is {self.example_solution}, your solution is {value}."
        )
        assert value == self.example_solution
        print("Example solution passed.")

    @contextmanager
    def read_input_file(self):
        file = open(self.input_file, "r")
        try:
            yield file
        finally:
            file.close()


@dataclass
class Puzzle(PuzzleInput):
    day_number: int
    run_example: bool = False


class Grid2D:
    def __init__(self, grid: Grid):
        self.grid = grid

    def __repr__(self):
        xmin, xmax, ymin, ymax = self.boundaries
        r0 = "\n".join(
            "".join(self.grid.get((x, y), " ") for x in range(xmin, xmax + 1))
            for y in range(ymin, ymax + 1)
        )
        return r0

    def __iter__(self):
        return iter(self.grid)

    def __getitem__(self, gridpoint: GridPoint):
        return self.grid[gridpoint]

    def __setitem__(self, gridpoint: GridPoint, value: Any):
        self.grid[gridpoint] = value

    @classmethod
    def from_file(cls, filename: str) -> Self:
        with open(filename, "r") as f:
            input = f.read()

        grid = {
            (x, y): val
            for y, line in enumerate(input.split("\n"))
            for x, val in enumerate(line)
        }
        return cls(grid)

    @property
    def boundaries(self) -> tuple[int, int, int, int]:
        xmin, *_, xmax = sorted({x for x, y in self.grid.keys()})
        ymin, *_, ymax = sorted({y for x, y in self.grid.keys()})
        return (xmin, xmax, ymin, ymax)

    @property
    def directions(self) -> tuple[GridPoint]:
        directions = sorted(product((-1, 0, 1), repeat=2), key=itemgetter(1))
        return directions

    def get(self, gridpoint: GridPoint, default=None):
        return self.grid.get(gridpoint, default)

    def values(self):
        return self.grid.values()

    def neighbours(self, gridpoint, num_directions: int = 8):
        x0, y0 = gridpoint
        for dx, dy in self.directions:
            if num_directions != 9 and not (dx or dy):
                # skip (0,0)
                continue
            if num_directions == 4 and dx and dy:
                # this is a diagonal, skip
                continue

            x1 = x0 + dx
            y1 = y0 + dy
            yield (x1, y1)

    # def reset_gridpoint_value(self, gridpoint: GridPoint, value: Any):
    #     self.grid[gridpoint] = value


def create_grid_from_input(input: str) -> dict[tuple, str]:
    grid = {
        (x, y): val
        for y, line in enumerate(input.split("\n"))
        for x, val in enumerate(line)
    }

    return grid


def grid_boundaries(grid):
    xmin, *_, xmax = sorted({x for x, y in grid.keys()})
    ymin, *_, ymax = sorted({y for x, y in grid.keys()})
    return (xmin, xmax, ymin, ymax)


def print_grid(grid):
    xmin, xmax, ymin, ymax = grid_boundaries(grid)
    print(
        "\n".join(
            "".join(grid.get((x, y), " ") for x in range(xmin, xmax + 1))
            for y in range(ymin, ymax + 1)
        )
    )


# def neighbours(position, grid):


# class Grid:

#     def __init__(self):
#         self.grid = None

#     @property

#     @classmethod
#     def from_string(cls, input):
#         grid = {
#             (x, y): val
#             for y, line in enumerate(input.split("\n"))
#             for x, val in enumerate(line)
#         }


@dataclass
class Direction:
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

    @classmethod
    def adjacents(cls):
        return [
            cls.NORTH,
            cls.NORTHEAST,
            cls.EAST,
            cls.SOUTHEAST,
            cls.SOUTH,
            cls.SOUTHWEST,
            cls.WEST,
            cls.NORTHWEST,
        ]
