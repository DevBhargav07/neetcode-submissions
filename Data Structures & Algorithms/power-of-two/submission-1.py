class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        while n and n>1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True
