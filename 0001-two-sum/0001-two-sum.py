class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in range(0,len(nums)-1):
            for b in range(a+1,len(nums)):
                if (nums[a]+nums[b]==target):
                    return [a,b]
                
        