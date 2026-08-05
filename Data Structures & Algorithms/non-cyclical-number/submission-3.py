class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        while n > 0:
            e = n % 10
            n //= 10
            sum += e * e;
        if sum == 1:
            return True
        elif 1 < sum <= 9:
            return False
        return self.isHappy(sum)