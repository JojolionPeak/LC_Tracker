class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq, out = {}, []
        for i in strs:
            key = ''.join(sorted(i))
            if key not in freq:
                freq[key] = [i]
            else: freq[key].append(i)

        for i in freq.values():
            out.append(i)
        
        return out
