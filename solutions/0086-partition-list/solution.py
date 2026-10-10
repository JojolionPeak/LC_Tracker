# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        big_d, small_d = ListNode(), ListNode()
        b_tail, s_tail, cur = big_d, small_d, head

        while cur:
            if cur.val >= x:
                b_tail.next = cur
                b_tail = b_tail.next
            else:
                s_tail.next = cur
                s_tail = s_tail.next
            cur = cur.next

        s_tail.next, b_tail.next = big_d.next, None
        return small_d.next 
