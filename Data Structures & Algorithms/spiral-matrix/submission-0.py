class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1

        ans = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            for j in range(top, bottom+1):
                ans.append(matrix[j][right])
            right-=1

            if not (left <= right and top <= bottom):
                break
                
            for k in range(right, left-1, -1):
                ans.append(matrix[bottom][k])
            bottom-=1

            for m in range(bottom, top-1, -1):
                ans.append(matrix[m][left])
            left+=1
        
        return ans