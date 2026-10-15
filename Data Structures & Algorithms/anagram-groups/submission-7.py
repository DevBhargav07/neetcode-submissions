class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            curr = ''.join(sorted(string))
            anagram = anagrams.get(curr, [])
            anagram.append(string)
            anagrams[curr] = anagram
        return [r for r in anagrams.values()]
