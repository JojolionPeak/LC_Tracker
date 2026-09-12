class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            s = sorted(i)
            st = ''.join(s)
            if not st in anagrams:
                anagrams[st] = [i]
            else: anagrams[st].append(i)
        return(list(anagrams.values()))
        
