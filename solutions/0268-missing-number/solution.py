class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        l,count = len(nums), 0
        gauss = l * (l+1)//2
        for i in nums:
            count+=i
        return gauss - count
