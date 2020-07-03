# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):

    policy2D = [[' ' for col in grid[0]] for row in grid]

    state = init + [None]
    routes = [ [state] ]
    # print(routes)
    shortest = None
    while len(routes) > 0:
        route = routes.pop(0)
        # print(f'{route=}')
        tip = route[-1]
        # print(f'{tip=}')
        y = tip[0]
        x = tip[1]
        h = tip[2]
        # print(f'{tip[3]=}')
        m = tip[3]
        if shortest is not None and len(route) >= len(shortest):
            continue
        elif [y, x] == goal:
            # tip[3] = '*'
            if shortest is None or len(route) < len(shortest):
                shortest = route.copy()
                shortest.append([goal[0],goal[1], None, '*'])
        else:
            for j in range(len(action)):
                h2 = (tip[2] + action[j]) % len(forward)    
                y2 = (tip[0] + forward[h2][0]) % len(grid)
                x2 = (tip[1] + forward[h2][1]) % len(grid[0])
                m2 = action_name[j]
                if y2 >= 0 and y2 < len(grid) and x2 >= 0 and x2 < len(grid[0]):
                    if grid[y2][x2] == 0:
                        branch = []
                        
                        print(f'{j=}')
                        print(f'cost of action {m2} : {cost[j]}')
                        for k in range(cost[j] - 1):
                            branch.append(None)
                        branch.append([y2, x2, h2, m2])
                        routes.append(route + branch)

    
    if shortest is not None:
        shortest = [s for s in shortest if s is not None]
        last = shortest[-1]
        for n in range(0, len(shortest)-1):
            if shortest[n] is not None:
                step = shortest[n]
                mark = shortest[n+1][3]
                policy2D[step[0]][step[1]] = mark
    else:
        return 'fail'

    return policy2D


path = optimum_policy2D(grid,init,goal,cost)
for row in path:
    print(row)
# print(path)