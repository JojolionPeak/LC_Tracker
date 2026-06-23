class Solution:
    def firstUniqChar(self, s: str) -> int:
        #input: string, output: int of the index of the first unique char/ -1

        # CREATE counter dict AS {}
        # FOR i from 0 to input length
        #     SET dict[key] to each val in input
        # Loop ends
        # FOR key in counter dict
        #     OUTPUT: index of first unique char
        # Loop ends
        # OUTPUT: -1 if no unique chars
        
        if len(s) == 1:
            return 0

        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
