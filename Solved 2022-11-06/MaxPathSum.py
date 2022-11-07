import math
class Solution(object):
    def maxPathSum(self, root):
        self.max_path = -math.inf

        def maxPath(self, root):
            if not root:
                return 0

            left_path = max(maxPath(root.left), 0)
            right_path = max(maxPath(root.right), 0)
            path = left_path + right_path + root.val
            self.max_path = max(path, self.max_path)
            return root.val + max(left_path, right_path)

        maxPath(root)
        return self.max_path
