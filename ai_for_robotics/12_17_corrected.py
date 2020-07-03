# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
# grid = [[0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    value = [[-1 for col in grid[0]] for row in grid]

    change = True
    
    while change:
        change = False

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                    

                if [y, x] == goal:
                    if value[y][x] != 0:
                        value[y][x] = 0



    value = [[99 if col == -1 else col for col in row] for row in value]

    return value 

value = compute_value(grid, goal, cost)

for row in value:
    print(row)