
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
        if not head:
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
    nodes = []
    for lst in lists:
        while lst:
            nodes.append(lst.val)
            lst = lst.next
    nodes.sort()

    res = ListNode(0)
    cur = res
    for node in nodes:
        cur.next = ListNode(node)
        cur = cur.next
    return res.next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """_Neetcode_Easy_

    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
    The new list should be made up of nodes from list1 and list2.

    Itereative approach
    """
    dummy = curr_node = ListNode()  # two references to the same empty list node

    while list1 and list2:  # the heads of list1 and list2 are both non-null
        if list1.val <= list2.val:
            curr_node.next = list1 #The list with the smalles head becomes starts the combined list
            list1 = list1.next # The affected list has its head updated
        else:
            curr_node.next = list2
            list2 = list2.next
        curr_node = curr_node.next  # `dummy` still points to the empty ListNode, but `node` is now a different object
    curr_node.next = (
        list1 or list2
    )  # One of the lists is exhausetd, so, we append the remaining of the other list to the new one we are constructing
    return (
        dummy.next
    )  # dummy still references the empty ListNode, whose `next` is the first ListNode in the concatenated result
