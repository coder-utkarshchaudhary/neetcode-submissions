"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        if len(intervals)==1:
            return True
                
        intervals.sort(key=lambda x: x.start)
        current_end = intervals[0].end
        for i in range(1, len(intervals)):
            currs, curre = intervals[i].start, intervals[i].end
            if currs<current_end:
                return False
            else:
                current_end=curre
            
        return True