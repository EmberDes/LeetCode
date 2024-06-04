class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(0,len(nums)*2):
            ans.append(nums[i % len(nums)])
        return ans
    
        