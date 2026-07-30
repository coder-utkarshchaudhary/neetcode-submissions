class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        def dfs(i, j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
                return 0
            
            area = 1
            grid[i][j] = 0
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in dirs:
                nx,ny=i+dx,j+dy
                area+=dfs(nx,ny)

            return area

        if not grid:
            return 0
        
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area