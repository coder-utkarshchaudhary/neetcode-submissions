class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l, h = 1, x
        while l<=h:
            m = (l+h)//2
            if m*m==x :
                return m
            if m*m<x:
                l=m+1
                ans = m
            else:
                h=m-1
        
        return ans