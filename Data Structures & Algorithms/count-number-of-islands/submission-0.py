class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        def dfs(i, j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0" or grid[i][j]=="#":
                return
            
            grid[i][j] = "#"

            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in dirs:
                nx,ny=i+dx,j+dy
                dfs(nx,ny)
        
        if not grid:
            return 0
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count