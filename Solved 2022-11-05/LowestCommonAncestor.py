
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
            while root:
                if root.val >= min(p.val, q.val) and root.val <= max(p.val, q.val):
                    return root

                if root.val < min(p.val, q.val):
                    root = root.right

                elif root.val > max(p.val, q.val):
                    root = root.left
