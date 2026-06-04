class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col]) - 1
                    if row in rows[num]:
                        return False
                    rows[num].add(row)
                    
                    if col in cols[num]:
                        return False
                    cols[num].add(col)

                    srow, scol = (row // 3, col // 3)
                    if (srow, scol) in square[num]:
                        return False
                    square[num].add((srow, scol))       
        return True