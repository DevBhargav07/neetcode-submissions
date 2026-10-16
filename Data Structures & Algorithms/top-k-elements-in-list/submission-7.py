class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # return [v for v, c in count.most_common(k)]

        # using bucket sorting method
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for n in range(len(freq)-1 , -1, -1):
            for i in freq[n]:
                res.append(i)
            if len(res) == k:
                return res
