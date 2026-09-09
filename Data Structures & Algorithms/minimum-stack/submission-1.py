class MinStack:

    def __init__(self):
        self.items = []
        self.minitems = []
        

    def push(self, val: int) -> None:
        self.items.append(val)
        val = min(val, self.minitems[-1] if self.minitems else val)
        self.minitems.append(val)

    def pop(self) -> None:
        self.items.pop()
        
    def top(self) -> int:
        return self.items[-1]
        
    def getMin(self) -> int:
        return self.minitems[-1]

        
