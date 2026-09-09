class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we will use brute force method dual for loop
        res = [0] * len(temperatures) 
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j] and res[i] == 0:
                    res[i] = j - i
        return res
        # i = 0
        # j = 1
        # res = []
        # while j < len(temperatures):
        #     if temperatures[i] < temperatures[j]:
        #         res.append(j)
        #         # i+=1
        #     else:
        #         j += 1
        # return res
