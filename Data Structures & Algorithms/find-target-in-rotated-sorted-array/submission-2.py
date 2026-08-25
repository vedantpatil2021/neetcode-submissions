class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[l] == target:
                return l
            if nums[m] == target:
                return m
            if nums[r] == target:
                return r
            else:
                l = l + 1
                r = r - 1

        
        return -1   

