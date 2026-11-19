class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for n in nums:
            if n in unique:
                return False
            unique.add(n)
        return True