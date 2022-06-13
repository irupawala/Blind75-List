class Solution:
    def maxProduct(self, nums) -> int:
        result = nums[-1]
        next_element = (result, result)
        
        for i in range(len(nums)-2, -1, -1):
            
            _min, _max = nums[i], nums[i]            
            for no in next_element:
                product = no*nums[i]
                _max = max(product, _max)
                _min = min(product, _min)
                    
            result = max(_max, result)
            next_element = (_min, _max)
        
        return result

'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
