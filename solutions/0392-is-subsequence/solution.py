class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Init a cur var
        Check if len of s == 0: early return
        Loop through t
        If s[cur] == r increment cur
        If cur == len(s): return True
        return False
        """
        cur =  0
        if len(s) == 0: return True
        for r in t:
            if r == s[cur]:
                cur+=1
            if cur == len(s): return True
        return False
