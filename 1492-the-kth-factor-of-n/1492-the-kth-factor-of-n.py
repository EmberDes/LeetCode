class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fact =[]
        count=0
        for i in range(1,n+1):
            if n % i ==0:
                fact.append(i)
                count +=1
                if count == k:
                    return i
        return -1
        
        