# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca=[root]
        def search(root):
            #No tree
            if not root:
                return
            #Tree exists take the lca as thte root node
            lca[0]=root
            #If we found the common ancestor return it. If we found one of the things we cant really go any lower so return it
            if root is p or root is q:
                return

            #If we didnt
            elif root.val<p.val and root.val<q.val:
                search(root.right)
            
            elif root.val>p.val and root.val>q.val:
                search(root.left)
            #Else return we finished the search
            else:
                return
        
        search(root)
        return lca[0]