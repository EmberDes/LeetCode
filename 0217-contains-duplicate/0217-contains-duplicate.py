class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s  =set()
        for f in nums:
            if f not in s:
                s.add(f)
            else: 
                return True
        return False
        