class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        subsum = 0
        
        for n in nums:
            
            
            if  subsum<0:
                    subsum =0
            subsum += n
            maxsum = max(maxsum,subsum)
        return maxsum
        