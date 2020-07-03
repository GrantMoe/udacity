# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    
    # open list elements are of the type: [g, y, x]
    closed_nodes = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed_nodes[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    # [g, y, x]
    open_nodes = [[0, init[0], init[1]]]

    count = 0

    while len(open_nodes) > 0:
        open_nodes.sort(reverse=True)
        [g, y, x] = open_nodes.pop()
        expand[y][x] = count
        count += 1
        if [y, x] == goal:
            break
        else:
            for i in range(len(delta)):
                y2 = y + delta[i][0]
                x2 = x + delta[i][1]
                if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                    if closed_nodes[y2][x2] == 0 and grid[y2][x2] == 0:
                        g2 = g + cost
                        open_nodes.append([g2, y2, x2])
                        closed_nodes[y2][x2] = 1
                        action[y2][x2] = i
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    [y, x] = goal
    policy[y][x] = '*'
    while [y, x] != init:
        y2 = y - delta[action[y][x]][0]
        x2 = x - delta[action[y][x]][1]
        policy[y2][x2] = delta_name[action[y][x]]
        [y, x] = [y2, x2]
    return policy # make sure you return the shortest path

path = search(grid, init, goal, cost)

for row in path:
    print(row)