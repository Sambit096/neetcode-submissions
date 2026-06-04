"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        start=node
        #create a hashmap to keep a reference to the old nodes neighbours so we can use them in the new nodes neighbours
        o_to_n={}
        #create and push the rootnode into stack
        q=deque()
        q.append(start)
        #keep a list of nodes already visited
        visited=set()

        while q:
            node=q.popleft()
            o_to_n[node]=Node(val=node.val)
            
            for nei in node.neighbors:
                if nei not in visited:
                    #add the neighbour node to the  visited set
                    visited.add(nei)
                    #add the neighbour to the stack telling we plan to visit it
                    q.append(nei)
            
        
        for old_node,new_node in o_to_n.items():
            for nei in old_node.neighbors:
                new_nei=o_to_n[nei]
                new_node.neighbors.append(new_nei)
        
        return o_to_n[start]