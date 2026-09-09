class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting the lists
        nums.sort()
        freq = []
        for i in range(len(nums)-1, 0, -1):
            if len(freq) < k:
                if nums[i] not in freq and nums[i] == nums[i-1]:
                    freq.append(nums[i])
        return freq