class Fibonacci:
    def fibonacci_vanilla(self, n:int)->int:
        """Using vanilla recursion. Highly inefficient"""
        if n <= 1:
            return n
        return self.fibonacci_vanilla(n - 1) + self.fibonacci_vanilla(n - 2)


    def fibonacci_memoized(self, n:int)->int:
        """Still recursion but uses memoization to speed up the process. Also called Top-down dynamic programming"""
        if n <= 1:
            return n
        cache = {}
        if n in cache:
            return cache[n]
        cache[n] = self.fibonacci_memoized(n - 1) + self.fibonacci_memoized(n - 2)
        return cache[n]


    def fibonacci_dp(self, n:int)->int:
        """Uses bottom-up dynamic programming. Most efficient solution
        Space Complexity: O(1)
        Time complexity: O(n)
        """
        if n <= 1:
            return n

        dp = [0,1]
        for _ in range(1,n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]

        return dp[1]

class UniquePaths:
    """Finding the number of unique paths from top left to bottom right
    We can only move to the right and downwards in the grid. We cannot move left or upwards
    """
    def paths_brute(self, rows, cols, r=0, c=0):
        """Using Brute force

        Time Complexity: O(2**(m+n))
        Space Complexity: O(2**(m+n))
        """
        if r == rows or c == cols:
            return 0
        if r == rows -1 and c == cols - 1:
            return 1
        
        return self.paths_brute(rows, cols, r + 1, c) + self.paths_brute(rows, cols, r, c + 1)
    
    def paths_memoized_brute(self, rows, cols, r=0, c=0):
        """Using Memoized Brute force; aka Top-down dynamic programming

        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        if r == rows or c == cols:
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1
        
        cache = [[0]*cols for row in range(rows)]
        if cache[r][c] > 0:
            return cache[r][c]
        
        cache[r][c] = self.paths_memoized_brute(rows, cols, r + 1, c) + self.paths_memoized_brute(
            rows,
            cols,
            r,
            c + 1,
        )
        return cache[r][c]
    
    def paths_dp(self, rows, cols):
        """Implemented with Dynamic Programming; aka Bottom-up dynamic programming; the true DP approach

        Time Complexity: O(m*n)
        Space Complexity: O(m)
        """
        
        prev_row = [0] * cols # Implicitly creating a row of all 0's after the matrix last row

        for _ in range(rows-1, -1, -1): # Technically equivalent to range(rows), but written tghis way to reflect the fact that we strat from last row to the first row
            cur_row = [0] * cols # a single row of zeros
            cur_row[cols - 1] = 1 # Set the bottom-right to 1
            for c in range(cols - 2, -1, -1):
                cur_row[c] = cur_row[c + 1] + prev_row[c]
            prev_row = cur_row
        return prev_row[0]


n = 10
fb = Fibonacci()
print(fb.fibonacci_memoized(n))
print(fb.fibonacci_dp(n))

unq = UniquePaths()
print("^^^^^^^", unq.paths_brute(4, 4))
print("^^^^^^^", unq.paths_memoized_brute(4, 4))
print("^^^^^^^", unq.paths_dp(4, 4))