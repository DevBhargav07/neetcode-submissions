class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i , j = 0, 1
        # while j < len(numbers):
        #     if numbers[i] + numbers[j] == target:
        #         return [i+1, j+1]
        #     i += 1
        #     j += 2
        # return [-1, -1]
        left, right = 0, len(numbers) - 1 
        while left <= right:
            # mid = left + (right - left) // 2
            current = numbers[left] + numbers[right]
            # if numbers[mid] == target:
            if current == target:
                return [left+1, right+1]
            if current < target:
                left += 1
            else:
                right -= 1
        
        return []