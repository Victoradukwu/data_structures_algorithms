from typing import Any, List

array = [2, 3, 5, 7, 9]
array2 = [-1, 0, 3, 5, 9, 12]


def linear_search(arr: List[Any], search_term:Any)->int:
    """Time complexity of O(n)"""
    for i in range(len(arr)):
        if arr[i] == search_term:
            return i
    return -1


def binary_search(arr: List[Any], search_term: Any)->int:
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


def minEatingSpeed(self, piles: List[int], h: int) -> int:
    """_Neetcode Midium_

    You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

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
            total_time += math.ceil(p/mid)

        if total_time > h:
            lowest = mid + 1
        else:
            highest = mid - 1
            result = mid
    return result