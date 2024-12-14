# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(N+M)
    # Space O(1)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ptr = res # ptr and res refer to the same object in memory

        while list1 and list2:
            if list1.val < list2.val:
                res.next = ListNode(list1.val)
                list1 = list1.next
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next
            res = res.next
        
        while list1:
            res.next = ListNode(list1.val)
            list1 = list1.next
            res = res.next

        while list2:
            res.next = ListNode(list2.val)
            list2 = list2.next
            res = res.next
        
        return ptr.next
