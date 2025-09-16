from typing import Optional, Self


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next: Optional[Self] = None
        self.prev: Optional[Self] = None


class MyLinkedList:
    """_Leetcode_Medium_

    Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
    A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
    If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

    Implement the MyLinkedList class:
    `MyLinkedList()` Initializes the MyLinkedList object.
    `int get(int index)` Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    `void addAtHead(int val)` Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
    `void addAtTail(int val)` Append a node of value val as the last element of the linked list.
    `void addAtIndex(int index, int val)` Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
    `void deleteAtIndex(int index)` Delete the indexth node in the linked list, if the index is valid.
    """

    def __init__(self):
        """Adds dummy nodes, left and right, to make work easier. All the other real nodes are between the dummy nodes"""
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    # def get(self, index: int) -> int:
    #     curr = self.left.next
    #     while curr and index > 0:
    #         curr = curr.next
    #         index -= 1
    #     if curr and curr != self.right and index == 0:
    #         return curr.val
    #     return -1

    def get(self, index: int) -> int:
        curr = self.left.next
        curr_index = 0
        while curr and curr_index < index:
            curr = curr.next
            curr_index += 1
            if not curr:
                return -1
        if curr and curr != self.right:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        tmp = self.left.next
        new_node.next = self.left.next
        new_node.prev = self.left
        self.left.next = new_node
        tmp.prev = new_node # type: ignore

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        tmp = self.right.prev
        new_node.next = self.right
        new_node.prev = self.right.prev

        self.right.prev = new_node
        if tmp:
            tmp.next = new_node

    # def addAtIndex(self, index: int, val: int) -> None:
    #     new_node = ListNode(val)
    #     curr = self.left.next
    #     while curr and index > 0:
    #         curr = curr.next
    #         index -= 1
    #     if curr and index == 0:
    #         tmp = curr.prev
    #         new_node.next = curr
    #         new_node.prev = curr.prev
    #         curr.prev = new_node
    #         tmp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.left.next
        curr_index = 0
        while curr and curr_index < index:
            curr = curr.next
            curr_index += 1
        if curr:
            tmp = curr.prev
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev = new_node
            if tmp:
                tmp.next = new_node

    # def deleteAtIndex(self, index: int) -> None:
    #     curr = self.left.next
    #     while curr and index > 0:
    #         curr = curr.next
    #         index -= 1
    #     if curr and curr != self.right and index == 0:
    #         curr.prev.next = curr.next
    #         curr.next.prev = curr.prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next

        curr_index = 0
        while curr and curr_index < index:
            curr = curr.next
            curr_index += 1
        if curr and curr != self.right:
            curr.prev.next = curr.next # type: ignore
            curr.next.prev = curr.prev # type: ignore


class BrowserHistory:
    """_Leetcode_medium_
    You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

    Implement the BrowserHistory class:
    `BrowserHistory(string homepage)` Initializes the object with the homepage of the browser.
    `void visit(string url)` Visits url from the current page. It clears up all the forward history.
    `string back(int steps)` Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    `string forward(int steps)` Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

    """
    def __init__(self, homepage: str):
        self.home = ListNode(homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        node = ListNode(url)
        curr = self.curr
        curr.next = node
        node.prev = curr
        self.curr = node

    def back(self, steps: int) -> str:
        ctr = 0
        curr = self.curr
        while curr.prev and ctr < steps:
            curr = curr.prev
            ctr += 1
        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        ctr = 0
        curr = self.curr
        while curr.next and ctr < steps:
            curr = curr.next
            ctr += 1
        self.curr = curr
        return curr.val
