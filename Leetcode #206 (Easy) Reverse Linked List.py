#Leetcode #206 (Easy) Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        # iterative
        revNode = None
        while head:
            node = ListNode()
            node.val = head.val
            node.next = revNode
            revNode = node
            head = head.next
        return revNode
        '''
        # recursive
        def rev(head, prehead=None):
            if head==None:
                return prehead
            temp = head.next
            head.next = prehead
            return rev(temp, head)
        return rev(head)