board = [[5, 0, 0, 6, 7, 0, 0, 8, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 5, 0, 0, 3, 0,0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 3, 9, 2, 0],
        [0, 0, 0, 0, 2, 0, 1, 0, 5],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 4, 7],
        [0, 3, 0, 0, 0, 4, 0, 0, 1]]

M = 9
prom = 0
visited = 0

###########################################################################3
# this program is to solve suduku using Backtracking algorithm
###############################################################################


def isSafe(grid, row, col, num):

        for x in range(9):
                if grid[row][x] == num:
                        return False

        for x in range(9):
                if grid[x][col] == num:
                        return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
                for j in range(3):
                        if grid[i + startRow][j + startCol] == num:
                                return False


        return True

def solve(board,row,col):
        global prom
        global visited
        if (row == M -1 and col == M):
                return True
        if col == M:
                row += 1
                col = 0
        if board[row][col] > 0:
                return solve(board, row, col + 1)
        for num in range(1, M + 1, 1):

                if isSafe(board, row, col,num):

                        board[row][col] = num



                        if solve(board, row, col + 1):
                                prom += 1
                                return True

                visited +=1
                board[row][col] = 0
        return False


solve(board,0,0)
for i in board:
        print(i)
print("promising", prom)
print("visited",visited)