class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1,2,3,3]
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        


        