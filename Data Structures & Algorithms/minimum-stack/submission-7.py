class MinStack:

    def __init__(self):
        self.stack = []
        self._min = None

    def push(self, val: int) -> None:
        if self._min == None or self._min > val:
            self._min = val
        self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()

        if self.stack and val == self._min:
            self._min = min(self.stack)

        if not self.stack:
            self._min = None

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min
        
