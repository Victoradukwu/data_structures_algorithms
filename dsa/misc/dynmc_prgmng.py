from typing import List


class Fibonacci:
    def recursion_vanilla(self, n: int) -> int:
        """Using vanilla recursion. Highly inefficient"""
        if n <= 1:
            return n
        return self.recursion_vanilla(n - 1) + self.recursion_vanilla(n - 2)

    def recursion_memoized(self, n: int) -> int:
        """Still recursion but uses memoization to speed up the process. Also called Top-down dynamic programming"""
        cache = {}

        # Defining a helper function enables us keep the cache outside the recursive function, ensuring that the cache
        # is not reinitialized on each recursive call
        def helper(i):
            if i <= 1:
                return i
            if i not in cache:
                print(f"No hit for {i}")  # Check that memoization actually works
                cache[i] = helper(i - 1) + helper(i - 2)
            return cache[i]

        return helper(n)

    def fibonacci_dp(self, n: int) -> int:
        """Uses bottom-up dynamic programming. Most efficient solution

        Space Complexity: O(1)
        Time complexity: O(n)
        """
        if n <= 1:
            return n

        dp = [0, 1]
        for _ in range(n - 1):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        return dp[1]


class UniquePaths:
    """Finding the number of unique paths from top left to bottom right
    We can only move to the right and downwards in the grid. We cannot move left or upwards
    """

    def recursive_brute(self, rows, cols):
        """Using Brute force

        Time Complexity: O(2**(m+n))
        Space Complexity: O(2**(m+n))
        """

        def dfs(r, c):
            """The number of ways of getting to cell (r,c)"""
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            return dfs(r, c - 1) + dfs(r - 1, c)

        return dfs(rows - 1, cols - 1)

    def recursive_memoized(self, rows, cols, r=0, c=0):
        """Using Memoized Brute force; aka Top-down dynamic programming

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """

        cache = {(0, 0): 1}

        def dfs(r, c):
            """The number of ways of getting to cell (r,c)"""
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if (r, c) not in cache:
                cache[(r, c)] = dfs(r, c - 1) + dfs(r - 1, c)
            return cache[(r, c)]

        return dfs(rows - 1, cols - 1)

    def paths_dp(self, rows, cols):
        """Implemented with Dynamic Programming; aka Bottom-up dynamic programming; the true DP approach

        Time Complexity: O(m*n)
        Space Complexity: O(m)
        """

        prev_row = [0] * cols  # Implicitly creating a row of all 0's after the matrix last row

        # Technically equivalent to range(rows), but written this way to reflect the fact that we start from last row to the first row
        for _ in range(rows):
            cur_row = [0] * cols  # a single row of zeros
            cur_row[cols - 1] = 1  # Set the bottom-right to 1
            for c in range(cols - 2, -1, -1):
                cur_row[c] = cur_row[c + 1] + prev_row[c]
            prev_row = cur_row
        return prev_row[0]

class ClimbingStairs:
    """_Neetcode_Easy_

    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    The simple solution here is that this is actually a FIBONACCI sequence, a la Greg Hogg, with f(n) = n if n < 3
    The number of ways of getting to the 10th stair equals the number of ways of getting to the 9th
    plus number of ways of getting to 8th
    """

    def vanillaRecursion(self, n: int) -> int:
        """
        This approach uses the vanilla recursion method. It is highly inefficient

        Time complexit: O(2^n)
        Space complexity: O(n)
        """

        if n < 3:
            return n
        return self.vanillaRecursion(n - 1) + self.vanillaRecursion(n - 2)

    def memoizedRecursion(self, n: int, cache={}) -> int:
        """Uses recursion with memoization, aka top-down dynamic programming. An improvement over the vanilla recursion

        Time complexit: O(n)
        Space complexity: O(n)
        """

        if n < 3:
            return n

        if n not in cache:
            cache[n] = self.memoizedRecursion(n - 1) + self.memoizedRecursion(n - 2)

        return cache[n]

    def dynamic_programming(self, n: int) -> int:
        """Use Bottom-up dynamic programming, aka True DP.

        Time complexit: O(n)
        Space complexity: O(n)
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def dp_space_optimized(self, n: int) -> int:
        """Uses Bottom-up DP with space optimization

        Time complexit: O(n)
        Space complexity: O(1)
        """
        second_last, last = 1, 2

        for _ in range(3, n + 1):
            second_last, last = last, second_last + last
        return last


class HouseRobber:
    """You are given an integer array `nums` where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

    You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
    Return the maximum amount of money you can rob without alerting the police.

    The guide here is that, at any given point, you have to pick the max of two options:
    1. rob the current house and add it to the max obtainable in two houses back
    2. skip robbing current house and take the max obtainable in the last house
    """

    def vanilla_recursion(self, nums: List[int]) -> int:
        """
        Time Complexity: O(2**n); Not efficient
        Space Complexity: O(n)
        """

        n = len(nums)
        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(dfs(i - 1), nums[i] + dfs(i - 2))

        return dfs(n - 1)

    def memoized_recursion(self, nums: List[int]) -> int:
        """
        Top-down dp
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        cache = {0: nums[0], 1: max(nums[0], nums[1])}

        def dfs(i):
            if i not in cache:
                cache[i] = max(dfs(i - 1), nums[i] + dfs(i - 2))
            return cache[i]

        return dfs(n - 1)

    def dp_regular(self, nums: List[int]) -> int:
        """
        Bottom-up dp
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]

    def dp_space_optimized(self, nums: List[int]) -> int:
        """_The Optimum_

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        nums_length = len(nums)

        if nums_length == 0:
            return 0
        if nums_length == 1:
            return nums[0]
        if nums_length == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, nums_length):
            curr, prev = max(nums[i] + prev, curr), curr

        return curr


class UniquePaths2:
    """
    You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

    An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

    Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The testcases are generated so that the answer will be less than or equal to 2 * (10^9).
    """

    def top_down_dp(self, grid: List[List[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])

        # The cache is a hash map in which the keys are tuples of (row, column)
        cache = {(row_length - 1, col_length - 1): 1}

        def dfs(r, c):
            if r == row_length or c == col_length or grid[r][c]:
                return 0
            if (r, c) not in cache:
                cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)

    def bottom_up_dp(self, grid: List[List[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[row_length - 1][col_length - 1] == 1:
            return 0
        cache = [[0] * (col_length + 1) for _ in range(row_length + 1)]

        cache[row_length - 1][col_length - 1] = 1

        for r in range(row_length - 1, -1, -1):
            for c in range(col_length - 1, -1, -1):
                if grid[r][c] == 1:
                    cache[r][c] = 0
                else:
                    cache[r][c] += cache[r + 1][c]
                    cache[r][c] += cache[r][c + 1]

        return cache[0][0]

    def dp_space_optimized(self, grid: List[List[int]]) -> int:
        row_length, col_length = len(grid), len(grid[0])
        dp = [0] * (col_length + 1)
        dp[col_length - 1] = 1

        for r in range(row_length - 1, -1, -1):
            for c in range(col_length - 1, -1, -1):
                if grid[r][c]:
                    dp[c] = 0
                else:
                    dp[c] += dp[c + 1]

        return dp[0]


n = 10
# fb = Fibonacci()
# print("fib_memoized:", fb.recursion_memoized(n))
# print("fib_dp:", fb.fibonacci_dp(n))

unq = UniquePaths()
print("^^^^^^^", unq.recursive_brute(4, 4))
print("^^^^^^^", unq.recursive_memoized(4, 4))
print("^^^^^^^", unq.paths_dp(4, 4))