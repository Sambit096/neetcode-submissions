class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]

        n=len(nums)
        def backtrack(i):
            if i==n:
                #Snapshot of the solution 
                res.append(sol[:])
                return
            
            #not take
            backtrack(i+1)

            #take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res