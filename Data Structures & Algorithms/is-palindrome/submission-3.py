class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ''.join(filter(str.isalnum, s))
        return rev.lower() == rev[::-1].lower()