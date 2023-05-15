# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(head: ListNode, k):
    current = head
    for i in range(k - 1):
        current = current.next

    left = current
    right = head

    while current.next:
        current = current.next
        right = right.next

    left.val, right.val = right.val, left.val
    return head

head = [1, 2, 3, 4, 5]
k = 2
print(swapNodes(head, k))
