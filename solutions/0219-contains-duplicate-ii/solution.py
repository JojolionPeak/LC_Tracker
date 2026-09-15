class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq = {}
        for i, val in enumerate(nums):
            if val in freq:
                if abs(i - freq[val]) <= k:
                    return True
            freq[val] = i
        return False
        
