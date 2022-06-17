class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals = sorted(intervals, key = lambda x: x[1]) 
        # Note that it is important to sort by end value here because we want to remove the segment which ends first
        count = 0
        
        last = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            
            if cur_start < last[1]:
                count+=1 # increase count if merging and keep the last same
            else:
                last = intervals[i] # last = current if non-overlapping
                
        return count

# Alternative way to make sure that we're removing the one which ends first is to sort and then start traversing the list from the end

'''
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        count = 0
        
        last = intervals[-1]
        for i in range(len(intervals)-2, -1, -1):
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            
            if cur_end > last[0]:
                count+=1 # increase count if merging and keep the last same
            else:
                last = intervals[i] # last = current if non-overlapping
                
        return count
'''    

'''
Time Complexity - O(nlogn) + O(n)
Space Complexity - O(1)
'''
