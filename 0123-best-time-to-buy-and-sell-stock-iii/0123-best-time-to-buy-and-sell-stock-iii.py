# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         dp = {}
        
#         def dfs(i,buying,cap) :
#             if i >= len(prices) or cap>2:
#                 return 0
#             if (i,buying,cap) in dp:
#                 return dp[(i,buying,cap)]
            
#             if buying:
#                 buy = dfs(i+1,not buying,cap+1)-prices[i]
#                 cooldown = dfs(i+1, buying,cap)
#                 dp[(i,buying,cap)] = max(buy,cooldown)
#             else:
#                 sell = dfs(i+1,not buying,cap) + prices[i]
#                 cooldown = dfs(i+1, buying,cap)
#                 dp[(i,buying,cap)] = max(sell,cooldown)
            
#             return dp[(i,buying,cap)]
        
#         return dfs(0,True,0)

class Solution:
    def maxProfit(self, prices):
        s1 = s2 = 0
        b1 = b2 = -float("inf")
        for p in prices:
            if -p > b1: b1 = -p
            if b1 + p > s1: s1 = b1 + p
            if s1 - p > b2: b2 = s1 - p
            if b2 + p > s2: s2 = b2 + p
        return s2