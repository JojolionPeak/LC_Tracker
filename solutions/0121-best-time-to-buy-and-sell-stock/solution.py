class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_prof = float('Inf'), 0
        
        for i in prices:
            min_price = min(i, min_price)
            max_prof = max(i - min_price, max_prof)
        
        return max_prof
