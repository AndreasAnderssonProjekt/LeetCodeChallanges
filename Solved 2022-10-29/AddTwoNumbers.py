def addTwoNumbers(self, l1, l2):
        n, r = addNodes(l1, l2, 0)
        l3 = ListNode(n)
        curr = l3
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

        while l1 or l2:
            n, r = addNodes(l1, l2, r)
            curr.next = ListNode(n)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if r != 0:
            curr.next = ListNode(r)
            

        if r != 0:
            curr.next = ListNode(r)
        return l3
    
def addNodes(l1, l2, r):
    n = 0
    if l1:
        n += l1.val

    if l2:
        n += l2.val

    if n + r < 10:
        return n + r, 0
    else:
        return n + r - 10, 1
