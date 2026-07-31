class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     current = nums[left] + nums[right]
        #     print(current)
        #     if current == target:
        #         return [left, right]
        #     elif current < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []
        seen = {}

        for i, val in enumerate(nums):
            complement = target - val

            if complement in seen:
                return [seen[complement], i]

            seen[val] = i
        return []