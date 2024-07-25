class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            profit = current_price-min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
        
