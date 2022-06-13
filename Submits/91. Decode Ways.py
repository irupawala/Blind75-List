class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        if len(s) == 1: return 1
        
        dp = { len(s) : 1 }
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1] # for length of first substring 1
            
            print(int(s[i:i+2]))
            if (i+1< len(s) and (int(s[i:i+2]) in range(10,27))): # for length of first substring 2
            #if (i+1< len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                dp[i] += dp[i+2]
        
        return dp[0]

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
