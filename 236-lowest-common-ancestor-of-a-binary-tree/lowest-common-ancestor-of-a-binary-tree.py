# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root or not p or not q:
        #     return None
        # if (max(p.val, q.val) < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif (min(p.val, q.val) > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root

        # cur = root

        # while cur:
        #     if p.val > cur.val and q.val > cur.val:
        #         cur = cur.right
        #     elif p.val < cur.val and q.val < cur.val:
        #         cur = cur.left
        #     else:
        #         return cur

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

