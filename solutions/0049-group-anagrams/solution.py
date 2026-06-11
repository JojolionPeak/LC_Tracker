class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dih = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if not key in dih: dih[key] = []
            dih[key].append(strs[i])
        return list(dih.values())
        
