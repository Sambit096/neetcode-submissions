class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        courses=prerequisites
        for a,b in courses:
            g[a].append(b)
        #Set three states
        UNVISITED=0
        VISITING=1
        VISITED=2
        states=[UNVISITED] * numCourses
        #we declare a dfs(node) to check if theres a cycle and retrun False or tru
        def dfs(node):
            #get the current state were in
            state=states[node]
            if state==VISITED: return True
            #Here we find a cycle since we should have already in a visiting node
            elif state==VISITING: return False
            states[node]=VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False
            #We finished cisiting the state and mark as such
            states[node]=VISITED
            return True
            
        # run a loop for the number of courses wwe have and check if dfs returned True or false and return 

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

