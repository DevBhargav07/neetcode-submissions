class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.items = nums
        self.k = k
        
    def add(self, val: int) -> int:
        self.items.append(val)
        self.items.sort()
        return self.items[len(self.items) - self.k]



