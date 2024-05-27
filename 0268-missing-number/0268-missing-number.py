class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while (i < n):
            correct = nums[i]
            if nums[i]<len(nums)-1 and nums[i] != nums[correct] :
                temp = nums[i]
                nums[i]=nums[correct]
                nums[correct]=temp
            else:
              i = i +1
        a=0
        for c in nums:
            if c != a:
                return a
            else:
                a += 1
        
        return n
                