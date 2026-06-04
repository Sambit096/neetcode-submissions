class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        n=len(nums)
        def backtrack():
            #Basecase
            if len(sol)==n:
                res.append(sol[:])
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res