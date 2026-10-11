class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        s = 0
        for l in range(0, len(nums)):
            if nums[l] != val:
                nums[s] = nums[l]
                s+=1
        return s
