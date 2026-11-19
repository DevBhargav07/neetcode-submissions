class Solution:
    def is_prime(self, n: int) -> bool:
        for i in range(2, n//2+1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for num in range(2, n):
            if self.is_prime(num):
                count += 1
        return count