board = [[1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

board2 = [[1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        ]



counter = 2
proising = 0

###########################################################################3
# this program is to solve knight tour problem using Backtracking algorithm
###############################################################################

# this function tries all possible moves from position p
# and checks if this move is inside the board
# then it stores the moves in a list
# and rtern this list
# the purpose of this function to check the number of possible moves for a spesific position
def possibilities(board,x,y):
    pos_x = [1, 1, -1, -1, 2, -2, 2, -2]
    pos_y = [2, -2, 2, -2, -1, -1, 1, 1]
    possible_moves = []
    for i in range(8):
        if x+pos_x[i] >= 0 and x+pos_x[i]< len(board[0]) and y+pos_y[i] >= 0 and y+pos_y[i] < len(board) and board[x+pos_x[i]][y+pos_y[i]]==0:
            possible_moves.append([x+pos_x[i],y+pos_y[i]])
    return possible_moves

# this function solves the problem
# it takes four parameters
# the board, position and counter that we use it to set a value to a position
def solve(board,x,y,counter):
    global proising
    # here the function checks if the value of the counter is larger than 65
    # becuase once we reach 65 so all cells in the board must had been filled
    # then the function returns True, and thus we got a solution
    if counter >= 65:
        return True

    # we get all possible moves to the initial position and store it as a list
    # in order to choose the appropriate move that meets the requairment
    pos = possibilities(board,x,y)
    # this loop takes every move for this position and gets the possible moves of it
    # compare the number of its moves with the previous position
    # in order to choose the position that have the minimum moves and then the counter increments by 1
    # the value of the chosen postion in the bord becomes the value of the counter
    minimum_pos = pos[0]
    for i in pos:
        if len(possibilities(board,i[0],i[1])) <= len(possibilities(board,minimum_pos[0],minimum_pos[1])):
            minimum_pos = i

    new_x = minimum_pos[0]
    new_y = minimum_pos[1]
    board[new_x][new_y]= counter
    counter += 1
    proising +=1
    solve(board,new_x,new_y,counter)










solve(board,0,0,counter)
for i in board:
    print(i)

# solve(board2,0,0,counter)
# for i in board2:
#     print(i)

print(proising)

# this heuristic takes half time because