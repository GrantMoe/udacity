# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------
from queue import PriorityQueue

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    count = 0
    # open list elements are of the type: [g, y, x]
    closed_nodes = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_nodes[init[0]][init[1]] = 1
    [g, y, x] = [0, init[0], init[1]]
    open_nodes = PriorityQueue()
    open_nodes.put([g,y,x])
    while not open_nodes.empty():
        [g, y, x] = open_nodes.get()
        expand[y][x] = count
        count += 1
        if [y, x] == goal:
            break
        else:
            for d in delta: #i in range(len(delta)):
                y2 = y + d[0]
                x2 = x + d[1]
                if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                    if closed_nodes[y2][x2] == 0 and grid[y2][x2] == 0:
                        g2 = g + cost
                        open_nodes.put([g2, y2, x2])
                        closed_nodes[y2][x2] = 1
    return expand


expand = search(grid, init, goal, cost)

for row in expand:
    print(row)