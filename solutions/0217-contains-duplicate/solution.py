class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        none = set(nums)
        if len(none) == len(nums):
            return False
        return True
