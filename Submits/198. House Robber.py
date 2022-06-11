class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        dp = [None] * len(nums)       
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(2, len(nums)):
            max_pre_rob = 0
            dp[i] = nums[i] + max(dp[:i-1])
            
        return max(dp)
