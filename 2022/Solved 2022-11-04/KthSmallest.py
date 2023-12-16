class Solution(object):
    def kthSmallest(self, root, k):
        if not root:
            return

        self.ans = root.val
        self.count = 0
        self.k = k
        self.done = False
        
        def helper(root):
            if self.done:
                return 
            if not root:
                return
            
            # Inorder traversal, stop when reaching node k.
            helper(root.left)
            self.count += 1
            print(self.count, root.val)
            if self.count == self.k:
                self.ans =  root.val
                self.done = True
                return
            helper(root.right)
            
           
        helper(root)    
        return self.ans
