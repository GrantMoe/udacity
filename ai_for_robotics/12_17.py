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
    
    policy = [[' ' for col in grid[0]] for row in grid]
    policy[goal[0]][goal[1]] = '*'
    # node in format [g, y, x]
    open_nodes = [[0, goal[0], goal[1]]]

    while len(open_nodes) > 0:
        open_nodes.sort(reverse=True)
        next_node = open_nodes.pop()
        y = next_node[1]
        x = next_node[2]
        g2 = next_node[0] + cost
    
        for i in range(len(delta)):
            y2 = y + delta[i][0]
            x2 = x + delta[i][1]
            if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                if grid[y2][x2] == 0 and policy[y2][x2] == ' ':
                    open_nodes.append([g2, y2, x2])
                    policy[y2][x2] = delta_name[(i + 2) % len(delta_name)]
                
    return policy 

value = compute_value(grid, goal, cost)

for row in value:
    print(row)