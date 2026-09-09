from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = defaultdict(int)
        for num in nums:
            if not seen[num]:
                seen[num]+=1
            else:
                return True
        
        return False