class Solution:

    def findPivot(self,lst):
        l,r = 0, len(lst)-1

        while r > l:
            m = l + (r - l)//2
            if lst[r] > lst[l]: r = m                           
            else:
                if r - l == 1: return r
                if lst[m] > lst[l]: l = m
                else: r = m   
        return 0    
    
    def Binarysearch(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if target == nums[m]: return m
            if nums[m] > target: r = m-1
            else: l = m+1

        return -1
   
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        
        result = self.Binarysearch(nums[0:pivot], target) 
        if result != -1: return result
        
        result = self.Binarysearch(nums[pivot:], target) 
        if result != -1: return result+pivot
        
        return -1    

'''
Time Complexity - O(logn) + O(logn/2) + O(logn/2) =~ logn
Space Complexity - O(1)
'''
