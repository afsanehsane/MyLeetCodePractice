class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        lowest_price = prices[0]
        for current_price in prices[1:]:
            possible_profit = current_price - lowest_price
            profit = max(profit, possible_profit)
            lowest_price = min(lowest_price, current_price)
        return profit

        