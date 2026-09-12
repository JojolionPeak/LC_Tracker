from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        if len(s) != len(t): return False
        for char in t:
            if counts[char]:
                counts[char]-=1
            else: return False

        return True

