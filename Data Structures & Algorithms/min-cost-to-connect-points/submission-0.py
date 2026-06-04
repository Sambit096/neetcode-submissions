class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Prims algorithm

        n=len(points)
        seen=set()
        min_heap=[(0,0)]
        total_cost=0
        #Run a loop whil the seen value <n(meaning all points not seen/covered)
        while len(seen)<n:
            dist,i=heapq.heappop(min_heap)
            #Chack if i in seen
            if i in seen:
                continue
            seen.add(i)
            #Increment the totalcost
            total_cost+=dist
            #Get its neighbours
            xi,yi=points[i]

            #run a loop for its neighbours:
            for j in range(n):
                if j not in seen:
                    #get the neighbours of j
                    xj,yj=points[j]
                    #Get the Manhattan distance
                    nei_dist=abs(xi-xj) +abs(yi-yj)
                    #Put the value into the heap
                    heapq.heappush(min_heap,(nei_dist,j))
        return total_cost
            
