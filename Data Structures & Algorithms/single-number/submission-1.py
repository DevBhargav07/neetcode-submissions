class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using O(n) and O(1) with ^ expression
        res = 0
        for i in nums:
            res ^= i
        return res
        # this O(n) & O(n)
        # duplicates = dict()
        # for i in nums:
        #     duplicates[i] = duplicates.get(i, 0) + 1
        # num = [num for num, cnt in duplicates.items() if cnt == 1]
        # # print(num)
        # return num[0]
        

        