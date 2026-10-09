class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' 
        increment r, and add count to freq
        while window is not valid (size - max_freq > k), decrement freq[cur] by 1, increment l (until window is valid)
        update max_freq
        '''
        freq, best, max_freq, l = {}, 0, 0, 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0)+1
            max_freq = max(freq.values())

            while (r-l+1) - max_freq > k:
                freq[s[l]]-=1
                l+=1
            
            best = max(r-l+1, best)
        return best
