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
