# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pprint import pprint

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' 
        make a dummy node to point to the last node, dummy node to be tail
        if the current head is None or cur.next is None, return current node
        Take previous returned node and set it's pointer to the current node
        Make the current node point to None
        return current node
        return the last node
        '''

        if head is None or head.next is None: return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
