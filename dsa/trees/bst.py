
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
        """_summary_
        Find the node is O(logn) and removing it is log(n) ie 2log(n). But 2 is a constant
        Therefore thr time complexity is O(logn)

        """
        if not root:
            return root

        if val > root.val:  # We have not found it yet
            root.right = self.delete_node(root.right, val)
        elif val < root.val:  # We have not found it yet
            root.left = self.delete_node(root.left, val)
        else:  # We have found it
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.min_value_node(root.right)
                root.val = min_node.val  # type: ignore
                root.right = self.delete_node(root.right, min_node.val)  # type: ignore
        return root

    def dfs_inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Neetcode_Easy_

        DFS: Before picking a node, we traverse its left subtree first. Then we pick the node and then traverse the right subtree. This is done recursivey and a a time complexity of O(n).
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

    def dfs_preorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        DFS: We print a node, traverse the left subtree, then traverse the right subtree. This is called
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

    def dfs_postorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        DFS: We traverse the left subtree, then traverse the right subtree, then print the root. This is called
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

    def dfs_reverseorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """_Bonus_

        DFS: We want to return the list in REVERSE ORDER ie last-to-first. This will be similar to the INORDER
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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> Optional[int]:
        """_Neetcode_Medium_

        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.
        Optimal solution: Recursively, we call dfs on the left, increment the value of k by 1. If the new value equals k, we return the value of the node just added; otherwise we run dfs on the right and repeat the process
        """

        if not root:
            return
        cnt = 0
        res = root.val

        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            # Inorder DFS. Note that after calling dfs on the left, the node is ''accessed before calling it on the right subtree
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

        Given a binary tree root, return the level order (bfs) traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.
        """
        res = []

        queue = deque()
        queue.append(root)

        while queue:
            q_length = len(queue)
            level = []
            for i in range(q_length):
                node = queue.popleft()
                if node:  # This check is necessary because a a null node (leaf node) might have been added to the queue earlier
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)

        return res


class ConstructBinaryTree:
    """_Neetcode_Medium_

    You are given two integer arrays preorder and inorder.

    preorder is the preorder traversal of a binary tree
    inorder is the inorder traversal of the same tree
    Both arrays are of the same size and consist of unique values.
    Rebuild the binary tree from the preorder and inorder traversals and return its root.
    """

    def depth_first_search(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Uses dfs

        Time Complexity: O(n**2)
        Space Complexity: O(n)
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # preorder[0] is the root, preorder[1:mid+1] used for the left subtree and preorder[mid+1:] used for the right subtree
        root.left = self.depth_first_search(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.depth_first_search(preorder[mid + 1 :], inorder[mid + 1 :])
        # Note inorder[mid] has been used for the root; same for preorder[0]
        return root

    def dfs_with_hashmap(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(inorder) - 1)

    def dfs_optimized(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """_summary_

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        preIdx = inIdx = 0

        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root

        return dfs(float("inf"))


class ConstructBinaryTree2:
    """_Neetcode_Medium_

    You are given two integer arrays postorder and inorder.

    postorder is the postorder traversal of a binary tree
    inorder is the inorder traversal of the same tree
    Both arrays are of the same size and consist of unique values.
    Rebuild the binary tree from the postorder and inorder traversals and return its root.
    """

    def depth_first_search(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v: i for i, v in enumerate(inorder)}
        """Uses dfs

        Time Complexity: O(n**2)
        Space Complexity: O(n)
        """
        if not inorder:
            return

        root_val = postorder.pop()
        root = TreeNode(val=root_val)
        idx = inorderIdx[root_val]
        root.right = self.depth_first_search(inorder[idx + 1 :], postorder)
        root.left = self.depth_first_search(inorder[:idx], postorder)
        return root