class Solution:
    def jump(self, nums: List[int]) -> int:
        far=0
        end=0
        start=0
        n=len(nums)
        smallest_jumps=0
        for i in range(n-1):
            far=max(far, i+nums[i])
            if i==end:
                #max jumps by 1
                smallest_jumps+=1
                end=far
            
        return smallest_jumps


