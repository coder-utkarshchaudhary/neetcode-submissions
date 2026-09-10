from bisect import bisect_right

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        idx = bisect_right(nums, 0)
        n = len(nums)

        if idx == n:
            return 1
        
        seen = set()
        cnt = 1
        for i in range(idx, n):
            if nums[i]!=cnt:
                if nums[i] in seen:
                    continue
                else:
                    return cnt
            else:
                seen.add(cnt)
                cnt+=1
        
        return cnt
        