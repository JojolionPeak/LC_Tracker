class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out, obj = [], {}
        for string in strs:
            new = "".join(sorted(string))
            if new in obj: obj[new].append(string)
            else: obj[new] = [string]
        for val in obj.values():
            out.append(val)
        return out
