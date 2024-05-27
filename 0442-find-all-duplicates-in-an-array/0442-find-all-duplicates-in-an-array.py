class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l =set()
        ans = []
        for ch in nums:
            if ch not in l:
                l.add(ch)
            else:
                ans.append(ch)
        return ans
        