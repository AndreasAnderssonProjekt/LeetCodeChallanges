def reverseList(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = rev
        prev = curr
    return prev
