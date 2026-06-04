class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #define distance function

        def dist(x,y):
            return x**2 +y**2
        
        #initialize hea
        heap=[]
        for x,y in points:
            d=dist(x,y)

            if len(heap)<k:
                #push stuff cuz we needd it to at least contain k elements
                #Since we are using a max heap store the -dist
                heapq.heappush(heap,(-d,x,y))

            else:
            #else we push and pop from the heap so we ultimately have th ecorrect number of k elements
                heapq.heappushpop(heap,(-d,x,y))
        
        #return x and y from the heap
        return [(x,y) for dist,x,y in heap]