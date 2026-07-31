class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        i=0
        count=1
        n=len(nums)
        for i in range(n):
            place = nums.pop(i)
            out.append(math.prod(nums))
            nums.insert(i, place)

        return out
    
