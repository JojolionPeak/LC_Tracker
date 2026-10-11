class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s = 1
        if len(nums) == 0: return 0
        for l in range(1, len(nums)):
            if nums[l] != nums[l-1]:
                nums[s] = nums[l]
                s+=1
        return s
