# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        for i in range(len(pairs)-1):
            j = i + 1
            while j < 0:
                if pairs[j] < pairs[j-1]:
                    pairs[j], pairs[j-1] = pairs[j-1], pairs[j]
                    j -= 1
                else:
                    break
        # return pairs
        