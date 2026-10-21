class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        # get length of rows
        # iterate through the columns
        # Get the max of every item in a column and add it to answer
        # Turn every el in column to 0
        answer, length, j = 0, len(grid)-1, 0
        if len(grid[0]) < 2: return grid[0][0]
        for cur in grid: cur.sort(reverse=True)
        for idx,val in enumerate(grid[0]):
            out = []
            while j <= length:
                out.append(grid[j][idx])
                grid[j][idx] = 0
                j+=1
            answer += max(out)
            j = 0
        return answer
