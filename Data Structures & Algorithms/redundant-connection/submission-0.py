class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent=list(range(n+1))
        rank=[1]*(n+1)

        def find(u):
            if parent[u]!=u:
                parent[u]=find(parent[u])
            
            return parent[u]

        
        def union(u,v):
            ult_u=find(u)
            ult_v=find(v)

            if ult_u==ult_v:
                return False
            
            if parent[ult_u]<parent[ult_v]:
                parent[ult_u]=ult_v
            
            elif parent[ult_v]<parent[ult_u]:
                parent[ult_v]=ult_u
            else:
                parent[ult_v]=ult_u

                rank[ult_v]+=1
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]

        
                
                