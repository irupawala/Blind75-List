class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
                
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):           
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        
        return dp[len(text2)][len(text1)]

 '''
 Time Complexity - O(n*m)
 Space Complexity - O(n*m)
 '''
