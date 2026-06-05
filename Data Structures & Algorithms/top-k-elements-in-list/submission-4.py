from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First get a count all the elements in the heap into a dictionary
        counter=Counter(nums)
         
        #Initialize a heap
        heap=[]
        #we now have a dictionary with {Num:Frequency} run through int
        for val,count in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(count,val))
            else:
                heapq.heappushpop(heap,(count,val))
        
        return [h[1] for h in heap]
        
        


