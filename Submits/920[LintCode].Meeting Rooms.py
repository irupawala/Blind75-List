from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda x: x.start)
        length = len(intervals) - 1
        for i in range(length):
            end_time = intervals[i].end
            start_time = intervals[i+1].start

            if end_time > start_time: return False
        
        return True
        
        return True
