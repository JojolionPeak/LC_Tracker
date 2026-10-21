class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # loop through each row
        # two pointer
        # decrement r and increment l
        l, r, row, out = 0, len(mat[0])-1, 0, 0
        while l < len(mat) and r > -1 and row < len(mat):
            if l == r:
                out+= mat[row][l]
            else:
                out+= mat[row][l]
                out+= mat[row][r]
            l, r, row = l+1, r-1, row+1
        return out
