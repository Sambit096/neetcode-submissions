from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands_visited=0
        m,n=len(grid),len(grid[0])
        
        def bfs(si: int, sj: int)->None:
            q=deque()
            q.append((si, sj))
            grid[si][sj]='0'
            while q:
                i,j=q.popleft()
                for ni, nj in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        grid[ni][nj] = '0'
                        q.append((ni, nj))
               
                    

                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    islands_visited+=1
                    bfs(i,j)
        return islands_visited
        