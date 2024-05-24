class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n ==1:
            return n
        one,two = 0,1
        for num in range(n-1):
            temp = two
            two = one+two
            one = temp
        return two
        