class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1] and not buy:
                buy = prices[i]
            if buy and prices[i] > prices[i + 1]:
                print(prices[i], buy)
                # return prices[i] - buy
                maxProfit = max(maxProfit, prices[i] - buy)
                print(maxProfit)
        print(maxProfit)
        return maxProfit if maxProfit else 0

