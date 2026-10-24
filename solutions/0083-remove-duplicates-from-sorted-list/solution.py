# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail, tail.val = dummy, None
        if not head: return
        while head:
            if head.val == tail.val: 
                head = head.next
                continue
            tail.next = head
            tail, head = tail.next, head.next
        tail.next = None
        return dummy.next
