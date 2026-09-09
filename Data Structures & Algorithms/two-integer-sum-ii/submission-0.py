class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i , j = 0, 1
        while j < len(numbers):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            i += 1
            j += 2
        return [-1, -1]