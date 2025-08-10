from collections import deque
from typing import List


class CountStudent:
    """_Leetcode_Easy_
    
    The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

    If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    Otherwise, they will leave it and go to the queue's end.
    This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

    You are given two integer arrays `students` and `sandwiches` where sandwiches[i] is the type of the `ith` sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the `jth` student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
    """
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_student_count = len([st for st in students if st == 0])
        square_student_count = len([st for st in students if st == 1])

        for sandwich in sandwiches:
            if sandwich == 0: # Circular sandwitch
                if circle_student_count == 0: # No more circular-loving student
                    return square_student_count
                else:
                    circle_student_count -= 1

            if sandwich == 1:
                if square_student_count == 0:
                    return circle_student_count
                else:
                    square_student_count -= 1

        return 0


class MyStack:
    """_Neetcode_Easy_

    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

    Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.
    Notes:

    You must use only standard operations of a queue, which means that only `push` to `back`, `peek/pop` from `front`, `size` and `is empty` operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

    """
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
