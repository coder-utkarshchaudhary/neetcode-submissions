class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)
        
        for r in range(n):
            s, e = 0, n-1
            while s<e:
                matrix[r][s], matrix[r][e] = matrix[r][e], matrix[r][s]
                s+=1
                e-=1