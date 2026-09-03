class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.items = []

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append(0)
            self.min = val
        else:
            self.items.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.items:
            return
        pop = self.items.pop()
        if pop < 0:
            self.min = self.min - pop


    def top(self) -> int:
        peek =  self.items[-1]
        if peek > 0:
            return peek + self.min
        return self.min

    def getMin(self) -> int:
        return self.min
