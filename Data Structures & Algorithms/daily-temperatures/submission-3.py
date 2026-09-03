class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # using stack for this 
        # 1. take the res with [0] values for all positions
        # 2. take stack to store temp and index
        # 3. iterate the temps
        # 4. check stack is not empty and stack top temperate is less than the current temp
        # 5. take that and add that to res in res[ind] 
        # 6. Add that value to stack
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd # to get the diff in indexes
            stack.append((t, i))
        return res
            
        # we will use brute force method dual for loop
        # res = [0] * len(temperatures) 
        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i] < temperatures[j] and res[i] == 0:
        #             res[i] = j - i
        # return res
        # i = 0
        # j = 1
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n - 2, -1, -1):
        #     j = i + 1
        #     while j < n  and temperatures[j] <= temperatures[i]:
        #         if res[j] == 0:
        #             j = n
        #             break
        #         j += res[j]
            
        #     if j < n:
        #         res[i] = j - i
        #             # i+=1
        #         # else:
        #         #     j += 1
        # return res
