from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            s = target - n
            if s in my_dict:
                return [my_dict[s], i]
            my_dict[n] = i
