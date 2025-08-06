from typing import Any, List

array = arr = [3, 7, 2, 9, 5]


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
    high = len(arr)-1
    
    while low<=high:
        mid = (high + low)//2
        if search_term == mid:
            return mid
        if search_term < mid:
            high = mid
        else:
            low=mid
    return -1

print(f'Linear search for 3 in {array}: {linear_search(array, 3)}')
print(f'Linear search for 4 in {array}: {linear_search(array, 4)}')
print(f'Linear search for 9 in {array}: {linear_search(array, 9)}')

print(f'Binary search for 3 in {array}: {linear_search(array, 3)}')
print(f'Binary search for 4 in {array}: {linear_search(array, 4)}')
print(f'Binary search for 9 in {array}: {linear_search(array, 9)}')