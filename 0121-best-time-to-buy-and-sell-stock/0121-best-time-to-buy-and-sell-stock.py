class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock=prices[0]
        current_profit = 0
        max_profit=0
        for i in range(len(prices)):
            if prices[i] < buy_stock:
                buy_stock = prices[i]

            if prices[i] > buy_stock:
                current_profit = prices[i] - buy_stock

            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit
