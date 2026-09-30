class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [nums]
        result = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for j in self.permute(remaining):
                result.append([current]+j)
        return result