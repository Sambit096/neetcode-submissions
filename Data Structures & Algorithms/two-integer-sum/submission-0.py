class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        start=0
        end=len(indexed_nums)-1
        for i in range(len(indexed_nums)):
            sum_nums=indexed_nums[start][0]+indexed_nums[end][0]
            if target > sum_nums:
                start+=1
            elif target < sum_nums:
                end-=1
            else:
                return sorted([indexed_nums[start][1], indexed_nums[end][1]])
        return []