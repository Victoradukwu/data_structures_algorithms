
from collections import deque
from typing import Any, List, Optional, Self


class TreeNode:
    def __init__(self, val, left: Optional[Self] = None, right: Optional[Self] = None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    
    def bst_search(self, root: Optional[TreeNode], target: Any)-> Optional[TreeNode]:
        """_Leetcode_Easy_

        You are given the root of a binary search tree (BST) and an integer val.
        Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
        
        Note: Like search on sorted array, the time time complexity is O(logn)--for a BALANCED bst. However, delete and insert for BST can also be O(logn), unlike in array where it is O(n)
        """
        if not root:
            return None
        
        if target > root.val:
            return self. bst_search(root.right, target)
        elif target < root.val:
            return self.bst_search(root.left, target)
        else:
            return root
        
    def bst_insert(self, root: Optional[TreeNode], val:int)->Optional[TreeNode]:
        """_Leetcode_Easy_

        You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
        """
        if not root:
            return TreeNode(val=val)

        if val > root.val:
            root.right = self.bst_insert(root.right, val)
        elif val < root.val:
            root.left = self.bst_insert(root.left, val)
        return root
    
    def min_value_node(self, root: Optional[TreeNode])-> Optional[TreeNode]:
        if not root:
            return None

        curr = root
        while root and root.left:
            curr = root.left
        return curr
    
    def delete_node(self, root: Optional[TreeNode], val)->Optional[TreeNode]:
        if not root:
            return root
        
        if val > root.val:
            root.right = self.delete_node(root.right, val)
        elif val < root.val:
            root.left = self.delete_node(root.left, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.min_value_node(root.right)
                root.val = min_node.val  # type: ignore
                root.right = self.delete_node(root.right, min_node.val) # type: ignore
        return root
    
    def inorder_traversal(self, root: Optional[TreeNode])->List[int]:
        """_Neetcode_Easy_

        Before picking a node, we traverse its left subtree first. Then we pick the node and then traverse the right subtree. This is done recursivey and a a time complexity of O(n).
        If we have an unsorted array, we will have to construct a valid BST before traversing. This will lead to a combined O(nlogn)
        """
        res = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res

    def preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        We print a node, traverse the left subtree, then traverse the right subtree. This is called
        PREORDER traversal
        """
        res = []

        def preorder(node):
            if not node:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res
    
    def postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        We traverse the left subtree, then traverse the right subtree, then print the root. This is called
        POSTORDER traversal
        """
        res = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res
    
    def reverseorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        We want to return the list in REVERSE ORDER ie last-to-first. This will be similar to the INORDER
        implementation. The only difference is that we run the run the right subtree before the left subtree
        
        NOTE: INORDER, PREORDER, POSTORDER, REVERSEORDER are all DFS implementations
        """
        res = []

        def reverseorder(node):
            if not node:
                return

            reverseorder(node.right)
            res.append(node.val)
            reverseorder(node.left)

        reverseorder(root)
        return res
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """_Neetcode_Medium_

        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
        Optimal solution: Recursively, we call dfs on the left, increment the value of k by 1. If the new value equals k, we return the value of the node just added; otherwise we run dfs on the right and repeat the process
        """
        cnt = 0
        res = root.val # type: ignore

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return

            dfs(node.left)
            cnt += 1
            if cnt == k:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res
    
    def bfs(self, root: Optional[TreeNode])->List[int]:
        """
        _Neetcode_Medium_
        Also called LEVEL ORDER TRAVERSAL; Better implement with a QUEUE data structure

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