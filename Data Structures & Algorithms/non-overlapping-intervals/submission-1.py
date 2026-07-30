class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        currE = intervals[0][1]
        drop=0
        for interval in intervals[1:]:
            if interval[0] >= currE:
                currE = interval[1]
            else:
                drop+=1
        
        return drop