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
        for s in strs:
            encoded_str += s + ":;|"
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, strs):
        # write your code here
        strs = strs.split(":;|")
        return strs[:-1]