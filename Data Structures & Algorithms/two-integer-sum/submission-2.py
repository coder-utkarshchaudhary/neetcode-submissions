class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        _map = {nums[i]:i for i in range(n)}
        for idx in range(n):
            if target-nums[idx] in _map and idx!=_map[target-nums[idx]]:
                return [idx, _map[target-nums[idx]]]
        
        return [-1,-1]
