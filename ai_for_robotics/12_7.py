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


# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]

grid = [[0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0, 0, 0], 
        [0, 1, 0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):

    open_nodes = []
    open_nodes.append([init, 0])

    # node: [[r, c], G]
    def checkG(elem):
        return elem[1]

    def isValid(square):
        if square[0] < 0 or square[1] < 0:
            return False
        if square[0] >= len(grid) or square[1] >= len(grid[0]):
            return False
        if grid[square[0]][square[1]] != 0:
            return False
        return True
        
    while len(open_nodes) > 0:
        open_nodes.sort(key=checkG)
        node = open_nodes.pop(0)
        path = [node[1], node[0][0], node[0][1]]
        if node[0] == goal:
            break
        for move in delta:
            neighbor = [ node[0][0] + move[0], node[0][1] + move[1]]
            if isValid(neighbor):
                open_nodes.append([neighbor, node[1] + cost])
                grid[neighbor[0]][neighbor[1]] = 'X'
        grid[node[0][0]][node[0][1]] = 'X'
    if [path[1], path[2]] != goal:
        return 'fail'
    return path


path = search(grid, init, [goal], cost)
print(path)