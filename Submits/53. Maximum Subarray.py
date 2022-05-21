class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for val in nums[1 : ]:
            curSum = max(val, curSum + val)
            maxSum = max(maxSum, curSum)
        return maxSum
    

'''
NeetCode
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        
        total = 0
        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
'''

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
