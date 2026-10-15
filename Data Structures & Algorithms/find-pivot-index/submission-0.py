class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        ls = 0
        for i in range(len(nums)):
            rs = total - nums[i] - ls
            if ls == rs:
                return i
            ls += nums[i]
        return -1