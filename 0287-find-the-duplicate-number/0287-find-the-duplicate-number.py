class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for char in nums:
            if char not in l:
                l.add(char)
            else:
                return char
        return 0