class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Valid window: (r - l + 1) - max_freq <= k
        Map: {letter: count}, updated one entry at a time
        Shrink with a while loop, not an if
        best is the returned answer, max_freq is about the current window
        Time O(n), space O(1)
        '''
        count, l, best = {}, 0, 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            max_freq = max(count.values())
            while (r-l+1) - max_freq > k:
                count[s[l]] = count.get(s[l])-1
                l+=1
            best = max(best, r-l+1)
        return best
