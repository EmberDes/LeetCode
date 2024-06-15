# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         dp = [n] * (n+1)
#         dp[0] = 0
        
#         for target in range(1, n+1):
#             for s in range(1,target):
#                 square = s * s
#                 if target - square < 0:
#                     break
#                 dp[target] = min(dp[target],1 + dp [target - square])
        
        
#         return dp[n]
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [n] * (n + 1)
        dp[0] = 0
        count = 1
        while count * count <= n:
            sq = count * count
            for i in range(sq, n + 1):
                dp[i] = min(dp[i - sq] + 1, dp[i])
            count += 1
        return dp[n]      