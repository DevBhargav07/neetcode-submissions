class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # tracing with two pointers
        # i, counter = 0, 0
        # maximum = 0
        # while i <= len(nums) - 1:
        #     if nums[i] != 1:
        #         counter = 0
        #     else:
        #         counter += 1
        #     maximum = max(maximum, counter)
        #     i+=1
        # return maximum


        # optmizing the use of maximum
        total = maxi = 0
        for num in nums:
            maxi = maxi + 1 if num else 0
            total = max(total, maxi)
        return total

