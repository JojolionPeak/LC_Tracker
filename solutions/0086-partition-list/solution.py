# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        big_list, out = ListNode(), ListNode()
        big_tail, prev = big_list, out

        while head:
            if head.val >= x:
                big_tail.next = head
                big_tail , head = big_tail.next, head.next
                big_tail.next = None
            else:
                prev.next = head
                prev, head = prev.next, head.next
        prev.next = big_list.next
        return out.next
