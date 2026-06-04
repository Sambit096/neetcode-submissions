import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for a,b,time in times:
            graph[a].append((b,time))
        min_times={}
        min_heap=[(0,k)]

        while min_heap:
            time_k_to_i,i=heapq.heappop(min_heap)
            if i in min_times:
                continue
            #Assign the min time it takes to get tot i into the hashmap
            min_times[i]=time_k_to_i
            for  nei,nei_time in graph[i]:
                # Check if THe neigh is not in te hashmap
                if nei not in min_times:
                    heapq.heappush(min_heap,(time_k_to_i+nei_time,nei))
        #Meaning we can visit all the nodes/visited al;l nodes
        if len(min_times)==n:
            return max(min_times.values())
        else:
            return -1


