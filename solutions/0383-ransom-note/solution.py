class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in range(len(ransomNote)): count[ransomNote[i]] = count.get(ransomNote[i],0)+1
        for i in range(len(magazine)):
            cur = magazine[i]
            if cur in count: count[cur]-=1
        for val in count.values():
            if val > 0: return False
        return True
