from collections import deque
from typing import Optional, Self


class TreeNode:
    def __init__(self, val, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    """_Neetcode_Medium_

    Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
    """

    res = []

    queue = deque()
    queue.append(root)

    while queue:
        q_length = len(queue)
        level = []
        for i in range(q_length):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level:
            res.append(level)

    return res

def rightSideView(root: Optional[TreeNode]) -> list[int]:
    from collections import deque

    res = []

    queue = deque()
    if root:
        queue.append(root)

    while queue:
        q_length = len(queue)
        for i in range(q_length):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if i == q_length - 1:
                res.append(node.val)
    return res