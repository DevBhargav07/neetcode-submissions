class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force method
        # n = len(arr)
        # ans = [0] * n
        # for i in range(n):
        #     rightMax = -1
        #     for j in range(i + 1, n):
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax
        # return ans

        # by following the method to traverse from right to left
        n = len(arr)
        ans = [0] * n
        rightMax = -1
        for i in range(n - 1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans