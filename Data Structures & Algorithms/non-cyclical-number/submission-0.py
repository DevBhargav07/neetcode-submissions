class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        while n > 0:
            e = n % 10
            n //= 10
            sum += e * e;
        return sum == 1