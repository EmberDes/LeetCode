class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        if x < 0:
            r = -1
            temp = -1*temp
        else :
            r= 1 
        new=0

        while (temp >0):
            new = new *10 + temp%10
            temp =temp//10 
        
        if new < -2**31 or new > 2**31 - 1:
            return 0
        return(r*new)

        