class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = {}
        for i in range(len(s)):
            count[s[i]] = (count.get(s[i]) or 0) +1
        for i in range(len(t)):
            if not count.get(t[i]):
                return False
            else:
                count[t[i]] -= 1
        return True
        
