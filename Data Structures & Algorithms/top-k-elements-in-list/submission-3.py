class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorting the lists
        # nums.sort()
        # freq = []
        # for i in range(len(nums)-1, 0, -1):
        #     if len(freq) < k:
        #         if nums[i] not in freq and nums[i] == nums[i-1]:
        #             freq.append(nums[i])
        # return freq if freq else nums
        # using counter to get the most repeated values
        count = Counter(nums)
        # print(count)
        # count = sorted(key=count, lambda x,y: y)
        count = OrderedDict(count.most_common())
        # print(count)
        res = []
        for i, val in count.items():
            # print(i, val)
            if len(res) < k:
                res.append(i)
        return res