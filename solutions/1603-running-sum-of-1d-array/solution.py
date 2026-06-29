class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            out.append(total)
        return out
        
