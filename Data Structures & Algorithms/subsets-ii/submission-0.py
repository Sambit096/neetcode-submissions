class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sol=[],[]
        n=len(nums)
        def backtrack(i):
            if i==n:
                res.append(sol[:])
                return
            
            #nottake
            j=i #pointer to go through and skipp all same elements
            while j<n and nums[j]==nums[i]:
                j+=1
            backtrack(j)

            #take
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res