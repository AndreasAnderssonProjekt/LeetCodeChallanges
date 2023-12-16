def isSymmetric(root):
    if not root:
        return True

    return isMirror(root.left, root.right)

def isMirror(root1, root2):
    if root1 and root2:
        return root1.val == root2.val and isMirror(root1.left, root2.left) and isMirror(root1.right, root2.right)

    return not root1 and not root2
