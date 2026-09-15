class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        using predefined code
        """
        # s = s.strip().split()
        # return len(s[-1])
        # works 
        """
        Using iterative method
        """
        counter = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if counter:
                    break
                pass
            else:
                counter += 1
        return counter
