class Solution:
    splitter = ":;|"
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += s + self.splitter
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split(":;|")
        return res[:-1]