class Solution:
    def climbStairs(self, n: int) -> int:
        # a logic of fibonacci series hiden
        # adding the previous two values
        if n < 3:
            return n
        prev2 = 1
        prev1 = 2
        for i in range(2, n):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1