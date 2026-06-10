class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9,3):
            for j in range (0,9,3):
                box = []
                for r in range (0,3):
                    for c in range(0,3):
                        if board[i+r][j+c] != '.' and i+r >= 0 and i+r < 9 and j+c >= 0 and j+c < 9:
                            box.append(board[i+r][j+c])
                boxSet = set(box)
                if len(box) != len(boxSet): return False

        for i in range (len(board)):
            hor = []
            ver = []
            for j in range(len(board[i])):
                if board[i][j] != '.': hor.append(board[i][j])
                if board[j][i] != '.': ver.append(board[j][i])
            horSet = set(hor)
            if len(horSet) != len(hor): return False
            verSet = set(ver)
            if len(verSet) != len(ver): return False
        return True
