from typing import Any

array = [2, 3, 5, 7, 9]
array2 = [-1, 0, 3, 5, 9, 12]


def linear_search(arr: list[Any], search_term:Any)->int:
    """Time complexity of O(n)"""
    for i in range(len(arr)):
        if arr[i] == search_term:
            return i
    return -1


def binary_search(arr: list[Any], search_term: Any)->int:
    """
    Time complexity of O(logn) but requires that the the array is already sorted
    So the effective time complexity is the that of the sorting algorithm
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if search_term == arr[mid]:
            return mid
        elif search_term < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(f'Linear search for 3 in {array}: {linear_search(array, 3)}')
print(f'Linear search for 4 in {array}: {linear_search(array, 4)}')
print(f'Linear search for 9 in {array}: {linear_search(array, 9)}')

print(f"Binary search for 3 in {array}: {binary_search(array, 3)}")
print(f"Binary search for 4 in {array}: {binary_search(array, 4)}")
print(f"Binary search for 9 in {array}: {binary_search(array, 9)}")


def guess_number(n: int) -> int:
    """__Neetcode simple practice__
    We are playing the Guess Game. The game is as follows:
    I pick a number from 1 to n. You have to guess which number I picked.
    Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

    You call a pre-defined API int guess(int num), which returns three possible results:
    0: your guess is equal to the number I picked (i.e. num == pick).
    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    Return the number that I picked.

    """

    def guess(n):
        pass

    low, high = 1, n
    while True:
        mid = (low + high) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res > 0:  # type: ignore
            low = mid + 1
        else:
            high = mid - 1


def firstBadVersion(self, n: int) -> int:
    """_LeetCode_Easy_

    You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
    """

    def isBadVersion(version):
        pass

    low = 1
    high = n + 1
    while low <= high:
        mid = (high + low) // 2
        result = isBadVersion(mid)
        if result:
            if mid == 1 or not isBadVersion(mid - 1):
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def minEatingSpeed(self, piles: list[int], h: int) -> int:
    """_Neetcode Medium_

    You are given an integer array 'piles' where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

    You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eat k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

    Return the minimum integer k such that you can eat all the bananas within h hours
    """
    import math
    lowest = 1
    highest = max(piles)
    result = highest

    while lowest <= highest:
        mid = (lowest + highest) // 2
        total_time = 0
        for p in piles:
            time_taken = math.ceil(p / mid)
            total_time += time_taken

        if total_time > h:
            lowest = mid + 1
        else:
            highest = mid - 1
            result = mid
    return result


class Search2DMatrix:
    """_Neetcode_Medium_

    You are given an m x n 2-D integer array `matrix` and an integer `target`.
    Each row in matrix is sorted in non-decreasing order.
    The first integer of every row is greater than the last integer of the previous row.
    Return true if target exists within matrix or false otherwise.
    """
    def brute_force(self, matrix: list[list[int]], target: int) -> bool:
        """
        Compare each element with the target. Not very efficient
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False
    
    def staircase_search(self, matrix: list[list[int]], target: int) -> bool:
        """
        Takes advantage of the fact that the matrix is sorted along both the rows and the columns. Similar to binary sort for a 1-D array
        Compare the target with the last element in the first row. If the element is greater than the
        target, remain on that row and check the lower column of that row. More efficient.
        
        Time complexity: O(m + n)
        Space complexity: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
    
    def binary_search(self, matrix: list[list[int]], target: int) -> bool:
        """
        Takes advantage of the fact that the matrix is sorted along both the rows and the columns. Considers the entire
        matrix as a `flattened 1-D array` and applies the true binary search. Even more efficient

        Time complexity: O(log(m * n))
        Space complexity: O(1)
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        left_pointer, right_pointer = 0, ROWS * COLS - 1
        while left_pointer <= right_pointer:
            mid = (right_pointer + left_pointer) // 2
            row, col = mid // COLS, mid % COLS
            if target > matrix[row][col]:
                left_pointer = mid + 1
            elif target < matrix[row][col]:
                right_pointer = mid - 1
            else:
                return True
        return False

    def double_binarysearch(self, matrix: list[list[int]], target: int) -> bool:
        """This method considers the matrix as a set of sorted rows, each row containing a set of sorted values
        We apply binary search to determine the row containg the search term, and then, apply binary search on the
        candidate row to find the cell containg the search term

        Time complexity: O(log(m * n))
        Space complexity: O(1)
        """

        rows = len(matrix)
        top_row, bottom_row = 0, rows - 1  # Top_row has lower index than bottom_row
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            else:
                break
        if not (top_row <= bottom_row):
            return False

        row_id = (top_row + bottom_row) // 2
        row = matrix[row_id]
        left_col, right_col = 0, len(row) - 1
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            if row[mid_col] == target:
                return True
            elif row[mid_col] > target:
                right_col = mid_col - 1
            else:
                left_col = mid_col + 1
        return False
