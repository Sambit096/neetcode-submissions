from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh=0
        m,n=len(grid),len(grid[0])
        EMPTY,ROTTEN,FRESH=0,2,1
        q=deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==ROTTEN:
                    q.append((i,j))
                elif grid[i][j]==FRESH:
                    num_fresh+=1
        if num_fresh==0:
            return 0
        min_minutes=-1
        while q:
            max_length=len(q)
            min_minutes+=1
            for _ in range(max_length):
                i,j=q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if(0<=r<m and 0<=c<n and grid[r][c]==FRESH):
                        grid[r][c]=ROTTEN
                        num_fresh-=1
                        q.append((r,c))
        if num_fresh==0:
            return min_minutes
        else:
            return -1

