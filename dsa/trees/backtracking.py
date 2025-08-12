
from typing import List, Optional

from bst import TreeNode


class Backtracking:
    
    def can_reach_root(self, root: Optional[TreeNode])-> bool:
        """_summary_

        Given a binary tree, determine if a path exists from the root to any leaf node, without crossing a node whose value is zero
        
        Time complexity is O(n), since we will touch every single node
        """
        if not root or root.val == 0:
            return False
        
        if not (root.left or root.right): # Successfully got to leaf node without passing a zero
            return True
        
        if self.can_reach_root(root.left):
            return True
        
        if self.can_reach_root(root.right):
            return True
        return False
    
    def leafPath(self, root, path):
        """_summary_

        Check if a path exists from the root node to a leaf node, without a zero. Determine such a path
        """
        if not root or root.val == 0:
            return False
        path.append(root.val)

        if not root.left and not root.right:
            return True
        if self.leafPath(root.left, path):
            return True
        if self.leafPath(root.right, path):
            return True
        path.pop()
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """_Leetcode_Easy_

        Given the root of a binary tree and an integer `targetSum`, return `True` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`.
        """
        def dfs(node, curr_sum):
            if not node:
                return False

            curr_sum += node.val
            if not (node.left or node.right):  # We're now at a leaf node
                return curr_sum == targetSum

            return dfs(node.left, curr_sum) or dfs(
                node.right, curr_sum
            )  # Return true if calling dfs on either left or right returns True

        return dfs(root, 0)
    
    def subsets(self, nums: List[int])->List[List[int]]:
        """_Neetcode_Medium_

        Given an array nums of unique integers, return all possible subsets of nums.
        The solution set must not contain duplicate subsets. You may return the solution in any order.
        """
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res