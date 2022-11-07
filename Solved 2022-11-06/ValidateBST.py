def isValidBST(self, root, floor=-float('inf'), ceiling = float('inf')):
        if not root:
            return True
 
        if root.val <= floor or root.val >= ceiling:
            return False
        
        return isValidBST(root.left, floor, root.val) and isValidBST(root.right, root.val, ceiling)
