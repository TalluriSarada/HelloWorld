myBoard = [[0, 4, 0, 7, 0, 0, 1, 3, 0],
           [0, 0, 2, 0, 0, 0, 6, 0, 0],
           [0, 0, 0, 4, 2, 0, 0, 0, 0],
           [6, 0, 0, 0, 0, 2, 0, 0, 3],
           [2, 3, 1, 0, 7, 0, 0, 8, 0],
           [4, 0, 0, 3, 1, 0, 0, 0, 0],
           [0, 7, 0, 0, 0, 8, 0, 0, 0],
           [0, 0, 6, 0, 3, 0, 0, 0, 4],
           [8, 9, 0, 0, 5, 0, 0, 0, 6]]
def isValid(board, row, col, num):
 
    #check row
    for i in range(9):
        if board[row][i] == num:
            return False
 
    #check col
    for i in range(9):
        if board[i][col] == num:
            return False
 
    #get top-left corner
    c_row = row - row%3
    c_col = col - col%3
 
    #check 3x3 square
    for i in range(c_row, c_row+3):
        for j in range(c_col, c_col+3):
            if board[i][j] == num:
                return False
 
    #return True if none of the cases above returns False
    return True
 
'''
Define the solveBoard() function,
which solves the Sudoku board using recursion
'''
 
def solveBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1,10):
                    if isValid(board, i, j, num):
                        board[i][j] = num
                        result = solveBoard(board)
                        if result == True:
                            return True
                        else:
                            board[i][j] = 0
                return False
    return True
 
 
'''
Call the solveBoard() function and
print the result
'''
 
solveBoard(myBoard)
 
for line in myBoard:
    print(line)
