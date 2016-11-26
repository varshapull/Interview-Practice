#Check if linkedlist is palindrome

 def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # find mid point
       	dummy = head
        dummy2 = head.next
        while dummy2 and dummy2.next:
            dummy = dummy.next
            dummy2 = dummy2.next.next
        
        # reverse the second half
        cur = dummy.next
        dummy.next = None
        pre = None
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        # compare values from two halves
        tail = pre
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        
        return True