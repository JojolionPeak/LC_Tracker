# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                tail, list1 = tail.next, list1.next

            else:
                tail.next = list2
                tail, list2 = tail.next, list2.next

        tail.next = list1 or list2
        merged = dummy.next
        return merged
