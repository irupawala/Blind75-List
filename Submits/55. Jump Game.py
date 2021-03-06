# Neetcode Solution
class Solution:
    def canJump(self, nums) -> bool:
        goal = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= goal:
                goal = i
        
        return goal == 0
            

        
# Excellent Solution        
'''
class Solution:
    def canJump(self, nums) -> bool:
        j = 0
        
        for i, x in enumerate(nums):
            if j < i: return False
            j = max(j, i+x)
        
        return True         
'''

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
