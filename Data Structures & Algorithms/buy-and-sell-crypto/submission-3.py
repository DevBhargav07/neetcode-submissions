class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy = 0
        # maxProfit = 0
        # for i in range(len(prices)-1):
        #     if prices[i] < prices[i+1] and not buy:
        #         buy = prices[i]
        #     if buy and prices[i] > prices[i + 1]:
        #         # print(prices[i], buy)
        #         # return prices[i] - buy
        #         maxProfit = max(maxProfit, prices[i] - buy)
        #         # print(maxProfit)
        # # last = prices[-1]

        # # print(maxProfit)
        # # maxProfit = max(maxProfit, prices[-1] - buy)
        # return maxProfit if maxProfit else 0

        left = 0
        right = len(prices) - 1
        buy = 0
        profit = 0
        while left < right:
            if not buy and prices[left] < prices[left+1]:
                buy = prices[left]
                # left += 1
            if prices[right] > prices[right - 1]:
                print(profit, prices[right], buy)
                profit = max(profit, prices[right] - buy)
                right -= 1
            left += 1
            right -= 1
        return profit


