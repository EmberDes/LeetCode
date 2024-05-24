class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_val = 1
        r_val = 1
        n = len(nums)
        l_arr=[0]*n
        r_arr = [0]*n
        
        for i in range(n):
            j =-i-1
            l_arr[i]=l_val
            r_arr[j]=r_val
            l_val = l_val * nums[i]
            r_val = r_val * nums[j]
            
        return[l*r for l,r in zip(l_arr,r_arr)]
        