def solve(n):

    board = [[0 for j in range(n)] for i in range(n)]

    nrQueens = 0

    if solve_helper(board,n,nrQueens):
        print_board(board)
    else:
        print("No solution exist")



def solve_helper(board,n,nrQueens):
    if n == 2 or n == 3:
        return False
    if nrQueens == len(board):
        return True

    for i in range(len(board)):
        for j in range(len(board[0])):
            if isSafe(board, i, j):
                board[i][j] = 1
                if solve_helper(board,n,nrQueens + 1):
                    return True
                board[i][j] = 0
    return False



def isSafe(board, x, y):
    return isDiagonalsSafe(board, x, y) and isHorizontalSafe(board, x, y) and isVerticalSafe(board, x, y)

def isDiagonalsSafe(board, x, y):
    n = len(board)
    x_upper, y_upper = x - min(x,y), y - min(x,y)
    x_lower, y_lower = x - min(x, n - y - 1), y + min(x, n - y - 1)
    while x_upper < n and y_upper < n:
        if board[x_upper][y_upper] == 1:
            return False
        x_upper += 1
        y_upper += 1

    while x_lower < n and y_lower >= 0:
        if board[x_lower][y_lower] == 1:
            return False
        x_lower += 1
        y_lower -= 1

    return True


def isHorizontalSafe(board, x, y):
    for i in range(len(board)):
        if board[i][y] == 1:
            return False
    return True

def isVerticalSafe(board, x, y):
    for i in range(len(board)):
        if board[x][i] == 1:
            return False
    return True

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end = " ")
        print()

solve(8)
