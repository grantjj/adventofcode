# PACKAGE IMPORTS
import numpy as np
from scipy.spatial import distance

# PUZZLE INPUT
import_dir = '../import'
coords_file = f"{import_dir}/chronal_coords.txt"

# FUNCTION DEFINTIONS

# PART 1 PROGRAM

# set up bounds
coords_list = np.loadtxt(coords_file, dtype=int, delimiter=', ')
xmin, ymin = coords_list.min(axis=0) - 1
xmax, ymax = coords_list.max(axis=0) + 1 + 1
grid = np.ones([xmax,ymax], dtype=int) * 1e6

xgrid, ygrid = np.meshgrid(np.arange(xmin, xmax), np.arange(xmin, xmax))
targets = np.dstack([xgrid, ygrid]).reshape(-1, 2)

manhattanDistance = distance.cdist(coords_list, targets, metric='cityblock')

print(manhattanDistance)

# for x in range(xmax):
# 	for y in range(ymax):
# 		for item in coords_list:
# 			md = manhattanDistance([x,y], item)
# 			grid[x,y] = md if md < grid[x,y] else grid[x,y]

# print(grid)