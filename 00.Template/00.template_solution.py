class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        buy_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > max_profit:
                max_profit = price - buy_price

        return max_profit
