#most optimised code
from copy import deepcopy

def NQueens(n: int):
    if n==1 : return [["Q"]]
    if n==2 or n==3 : return []

    #sets of invalid cells
    cols = set()
    d1 = set() #r+c
    d2 = set() #r-c

    answers = [] #list containing all answers
    
    global count
    count = 0 #backtracking count

    #board
    board = [["."]*n for x in range(n)]

    #solve by backtracking
    def solve(row) :
        global count 

        if row==n :
            #last row of the board has been filled
            answers.append(deepcopy(board))
            print(count) #print backtracking count
            return

        #for each cell in the given row
        for col in range(0,n) :
            #if this cell is invalid
            if col in cols or row+col in d1 or row-col in d2 :
                continue #skip this cell

            #place the queen in this cell
            board[row][col] = "Q"

            #add this cell to list of invalid cells
            cols.add(col)
            d1.add(row + col)
            d2.add(row-col)

            #solve furthur
            solve(row + 1)

            #coming here means placing the queen in this cell was wrong move
            #undo that
            board[row][col] = "."
            cols.remove(col)
            d1.remove(row + col)
            d2.remove(row-col)

            #increment count
            count += 1 

    solve(0) #start solving from the 1st row

    #print all answers
    for ans in answers:
        print(ans)
        print()

    return answers


#driver code
NQueens(5)





