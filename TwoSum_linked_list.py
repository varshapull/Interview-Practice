#https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        p = l1
        q = l2
        carry = 0 
        
        while p != None or q!= None:
            if p != None:
                x = p.val
            else:
                x = 0
            if q!= None :
                y = q.val
            else:
                y = 0
            sum = x+y+carry
            carry = sum/10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            
            if p != None:
                p = p.next
            if q!= None:
                q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next
            