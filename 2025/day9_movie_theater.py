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

    # make a grid from the coords
    xmin, *_, xmax = sorted({x for x, y in red_tiles})
    ymin, *_, ymax = sorted({y for x, y in red_tiles})
    
    tile_floor = {
            (x, y): '#' if (x,y) in red_tiles else '.'
            for y in range(ymin, ymax+1)
            for x in range(xmin, xmax+1)
        }
    tile_grid = Grid2D(tile_floor)
    
    # add last tile to front of list
    reds = [red_tiles[t] for t in range(-1, n_tiles)]
    # print(tile_grid)

    # find the green tile boundaries
    for tile in range(n_tiles):
        x0, y0 = reds[tile]
        x1, y1 = reds[tile+1]
        # print(x0, y0, x1, y1)
        if y0 == y1:
            for x in range (min(x0, x1) +1, max(x0, x1)):
                tile_grid[(x,y0)] = 'X'
        if x0 == x1:
            for y in range (min(y0, y1) +1, max(y0, y1)):
                tile_grid[(x0,y)] = 'X'

    # print("")
    # print(tile_grid)

    # fill in the grid
    for r, row in tile_grid.rows.items():
        colored_tiles = [n+tile_grid._xmin for n,t in enumerate(row) if t in ['X','#']]
        y = r+tile_grid._ymin
        for x in range(colored_tiles[0], colored_tiles[-1] + 1):
            if tile_grid[(x,y)] == '.':
                tile_grid[(x,y)] = 'X' 

    # print("")
    # print(tile_grid)

    # find the rectangles
    rectangles = []
    for tile in range(n_tiles):
        for tile_n in range(tile + 1, n_tiles):
            x0, y0 = red_tiles[tile]
            x1, y1 = red_tiles[tile_n]
            rectangle_contents = [
            tile_grid[(x,y)]
                for x in range (min(x0, x1), max(x0, x1)+1)
                for y in range (min(y0, y1), max(y0, y1)+1)
            ]
            # print(x0,y0,x1,y1, rectangle_contents)
            if '.' not in rectangle_contents:
                rectangles.append(len(rectangle_contents))

    return(max(rectangles))

    

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