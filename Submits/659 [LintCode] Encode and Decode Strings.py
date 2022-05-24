class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        single_str = "*&^".join(map(str, strs))
        return single_str

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        decoded_str = list(str.split("*&^"))
        return decoded_str
