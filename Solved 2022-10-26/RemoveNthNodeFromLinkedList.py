def removeNthFromEnd(head,n):
    slow = head
    fast = head

    for i in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head
