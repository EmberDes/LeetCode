class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        def swap(fIndex , lIndex , n):
            print(fIndex,lIndex)
            temp = n[fIndex]
            n[fIndex] = n[lIndex]
            n[lIndex] = temp
            
        low = 0
        high = len(nums)-1
        mid  =0
        while ( mid <= high):
            currentValue = nums[mid]
            if currentValue == 0:
                swap(low , mid ,nums)
                mid +=1
                low +=1
            elif currentValue == 1:
                mid +=1
            elif currentValue == 2:
                swap(mid,high,nums)
                high -=1
                
            
    
            