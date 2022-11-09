from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        res = 0
        max_profit = 0
        min_prices = 0
        for i in range(length):
            max_profit = max(max_profit, (prices[i] - min_prices))
            min_prices = min(prices[i], min_prices)
        return res
