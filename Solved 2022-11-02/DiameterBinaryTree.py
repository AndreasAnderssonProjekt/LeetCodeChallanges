"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any 
two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        
        self.max_path = 0
        
        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)
            self.max_path = max(self.max_path, left + right)
            return 1 + max(left, right)
        
        
        depth(root)
        return self.max_path
