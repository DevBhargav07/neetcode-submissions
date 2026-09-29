class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n + 1)
        for i in nums:
            if 1 <= i <= n:
                ans[i] = 1
        return [i for i in range(1, n+1) if ans[i]==0]