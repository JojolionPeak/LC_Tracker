class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen, count = set(nums), 0

        for n in seen:
            
            if n-1 not in seen:
                step = 1
                while n+1 in seen:
                    step+=1
                    n+=1
                count = max(count, step)
        return count
