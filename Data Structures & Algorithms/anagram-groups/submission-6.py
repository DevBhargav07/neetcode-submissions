class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS].append(s)
        return list(res.values()) # O(m*n logn)
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     # print(res[tuple(count)].append(s))
        #     res[tuple(count)].append(s)
        # return list(res.values()) # O(m*n)