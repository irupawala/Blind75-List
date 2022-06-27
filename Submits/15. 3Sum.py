class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: continue
            target = 0 - nums[i]
            j,k = i+1, len(nums)-1

            while j < k:
                _sum = nums[j] + nums[k]
                if _sum > target: k-=1
                elif _sum < target: j+=1
                else:
                    result.append([nums[i], nums[j], nums[k]])                            
                    j += 1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1

        return result

    
# Ibrahim Solution inspired from Grokking
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()
        self.nums = nums
        self.res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue # to avoid duplicates
            self.two_sum_zero(i, i+1)
        return self.res
            
    def two_sum_zero(self, i, left):
        target_sum = 0 - self.nums[i]
        right = len(self.nums)-1
        
        while left < right:              
            _sum = self.nums[left] + self.nums[right]
            
            if _sum == target_sum: 
                self.res.append([self.nums[i], self.nums[left], self.nums[right]]) 
                left += 1
                
                while self.nums[left] == self.nums[left-1] and left < right: # necessary to avoid duplicates, right will take care of itself 
                    left += 1
                #right -= 1
                #while self.nums[right] == self.nums[right+1] and left < right:
                #    right -= 1

            if _sum < target_sum:
                left += 1
                
            elif _sum > target_sum:
                right -= 1
                
        return None
'''    
    
    
'''
Time Complexity - nlog(n) + O(n^2) (Two inner loops) =~ O(n^2)
Space Complexity - O(1) or O(n) (because some libraries take O(n) for sorting)
'''
