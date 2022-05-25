'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string_len, i = 0, 0
        substring = []

        while i < len(s):        
            if s[i] not in substring :
                substring.append(s[i])              
            else: 
                i = i - len(substring) 
                substring = []
            i += 1
            max_string_len = max(max_string_len, len(substring))   

        return max_string_len   
'''


'''
Time Complexity - O(n^2)
Space Complexity - O(n)
'''

# Neet Code O(n) Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = list() # set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.append(s[r]) #charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


'''
Time Complexity - O(n2)
Space Complexity - O(n)
'''
    
