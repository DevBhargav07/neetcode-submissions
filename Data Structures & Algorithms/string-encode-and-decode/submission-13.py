class Solution:
    string = ":;|"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + self.string
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split(f"{self.string}")
        return res[:-1]