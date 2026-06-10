class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono = []
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                pass
            elif nums[i] < nums[i+1]:
                mono.append(1)
                pass
            elif nums[i] > nums[i+1]:
                mono.append(0)
                pass
        val = list(set(mono))
        if len(val) == 1 or len(val) == 0:
            return True
        return False
