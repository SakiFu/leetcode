"""
Given a singly linked list, determine if it is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, head):
        if not head:
            return True
        first_half = []
        slow = head
        fast = head
        while fast and fast.next:
            first_half.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if first_half.pop() != slow.val:
                return False
            slow = slow.next
        return True