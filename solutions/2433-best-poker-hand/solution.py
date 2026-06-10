class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        freq = {}

        for rank in ranks: freq[rank] = (freq.get(rank) or 0) + 1
        for suit in suits: freq[suit] = (freq.get(suit) or 0) + 1

        if freq[suits[0]] == 5: return 'Flush'
        else: 
            for suit in suits: freq[suit] = 0

        max_val = max(freq.values())
        if max_val >= 3: return 'Three of a Kind'
        if max_val == 2: return 'Pair'
        return 'High Card'

