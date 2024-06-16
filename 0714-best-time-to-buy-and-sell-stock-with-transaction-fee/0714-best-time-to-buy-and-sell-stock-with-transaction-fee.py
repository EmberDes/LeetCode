# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
        
        
#         dp = {}
        
#         def dfs(i,buying) :
#             if i >= len(prices):
#                 return 0
#             if (i,buying) in dp:
#                 return dp[(i,buying)]
            
#             if buying:
#                 buy = dfs(i+1,not buying)-prices[i]
#                 cooldown = dfs(i+1, buying)
#                 dp[(i,buying)] = max(buy,cooldown)
#             else:
#                 sell = dfs(i+1,not buying) + prices[i]-fee
#                 cooldown = dfs(i+1, buying)
#                 dp[(i,buying)] = max(sell,cooldown)
            
#             return dp[(i,buying)]
        
#         return dfs(0,True)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # Initialize the minimum price with the first stock price plus fee
        min_price = prices[0] + fee
        # Initialize the maximum profit as 0
        max_profit = 0
        
        # Iterate over each stock price
        for price in prices:
            # If the current price is greater than the minimum price,
            # a profit can be made by selling the stock
            if min_price < price:
                # Add the difference between the current price and the minimum price
                # to the maximum profit
                max_profit += price - min_price
                # Update the minimum price to the current price
                min_price = price
            # If the current price plus fee is less than the minimum price,
            # update the minimum price to the current price plus fee
            elif price + fee < min_price:
                min_price = price + fee
        
        # Return the maximum profit
        return max_profit
        