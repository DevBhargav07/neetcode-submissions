import copy
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort to get the max and second max numbers to get the difference of the two maximum numebrs
        # for every iteration finding the max and minimum
        # taking the maximum - minimum and adding in the mini postion id
        # removing the max
        # iterate it through all the elements until length < 2
        # dummy = copy.deepcopy(stones)
        while len(stones) > 1:
            stones.sort()
            curr = stones.pop() - stones.pop()
            if curr:
                stones.append(curr)
        return stones[0] if stones else 0


        