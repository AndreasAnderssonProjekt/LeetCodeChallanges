def reverseList(head):
    rev = None
    while head:
        curr = head
        head = head.next
        curr.next = rev
        rev = curr
    return rev
