# Very long winded code, better solutions possible

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        block = dict({1 : [] , 2 : [] , 3 : [] , 4 : [] , 5 : [] , 6 : [] , 7 : [] , 8 : [] , 9 : []})
        for i in range (9) :
            row = []
            col = []
            for j in range (9) :
                if board[i][j] != "." :
                    r = int(board[i][j])
                    if r in row :
                        return False
                    row.append(r)
                    l = block[(i // 3) * 3 + (j // 3) + 1]
                    if r in l:
                        return False
                    l.append(r)
                    block[(i // 3) * 3 + (j // 3) + 1] = l
                if board[j][i] != "." :
                    c = int(board[j][i])
                    if c in col :
                        return False
                    col.append(c)
        return True

        
