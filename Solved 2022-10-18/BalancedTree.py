#Data Structure for Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isBalanced(root):
    if not root:
        return True
    left_height, right_height = height(root.left), height(root.right)
    return abs(left_height - right_height) <= 1 and isBalanced(root.left) and isBalanced(root.right)
    
#Helper
def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height + 1, right_height + 1)
