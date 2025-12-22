from collections import defaultdict
from operator import itemgetter
from pprint import pprint

from helpers import Puzzle

GridPoint = tuple[int, int, int]


def straight_line_distance(p0: GridPoint, p1: GridPoint):
    d = sum([(i1 - i2) ** 2 for i1, i2 in zip(p0, p1)]) ** 0.5
    return d

def find_circuit(circuits, box):
    for c, circuit in enumerate(circuits):
        if box in circuit:
            return c
    return None

def part1(puzzle: Puzzle, connections: int):
    with puzzle.read_input_file() as f:
        raw_data = f.read().splitlines()

    box_coords = [tuple(list(map(int, j.split(",")))) for j in raw_data]
    n_boxes = len(box_coords)

    nearest_neighbours = []
    for box, coords in enumerate(box_coords):
        for box_n in range(box + 1, n_boxes):
            d = straight_line_distance(coords, box_coords[box_n])
            nearest_neighbours.append([coords, box_coords[box_n], d])

    nearest_neighbours.sort(key=itemgetter(2))
    # pprint(nearest_neighbours[:10])

    # a circuit is a group of boxes
    circuits = [{box_coords[n]} for n in range(n_boxes)]
    n_cnxn = 0
    while n_cnxn < connections:
        # print(n_cnxn)
        b1, b2 = nearest_neighbours[n_cnxn][0:2]
        c1, c2 = find_circuit(circuits, b1), find_circuit(circuits, b2)
        # print("new connection", b1, b2)
        # print("circuits", c1, c2, circuits[c1], circuits[c2])
        
        # if any([c1,c2]):
        if c1 != c2:
            circuits[c1] = circuits[c1] | circuits[c2]
            circuits.pop(c2)
            # print(c1,c2, circuits[c1])
        


        n_cnxn += 1
        # pprint(circuits)

    circuits.sort(key=lambda c: len(c), reverse=True)
    circuit_x = [len(c) for c in circuits[0:3]]
    return(eval("*".join([str(c) for c in circuit_x])))

def part2(puzzle: Puzzle):
    with puzzle.read_input_file() as f:
        raw_data = f.read().splitlines()

    box_coords = [tuple(list(map(int, j.split(",")))) for j in raw_data]
    n_boxes = len(box_coords)

    nearest_neighbours = []
    for box, coords in enumerate(box_coords):
        for box_n in range(box + 1, n_boxes):
            d = straight_line_distance(coords, box_coords[box_n])
            nearest_neighbours.append([coords, box_coords[box_n], d])

    nearest_neighbours.sort(key=itemgetter(2))
       # a circuit is a group of boxes
    circuits = [{box_coords[n]} for n in range(n_boxes)]
    n_cnxn = 0
    circuits_x = 0
    while len(circuits) > 1:
        # print(n_cnxn)
        b1, b2 = nearest_neighbours[n_cnxn][0:2]
        c1, c2 = find_circuit(circuits, b1), find_circuit(circuits, b2)
        # print("new connection", b1, b2)
        # print("circuits", c1, c2, circuits[c1], circuits[c2])
        
        # if any([c1,c2]):
        if c1 != c2:
            circuits[c1] = circuits[c1] | circuits[c2]
            circuits.pop(c2)
            # print(c1,c2, circuits[c1])
        
        if len(circuits) == 1:
            circuits_x = b1[0] * b2[0]
        n_cnxn += 1
        # pprint(circuits)

    
    return circuits_x


def main():
    puzzle = Puzzle(day_number=8, run_example=True)
    puzzle.example_solution = 40
    output = part1(puzzle, 10)
    puzzle.check_solution(output)

    puzzle = Puzzle(day_number=8)
    output = part1(puzzle, 1000)
    puzzle.check_solution(output)

    puzzle = Puzzle(day_number=8, run_example=True)
    puzzle.example_solution = 25272
    output = part2(puzzle)
    puzzle.check_solution(output)

    puzzle = Puzzle(day_number=8)
    output = part2(puzzle)
    puzzle.check_solution(output)


if __name__ == "__main__":
    main()
