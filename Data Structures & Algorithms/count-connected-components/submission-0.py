class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank=[0]*n
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])  
            return parent[u]
        def union(u,v):
            ult_u=find(u)
            ult_v=find(v)
            if ult_u == ult_v:
                return 0
            if rank[ult_u]<rank[ult_v]:
                parent[ult_u]=ult_v
            elif rank[ult_v]>rank[ult_u]:
                parent[ult_v]=ult_u
            else:
                parent[ult_v]=ult_u
                rank[ult_v]+=1
            return 1
        
        
        res=n
        for a,b in edges:
            res-=union(a,b)
        return res