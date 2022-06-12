class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        dp = [None] * len(nums)       
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(2, len(nums)):
            max_pre_rob = 0
            dp[i] = nums[i] + max(dp[:i-1])
            
        return max(dp)

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''

 #NeetCode Solution  
 '''   
 class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
   '''
