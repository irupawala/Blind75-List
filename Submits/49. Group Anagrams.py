from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        ans = []
        heap = []
        
        for num in set_nums: 
            heappush(heap, [-nums.count(num), num])
            
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans
        
'''
Time Complexity - O(unique_nums*log(unique_nums) + O(k*unique_nums)
Space Complexity - O(unique_nums)
'''
