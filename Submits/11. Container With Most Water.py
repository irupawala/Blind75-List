class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        max_area = 0
        
        while end-start > 0:
            area = min(height[start], height[end]) * (end-start)
            max_area = max(max_area, area)
            
            if height[start] <= height[end]: start+=1
            else: end-=1
        
        return max_area
    
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
