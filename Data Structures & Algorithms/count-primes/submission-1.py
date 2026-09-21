class Solution:
    # def is_prime(self, n: int) -> bool:
    #     for i in range(2, n//2+1):
    #         if n % i == 0:
    #             return False
    #     return True

    def countPrimes(self, n: int) -> int:
        # count = 0
        # for num in range(2, n):
        #     if self.is_prime(num):
        #         count += 1
        # return count

        #sieve of Eratosthenes
        sieve = [False] * n
        res = 0
        for num in range(2, n):
            if not sieve[num]:
                res += 1
                for i in range(num * num, n, num):
                    sieve[i] = True
        return res