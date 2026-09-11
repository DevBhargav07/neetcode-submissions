class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and not counter:
                pass
            elif s[i] == " " and counter:
                break
            else:
                counter += 1
        return counter
            