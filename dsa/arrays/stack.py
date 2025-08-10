from typing import Self


def isValid(self, s: str) -> bool:
    """_Netcode_Easy_

    You are given a string `s` consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
    The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    Return true if s is a valid string, and false otherwise.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = []
    close_open_mapping = {')':'(', '}':'{', ']':'['}
    
    for c in s:
        if c in close_open_mapping:
            if stack and stack[-1] == close_open_mapping[c]:
                stack.pop()
            else: 
                return False
        else:
            stack.append(c)
    return True if not stack else False




class MinStack:
    """_Neatcode_Medium_
    Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    Each function should run in  O(1) time.
    """
    def __init__(self)->None:
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[- 1]

    def getMin(self) -> int:
        return min(self.stack)
