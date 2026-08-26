class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mintime, maxtime = 1, max(piles)
        ans = maxtime
        while mintime<=maxtime:
            m = (mintime+maxtime)//2
            hours  = 0
            for i in piles:
                hours += math.ceil(float(i)/m)
            if hours>h:
                mintime = m+1
            else:
                ans = m
                maxtime = m-1
        
        return ans