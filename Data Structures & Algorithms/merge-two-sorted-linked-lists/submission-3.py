# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        cur = dummy_node
        while list1 or list2:
            if not list1:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
            elif not list2:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            elif list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        return dummy_node.next
        