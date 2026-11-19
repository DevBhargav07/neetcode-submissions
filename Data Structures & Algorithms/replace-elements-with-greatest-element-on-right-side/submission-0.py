class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # brute force method
        for i in range(len(arr)):
            maxi = max(arr[i:])
            arr[i] = maxi
        arr[-1] = -1
        return arr

        