# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes=0
        q=deque()
        #Put the initial roit and largest
        q.append((root,-float('inf')))
        while q:
            node,largest=q.popleft()
            if largest<=node.val:
                good_nodes+=1
            
            largest=max(largest,node.val)

            if node.left:q.append((node.left,largest))
            if node.right:q.append((node.right,largest))

        return good_nodes
