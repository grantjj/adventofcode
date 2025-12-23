from pprint import pprint
from operator import itemgetter
from helpers import Puzzle, Grid2D
from itertools import pairwise

DAY_NUMBER = 9

def rectangle_area(p1, p2):
    x, y = tuple([abs(a-b)+1 for a,b in zip(p1, p2)])
    return x*y
    
def get_red_tiles(puzzle):
    with puzzle.read_input_file() as f:
        raw_data = f.read().splitlines()

    red_tiles = [tuple(map(int,(tile.split(',')))) for tile in raw_data]
    
    return red_tiles

def part1(puzzle):

    red_tiles = get_red_tiles(puzzle)
    n_tiles = len(red_tiles)
    rectangles = []
    for tile in range(n_tiles):
        for tile_n in range(tile + 1, n_tiles):
            rectangles.append([
                red_tiles[tile],
                red_tiles[tile_n],
                rectangle_area(red_tiles[tile], red_tiles[tile_n])
            ]
            )
    
    rectangles.sort(key=itemgetter(2), reverse=True)

    # pprint(rectangles)
    return rectangles[0][2]

def part2(puzzle):
    red_tiles = get_red_tiles(puzzle)
    n_tiles = len(red_tiles)

    # Step 1: Compress 2D coordinates
    xs = sorted(set(x for x, y in red_tiles))
    ys = sorted(set(y for x, y in red_tiles))

    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}
    
    # Compressed red tiles
    reds = [(x_map[x], y_map[y]) for x, y in red_tiles]
    
    # Create grid
    tile_floor = {
            (x, y): '#' if (x,y) in reds  else '.'
            for y in range(len(ys))
            for x in range(len(xs))
        }
    tile_grid = Grid2D(tile_floor)
    # print(tile_grid)

    # find the green tile boundaries
    for tile in range(n_tiles):
        x0, y0 = reds[tile]
        x1, y1 = reds[(tile+1) % n_tiles]
        # print(x0, y0, x1, y1)
        if y0 == y1:
            for x in range (min(x0, x1) +1, max(x0, x1)):
                tile_grid[(x,y0)] = 'X'
        if x0 == x1:
            for y in range (min(y0, y1) +1, max(y0, y1)):
                tile_grid[(x0,y)] = 'X'

    # # print("")
    # print(tile_grid)

    # fill in the grid
    inside_point = None
    for y in tile_grid._yrange:
        for x in tile_grid._xrange:
            if tile_grid[(x,y)] != ".":
                continue

            transitions = 0
            prev = "."
            for _x in range(x, -1, -1):
                cur = tile_grid[(_x, y)]
                if cur != prev:
                    transitions += 1
                prev = cur
            
            if transitions % 2 == 1:
                inside_point = (x,y)
                break
        
        if inside_point:
            break
    

    # Step 4: Flood fill from the inside point
    if inside_point:
        stack = [inside_point]
        while stack:
            x,y = stack.pop()
            # if x in tile_grid._xrange and y in tile_grid._yrange and tile_grid[(x,y)] == '.':
            if 0 <= x < len(xs) and 0 <= y < len(ys) and tile_grid[(x,y)] == ".":
                tile_grid[(x,y)]= 'X'
                stack.extend([(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)])

    # print(tile_grid)

    # Step 5: Find the largest rectangle with red corners where the perimeter is inside polygon
    largest_area = 0

    for tile in range(n_tiles):
        for tile_n in range(tile + 1, n_tiles):
            x1, y1 = red_tiles[tile]
            x2, y2 = red_tiles[tile_n]
            area = rectangle_area((x1,y1), (x2,y2))
            if area <= largest_area:
                continue

            # check if all green tiles
            _x1, _y1 = x_map[x1], y_map[y1]
            _x2, _y2 = x_map[x2], y_map[y2]
            _xmin = min(_x1, _x2)
            _xmax = max(_x1, _x2)
            _ymin = min(_y1, _y2)
            _ymax = max(_y1, _y2)

            enclosed = True
            for x in range(_xmin, _xmax+1):
                if tile_grid[(x, _ymin)] == "." or tile_grid[(x, _ymax)] == ".":
                    enclosed = False
                    break

            if enclosed:
                for y in range(_ymin, _ymax+1):
                    if tile_grid[(_xmin, y)] == "." or tile_grid[(_xmax, y)] == ".":
                        enclosed = False
                        break

            if enclosed:
                largest_area = area

    # print(largest_area)
    return largest_area
# https://github.com/euporphium/pyaoc/blob/main/aoc/2025/solutions/day09_part2.py
    

def main():

    # puzzle = Puzzle(day_number=DAY_NUMBER, run_example=True)
    # puzzle.example_solution = 50
    # solution = part1(puzzle)
    # puzzle.check_solution(solution)

    # puzzle = Puzzle(day_number=DAY_NUMBER)
    # solution = part1(puzzle)
    # puzzle.check_solution(solution)

    puzzle = Puzzle(day_number=DAY_NUMBER, run_example=True)
    puzzle.example_solution = 24
    solution = part2(puzzle)
    puzzle.check_solution(solution)

    puzzle = Puzzle(day_number=DAY_NUMBER)
    solution = part2(puzzle)
    puzzle.check_solution(solution)


if __name__ == "__main__":
    main()