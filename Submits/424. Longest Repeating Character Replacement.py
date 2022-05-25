'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        charset = {}

        for r in range(len(s)):
            charset[s[r]] = 1 + charset.get(s[r], 0)
            while ((r-l+1) - max(charset.values())) > k:
                   charset[s[l]] -= 1
                   l += 1
            res = max(res, r-l+1)

        return res
'''

'''
Time Complexity - O(26*n) --> Max 26 alphabets to search the max repeating char value
Space Complexity - O(unique_elements)
'''


# NeetCode O(n) Solution 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        charset = {}
        maxFreq = 0

        for r in range(len(s)):
            charset[s[r]] = 1 + charset.get(s[r], 0)
            maxFreq = max(maxFreq, charset[s[r]])
            
            while ((r-l+1) - maxFreq) > k:
                   charset[s[l]] -= 1
                   l += 1
                
            res = max(res, r-l+1)

        return res


'''
Time Complexity - O(n) 
Space Complexity - O(unique_elements)
'''
