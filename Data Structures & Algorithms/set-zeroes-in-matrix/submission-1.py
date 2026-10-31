class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_with_0 = []
        col_with_0 = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_with_0.append(i)
                    col_with_0.append(j)
        
        for r in row_with_0:
            for j in range(n):
                matrix[r][j]=0

        for c in col_with_0:
            for i in range(m):
                matrix[i][c]=0