class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        mySquares = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        myRows = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }
        myColumns = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: []
        }


        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.':

                    #Check if column is valid else return False or append val
                    if val in myColumns[col]:
                        return False
                    else:
                        myColumns[col].append(val)
                    
                    #Check if row is valid else return False or append val
                    if val in myRows[row]:
                        return False
                    else:
                        myRows[row].append(val)

                    #Check if Square is valid else return false or append val
                    currSquare = (row // 3) * 3 + (col // 3)
                    currSquare = int(currSquare)

                    if val in mySquares[currSquare]:
                        return False
                    else:
                        mySquares[currSquare].append(val)

                
                
        return True
