class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        colm = len (matrix[0])
        
        low = 0
        high = row * colm -1
        
        while low <= high:
            mid = (low +high)//2
            print (mid)
            if target == matrix [mid//colm][mid%colm]:
                return True
            elif target >= matrix [mid//colm][mid%colm]:
                low = mid +1
            
            elif target <= matrix [mid//colm][mid%colm]:
                high = mid -1
        
        return False
        