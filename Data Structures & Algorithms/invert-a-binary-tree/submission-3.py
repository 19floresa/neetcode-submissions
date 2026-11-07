# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = [ (root, root.left, root.right) ]
        while q:
            for _ in range(len(q)):
                p, l, r = q.pop(0)
                p.left = r
                p.right = l
                if l:
                    q.append((l, l.left, l.right))
                if r:
                    q.append((r, r.left, r.right))
        return root

        