class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
                return 0
        
        m,n=len(grid),len(grid[0])
        diag=[(1,0),(-1,0),(0,1),(0,-1)]
        islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    islands+=1
                    q=deque([(i,j)])
                    grid[i][j]='0'
                    while q:
                        r,c=q.popleft()
                        for dr,dc in diag:
                            nr,nc=r+dr,c+dc
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':
                                grid[nr][nc]='0'
                                q.append((nr,nc))
        
        return islands