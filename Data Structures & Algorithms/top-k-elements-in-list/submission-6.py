from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[]
        for val,count in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(count,val))
            else:
                heapq.heappushpop(heap,(count,val))
        
        return [val for count,val in heap]
