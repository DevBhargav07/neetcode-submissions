class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # tracing with two pointers
        i, counter = 0, 0
        maximum = 0
        while i <= len(nums) - 1:
            if nums[i] != 1:
                counter = 0
            else:
                counter += 1
            maximum = max(maximum, counter)
            i+=1
        return maximum

