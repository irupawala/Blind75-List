class Solution:
    def spiralOrder(self, matrix):
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        result = []
        
        l, r = 0, COLUMNS
        top, bottom = 0, ROWS
        total_count = ROWS * COLUMNS
        
        while l < r and top < bottom:
            
            for i in range(l, r-1):
                result.append(matrix[top][i])
                
            for i in range(top, bottom):
                result.append(matrix[i][r-1])
                
            if len(result) == total_count: return result
                
            for i in range(r-2, l-1, -1):
                result.append(matrix[bottom-1][i])
                
            for i in range(bottom-2, top, -1):
                result.append(matrix[i][l])
                
            r -= 1
            l += 1
            bottom -= 1
            top += 1
        
        return result
