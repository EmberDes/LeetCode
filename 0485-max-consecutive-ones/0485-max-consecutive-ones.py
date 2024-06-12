class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mCnt = 0
        cnt = 0
        for i in nums:
            if i == 1:
                cnt+=1
            else:
                cnt =0
            mCnt = max(mCnt,cnt)
        
        return mCnt
        