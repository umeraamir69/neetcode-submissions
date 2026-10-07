class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            checkDuplicate =[]
            for a in i :
                if a == ".":
                    continue
                if a in checkDuplicate:
                   return False
                else:
                    checkDuplicate.append(a)

        row  , column = 0 , 0
        for column in range(len(board)):
            checkDuplicate =[]
            for row in range(len(board)):
                if board[row][column] == ".":
                    continue
                if board[row][column] in checkDuplicate:
                    return False
                else:
                    checkDuplicate.append(board[row][column])




        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                checkDuplicate = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        value = board[i][j]

                        if value == ".":
                            continue

                        if value in checkDuplicate:
                            return False
                        else:
                            checkDuplicate.append(value)

        return True

        