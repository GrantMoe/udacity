# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
from queue import PriorityQueue

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # open list elements are of the type: [g, y, x]
    closed_nodes = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_nodes[init[0]][init[1]] = 1
    [g, y, x] = [0, init[0], init[1]]
    open_nodes = PriorityQueue()
    open_nodes.put([g,y,x])
    while not open_nodes.empty():
        [g, y, x] = open_nodes.get()
        if [y, x] == goal:
            return [g, y, x]
        else:
            for move in delta: #i in range(len(delta)):
                y2 = y + move[0]
                x2 = x + move[1]
                if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                    if closed_nodes[y2][x2] == 0 and grid[y2][x2] == 0:
                        g2 = g + cost
                        open_nodes.put([g2, y2, x2])
                        closed_nodes[y2][x2] = 1
    return('fail')



path = search(grid, init, goal, cost)
print(path)