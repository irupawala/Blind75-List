class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()] 
        start, end = 0, len(s)-1
        
        while start < end:
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True

    '''
    Time Complexity - O(n)
    Space Complexity - O(n)
    '''
