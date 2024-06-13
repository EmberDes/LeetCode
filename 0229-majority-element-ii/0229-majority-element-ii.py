class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cn1,el1 = 0 ,float('-inf')
        cn2,el2 =0 , float('-inf')
        for i in nums:
            if cn1 == 0 and i!=el2:
                el1 = i
                cn1 +=1
            elif cn2 == 0 and i!=el1:
                el2 = i
                cn2 +=1
            
            elif i == el1 :
                cn1 +=1
            elif i == el2:
                cn2 +=1
            else:
                cn1 -=1
                cn2 -=1
        
        ls=[]
        cnt1, cnt2 = 0, 0
        for i in nums:
            if i == el1:
                cnt1 += 1
            if i == el2:
                cnt2 += 1

        mini = int(len(nums) / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        return ls
            