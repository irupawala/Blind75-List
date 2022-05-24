class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            _sum = numbers[start] + numbers[end]
            if _sum == target: return [start+1, end+1]
            if _sum > target: end -= 1
            else: start += 1
        
'''
Time Complexity - O(n)
Space Complexity - O(1)
'''
