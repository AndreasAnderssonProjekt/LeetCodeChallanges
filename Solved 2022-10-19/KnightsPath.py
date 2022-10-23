def solve(n):
    #Create Empty Board, -1 indicates that knight have not yet visited the square.
    board = [[-1 for j in range(n)] for i in range(n)]

    #Knight starts in upper left corner.
    board[0][0] = 0

    #Current step count.
    step = 1

    #Current coordinates of knight
    x = 0
    y = 0

    # Eligible moves.
    x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
    y_moves = [1, 2, 2, 1, -1, -2, -2, -1]

    if solve_helper(board,x, y, x_moves, y_moves, step):
        print_board(board)
    else:
        print("There is no feasible solution.")


def solve_helper(board, x, y, x_moves, y_moves, step):

    if step == n * n:
        return True

    for i in range(len(x_moves)):
        x_new, y_new = x + x_moves[i], y + y_moves[i]
        if(eligibleMove(board,x_new,y_new)):
            board[x_new][y_new] = step
            if(solve_helper(board, x_new, y_new, x_moves, y_moves, step+1)):
                return True
            #Backtracking solution.
            board[x_new][y_new] = -1
    return False


def eligibleMove(board,x,y):
    return (x >= 0 and x < n and y >= 0 and y < n and board[x][y] == -1)

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j],end = " ")
        print()

n = 8
solve(n)
