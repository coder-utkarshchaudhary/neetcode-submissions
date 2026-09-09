class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, j = 0, n
        while i<j:
            if nums[i]!=val:
                i+=1
            else:
                j-=1
                nums[i] = nums[j]
        
        return j