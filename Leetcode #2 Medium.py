#Leetcode #2 Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sumNode = ListNode()
        head = sumNode
        c = 0
        while l1 or l2 or c:
            temp = num1 = num2 = 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            temp = num1+num2+c
            if temp>9:
                c = 1
            else:
                c = 0
            sumNode.next = ListNode(temp%10)
            sumNode = sumNode.next
            
        return head.next