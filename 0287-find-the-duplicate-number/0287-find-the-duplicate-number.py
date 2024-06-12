class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         not according to the given constraint 
        # l = set()
        # for char in nums:
        #     if char not in l:
        #         l.add(char)
        #     else:
        #         return char
        # return 0
        slow ,fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                break
        slow2=0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            