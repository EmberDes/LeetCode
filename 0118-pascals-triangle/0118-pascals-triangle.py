class Solution(object):
    def generate(self, numRows):
        def generateRow(row):
            ans = 1
            ansRow = [1] #inserting the 1st element

            #calculate the rest of the elements:
            for col in range(1, row):
                ans *= (row - col)
                ans //= col
                ansRow.append(ans)
            return ansRow
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ans = []

        #store the entire pascal's triangle:
        for row in range(1, numRows+1):
            ans.append(generateRow(row))
        return ans
        
       
        
        
        
    