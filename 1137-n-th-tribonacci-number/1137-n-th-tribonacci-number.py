class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2 :
            return 1
        one,two,three = 0,1,1
        for i in range(n-2):

            temp1 = three
            temp2 = two
            three = one+two+three
            two = temp1
            one = temp2
        return three 
        