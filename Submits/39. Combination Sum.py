class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(candidates)
        dp = [[ [] for x in range(target+1)] for y in range(n)]
        
        # populate the sum = 0 columns
        for i in range(n):
            dp[i][0] = []
            
        # with only one candidate, with repetition we can form a subset when the required sum is multiple of the candidate
        for s in range(1, target+1):
            no = candidates[0]
            if not s % no: 
                ans = []
                for i in range(s // no): ans.append(no)
                dp[0][s].append(ans)
            #else: dp[0][s] = []      
        
        # process all the subsets for all sums
        for i in range(1,len(candidates)):
            for s in range(1, target+1):
                # exclude the number
                dp[i][s] = dp[i-1][s][:]
                # include the number, if it does not exceed the sum
                cur = candidates[i]
                if s >= cur:
                    if s - cur == 0:
                        dp[i][s].append([cur])
                    else:
                        subset_wo_s = dp[i][s-cur]
                        for lst in subset_wo_s:
                            updated_lst = lst[:]
                            updated_lst.append(cur)
                            dp[i][s].append(updated_lst)
               
        # the bottom right corner will be our answer
        return dp[n-1][target]
        
'''
Time Complexity - O(target * candidates)
Space Complexity - O(target * candidates)
'''
