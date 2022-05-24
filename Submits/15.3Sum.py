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
    
'''
Time Complexity - nlog(n) + O(n^2) (Two inner loops) =~ O(n^2)
Space Complexity - O(1) or O(n) (because some libraries take O(n) for sorting)
'''
