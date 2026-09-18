class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # decimal_a = int(a, 2)
        # decimal_b = int(b, 2)
        # decimal_sum = decimal_a + decimal_b
        # return bin(decimal_sum)[2:]

        # using iteration
        res = []
        carry = 0
        i,j = len(a) -1, len(b) - 1
        while i >=0 or j >=0 or carry:
            digitA = int(a[i]) if i >= 0 else 0
            digitB = int(b[j]) if j >= 0 else 0
            total = digitA + digitB + carry
            res.append(total % 2)
            carry =  total // 2

            i -= 1
            j -= 1
        res.reverse()
        return ''.join(map(str,res))
