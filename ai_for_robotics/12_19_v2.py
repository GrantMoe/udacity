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
    # NOTE: lots of test printing of routes still in

    policy2D = [[' ' for col in grid[0]] for row in grid]
    # init: [y, x, h]
    routes = [[init]]
    costs = [0]
    trails = [[]]
    cheapest_route = None
    lowest_cost = None
    best_trail = None

    while len(routes) > 0:
        route = routes.pop(0)
        c = costs.pop(0)
        t = trails.pop(0)
        y = route[-1][0]
        x = route[-1][1]
        h = route[-1][2]
        
        # price check
        if cheapest_route is not None and c >= lowest_cost:
            print(f'Price checked at price {c=}!')
            policy2D = [[' ' for col in grid[0]] for row in grid]
            for j in range(len(route)):
                t_temp = t + ['$']
                policy2D[route[j][0]][route[j][1]] = t_temp[j]
            for row in policy2D:
                print(row)
            if cheapest_route is None or c < lowest_cost:
                cheapest_route = route
                lowest_cost = c
                best_trail = t + ['*']
            print('\r\r')
        #goal check
        elif [y, x] == goal:
            print(f'trail complete with cost {c}')
            policy2D = [[' ' for col in grid[0]] for row in grid]
            for j in range(len(route)):
                t_temp = t + ['*']
                policy2D[route[j][0]][route[j][1]] = t_temp[j]
            for row in policy2D:
                print(row)
            if cheapest_route is None or c < lowest_cost:
                cheapest_route = route
                lowest_cost = c
                best_trail = t + ['*']
            print('\r\r')
        else:
            for i in range(len(action)):
                h2 = (h + action[i]) % len(forward)
                y2 = (y + forward[h2][0])
                x2 = (x + forward[h2][1])
                s2 = [y2, x2, h2]
                if y2 >= 0 and y2 < len(grid) and x2 >=0 and x2 < len(grid[0]):
                    if grid[y2][x2] == 0 and s2 not in route:
                        routes.append(route + [s2])
                        costs.append(c + cost[i])
                        trails.append(t + [action_name[i]])
                    if s2 in route:
                        print(f'retread at [{y2}][{x2}]')
                        policy2D = [[' ' for col in grid[0]] for row in grid]
                        for j in range(len(route)):
                            t_temp = t + ['X']
                            policy2D[route[j][0]][route[j][1]] = t_temp[j]
                        for row in policy2D:
                            print(row)
                        print('\r\r')
    if cheapest_route is not None:
        policy2D = [[' ' for col in grid[0]] for row in grid]
        for j in range(len(cheapest_route)):
            policy2D[cheapest_route[j][0]][cheapest_route[j][1]] = best_trail[j]
    else:
        return 'fail'

    return policy2D


path = optimum_policy2D(grid,init,goal,cost)
for row in path:
    print(row)
