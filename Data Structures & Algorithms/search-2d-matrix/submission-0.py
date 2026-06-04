class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        t=m*n
        r=t-1
        l=0

        while l<=r:
            m=(l+r)//2
            i=m//n
            j=m%n

            mid=matrix[i][j]

            if target==mid:
                return True
            
            elif target<mid:
                r=m-1
            else:
                l=m+1
        return False
