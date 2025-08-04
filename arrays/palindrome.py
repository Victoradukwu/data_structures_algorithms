"""Determine if a linked list s a palindrome"""


from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def is_palindrome1(self, head: Optional[ListNode])-> bool:
        """
        First implementation, using list. This has O(n) for time and space
        because it requires creating of a list of equal length
        """
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
        
        # return all((x[0] == x[1] for x in zip_longest(vals, reversed(vals)))) ## For Python, this line can replace all the lines below, but it is less readable
        left = 0
        right = len(vals) - 1
        
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def is_palindrome2(self, head: ListNode)->bool:
        """This implementation, though more verbose, has better space efficiency and time efficiency
        """
        if not head:  # an empty python list
            return True
        
        fast = head
        slow = head

        #find the middle (slow)
        while fast and fast.next:
            slow = slow.next # pyright: ignore[reportOptionalMemberAccess]
            fast = fast.next.next
        
        #reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
            
        left, right = head, prev
        while right:
            if left.val != right.val:  # pyright: ignore[reportOptionalMemberAccess]
                return False
            left = left.next  # pyright: ignore[reportOptionalMemberAccess]
            right = right.next
        
        return True
    
    
def build_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Example palindrome list: [1, 2, 2, 1]
head = build_linked_list([1, 2, 2, 1])
sol = Solution()
print(sol.is_palindrome2(head))  # Should print True

# Example non-palindrome list: [1, 2, 3]
head2 = build_linked_list([1, 2, 3])
print(sol.is_palindrome2(head2))  # Should print False