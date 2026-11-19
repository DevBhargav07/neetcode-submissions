class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        # every new thing is going to get the :;| - for merging
        # space? :;  
        # properties = {"append": ":;|", " ": ":;"}
        encoded_str = ""
        replace_strs = {"e": "$", "l": "^", "o": "{", "O": "}", "a": "[", "b": "]"}
        for s in strs:
            temp = ''
            for i in range(len(s)):
                temp += replace_strs.get(s[i], s[i])
            s = temp
            encoded_str +=  s + ":;|"
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        decode_strs = {"$": "e", "^": "l", "{": "o", "}": "O", "[": "a", "]": "b"}
        
        strs = strs.split(":;|")
        strs = strs[:-1]
        res = []
        for s in strs:
            if not s:
                continue
            temp = ''
            for i in range(len(s)):
                temp += decode_strs.get(s[i], s[i])
            # s = temp
            res.append(temp)

        return res if res else [""]