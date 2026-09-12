class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        chars = set()
        for i in nums:
            if i not in chars:
                chars.add(i)
            else: return True
        return False
