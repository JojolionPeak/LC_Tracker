class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        rev = []
        for num in reversed(nums):
            rev.append(num)
        return nums + rev
        
