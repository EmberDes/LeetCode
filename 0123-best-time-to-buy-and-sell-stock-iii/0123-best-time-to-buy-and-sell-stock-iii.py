class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        
        def dfs(i,buying,cap) :
            if i >= len(prices) or cap>2:
                return 0
            if (i,buying,cap) in dp:
                return dp[(i,buying,cap)]
            
            if buying:
                buy = dfs(i+1,not buying,cap+1)-prices[i]
                cooldown = dfs(i+1, buying,cap)
                dp[(i,buying,cap)] = max(buy,cooldown)
            else:
                sell = dfs(i+1,not buying,cap) + prices[i]
                cooldown = dfs(i+1, buying,cap)
                dp[(i,buying,cap)] = max(sell,cooldown)
            
            return dp[(i,buying,cap)]
        
        return dfs(0,True,0)