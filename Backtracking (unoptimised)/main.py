from copy import deepcopy

#number of times back-tracked
count = 0
answers = [] #list of correct solutions
row_to_be_filled = 0 #row index 
n = 0

def NQueens(N) :
    if N==1 : return [["Q"]]
    if N==2 or N==3 : return []

    #global variables
    global answers , n
    n = N

    #board
    board = [[" " for x in range(n)] for y in range(n)]

    #list of remaining cells
    remval = [[True for x in range(n)] for y in range(n)]
        # nxn list with all elements = True initially

    solve(board, remval) 

    #print each colution
    for answer in answers :
        print(answer)
        print()



#solve by backtracking
def solve(board, remval) :
    global count, answers, row_to_be_filled, n

    #if all rows from 0 to n-1 have been filled
    if row_to_be_filled == n : 
        answers.append(deepcopy(board))
        print(count)
        return

    row = row_to_be_filled

    #for each cell in the row  #cell =(row, col)
    for col in range(n) :
        #if this cell is invalid, skip it
        if remval[row][col] == False :
            continue

        #add queen to the cell
        board[row][col] = "Q"

        #now next row is to be filled
        temp = row_to_be_filled
        row_to_be_filled += 1

        #update the validity of the cells
        #then solve furthur
        solve(board, validate(deepcopy(remval),row,col) ) 
        
        #coming here means
        #placing queen in this cell was wrong
        #undo everything
        board[row][col] = " "
        row_to_be_filled = temp #prev value 

        #now we know that queen cant be placed here
        remval[row][col] = False

        #increment backtrack count
        count = count + 1
    #all queens have been correctly placed

    

#after placing a queen, mark all invalid cells as False
def validate(remval, row, col) :
    global n

    #queen has been placed in board[row][col]
    remval[row][col] = False
    #all the cells in the same row, col and diagonal are now invalid

    #diagonals
    sum = row +col
    dif = row - col

    #check all cells
    for r in range(row,n) :
        for c in range(0,n) :
            #if cell in the same row, col or diagonals
            if r==row or c==col or r+c==sum or r-c==dif :
                remval[r][c] = False

    return remval 



############ driver code ####################
NQueens(5)

