# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        f, s, s_count, f_count = head, head, 1, 1
        if not head: return None
        while f.next and f.next.next:
            s, f = s.next, f.next.next
        if f.next: s = s.next
        return s
