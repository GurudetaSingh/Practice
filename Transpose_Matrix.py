# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:        
        result = []
        
        for i in range(len(matrix[0])):
            tmp = []
            for j in range(len(matrix)):
                tmp.append(matrix[j][i])
            
            result.append(tmp)
        
        return result
      
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:        
        return zip(*matrix)
        
