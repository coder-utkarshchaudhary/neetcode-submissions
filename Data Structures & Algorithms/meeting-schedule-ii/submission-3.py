"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals)==1:
            return 1
            
        intervals.sort(key=lambda x: x.start)
        n, num_rooms = len(intervals), 1
        latest_ends = [intervals[0].end]
        for i in range(1, n):
            currS, currE = intervals[i].start, intervals[i].end
            if num_rooms==1:
                if currS>=latest_ends[0]:
                    latest_ends[0]=currE
                else:
                    num_rooms+=1
                    latest_ends.append(currE)
            else:
                for j in range(num_rooms):
                    if latest_ends[j] <= currS:
                        latest_ends[j]=currE
                        break
                else:
                    num_rooms+=1
                    latest_ends.append(currE)
        
        return num_rooms