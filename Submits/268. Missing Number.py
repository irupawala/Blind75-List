'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return(list(set(range(len(nums)+1)) - set(nums)).pop())
'''        
        
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _total = sum(range(len(nums)+1))
        return _total - sum(nums)      
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
