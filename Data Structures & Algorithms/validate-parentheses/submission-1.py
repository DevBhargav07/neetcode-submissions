class Solution:
    def isValid(self, s: str) -> bool:
        param = {")": "(", "}": "{", "]": "["}
        stack = []
        for p in s:
            if p in param.values():
                stack.append(p)
            elif p in param:
                if not stack or stack.pop() != param[p]:
                # stack.pop()
                    return False
        return not stack
            
        