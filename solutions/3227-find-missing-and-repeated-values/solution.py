class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans, seen, n = [None, None], set(), len(grid)
        for row in grid:
            for el in row:
                if el in seen: ans[0] = el
                else: seen.add(el)
        for i in range(1, n*n+1):
            if i not in seen: ans[1] = i
        return ans
