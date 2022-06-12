class Solution:
    def rob(self, nums) -> int:
        
        if len(nums) < 3: return max(nums)
        return max( self.robber_old(nums[1:]), self.robber_old(nums[:-1]) )

    def robber_old(self, nums: List[int]) -> int:

        dp = [None] * len(nums)       
        dp[0], dp[1] = nums[0], nums[1]

        for i in range(2, len(nums)):
            max_pre_rob = 0
            dp[i] = nums[i] + max(dp[:i-1])

        return max(dp)

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
