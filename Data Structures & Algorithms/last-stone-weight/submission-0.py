class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Max heap it

        for i in range(len(stones)):
            stones[i]=-stones[i]
        
        #Heapify

        heapq.heapify(stones)

        #As long as the array has mor than least 1 element

        while len(stones)>1:
            #pop the largest
            largest=heapq.heappop(stones)
            #pop the second largest
            second_largest=heapq.heappop(stones)

            #If the stones are equal in weight it would be destroyed

            #If they are not equal we subtract them and push the subtracted value into the heap
            if largest!=second_largest:
                heapq.heappush(stones,largest-second_largest)
            
        
        #if 1 is still in the heap
        if len(stones)==1:
            return -heapq.heappop(stones)
        else:
            return 0