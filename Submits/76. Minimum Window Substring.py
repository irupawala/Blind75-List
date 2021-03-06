class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(s) + 1
        char_frequency = {}
         
        for chr in t:
            if chr not in char_frequency: 
                char_frequency[chr] = 0
            char_frequency[chr] += 1
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0: # count every matching of char
                    matched += 1 
                    
            while matched == len(t):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        if min_length > len(s): return ""
        return s[substr_start:substr_start + min_length]
            

'''
Time Complexity - O(s+t)
Space Complexity - O(t)
'''
