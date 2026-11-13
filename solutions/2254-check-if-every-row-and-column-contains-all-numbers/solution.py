class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        ''' 
        check if every row is valid
        check if every column is valid
        ''' 
        seen, n, j, i = set(), len(matrix), 0, 0
        for row in matrix:
            while j < n:
                if row[j] in seen: return False
                elif not 1 <= row[j] <= n: return False
                seen.add(row[j])
                j+=1
            seen.clear()
            j = 0
        j = 0
        while j < n:
            while i < n:
                if matrix[i][j] in seen: return False
                elif not 1 <= matrix[i][j] <= n: return False
                seen.add(matrix[i][j])
                i+=1
            i = 0
            j+=1
            seen.clear()
        return True
