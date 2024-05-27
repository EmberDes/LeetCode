class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while(i < n):
            correct = nums[i]-1
            if(nums[i]!=nums[correct]):
                temp = nums[i]
                nums[i]=nums[correct]
                nums[correct] = temp
            else:
                i += 1
        print(nums)
        l=[]
        a =1
        for c in nums:
            if c != a:
                l.append(a)
                a +=1
            else:
                a +=1
        return l
                