class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # x = 0
        # steps = 0
        # while x < len(cost) - 1:
        #     # minimum = min(cost[x], cost[x+1])
        #     # pos1 = cost[x]
        #     # pos2 = cost[x+1]
        #     if cost[x] < cost[x+1]:
        #         x += 1
        #     else:
        #         x += 2
        #     # x += cost[x] if cost[x] < const[x+1] else cost[x+1]
        #     # steps =
        # return x 
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1],
                    dp[i-2]+cost[i-2])
        return dp[n]
