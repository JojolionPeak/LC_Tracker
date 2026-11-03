class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, l, longest = {}, 0, 0
        if len(s) == 1: return 1
        if len(s) == 0: return 0
        for idx, val in enumerate(s):
            if val in seen and seen[val] >= l:
                longest = max(longest, idx-l)
                l, seen[val] = seen[val]+1, idx
            seen[val] = idx
        return max(longest, idx-l+1)
