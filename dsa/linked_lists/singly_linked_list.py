
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedList:
    """_Neetcode_Easy_

    Given the head of a singly linked list, reverse the list, and return the new beginning of the list.
    """
    def reverse_list_iteration(self, head: ListNode) -> Optional[ListNode]:
        """_IterativeMethod_
        
        Time complexity: O(n)
        Space complexity: O(1)
        """
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    def reverse_list_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """_RecursiveMethod_

        Time complexity: O(n)
        Space complexity: O(n)
        """
        if not head:  # Base case
            return None

        new_head = head
        if head.next:
            new_head = self.reverse_list_recursion(head.next)
            head.next.next = head
        head.next = None

        return new_head

    
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """_Neetcode_hard_

    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    """
    node_values = []
    for lst in lists:
        while lst:
            node_values.append(lst.val)
            lst = lst.next
    node_values.sort()

    res = ListNode(0)
    cur = res
    for node_value in node_values:
        node = ListNode(node_value)
        cur.next = node
        cur = node
    return res.next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """_Neetcode_Easy_

    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
    The new list should be made up of nodes from list1 and list2.

    Itereative approach
    """
    nd = ListNode()
    dummy = nd
    curr_node = nd
    while list1 and list2:
        if list1.val <= list2.val:
            curr_node.next = list1
            list1 = list1.next
            curr_node = curr_node.next
        else:
            curr_node.next = list2
            list2 = list2.next
            curr_node = curr_node.next
    curr_node.next = list1 or list2
    return dummy.next
