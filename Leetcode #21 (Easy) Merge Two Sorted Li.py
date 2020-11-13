#Leetcode #21 (Easy) Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = newlist = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                newlist.next = l1
                l1 = l1.next
            else:
                newlist.next = l2
                l2 = l2.next
            newlist = newlist.next
        newlist.next = l1 or l2
        return ans.next
                