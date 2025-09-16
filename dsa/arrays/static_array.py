from typing import List


def removeDuplicates(nums: list[int]) -> int:
    """_Neetcode_

    You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.
    After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

    Note:
    The order of the unique elements should remain the same as in the original array.
    It is not necessary to consider elements beyond the first k positions of the array.
    To be accepted, the first k elements of `nums` must contain all the unique elements.
    Return k as the final result.
    
    This implementation uses two pointers, 'land_unique_index' and 'r'
    """
    last_unique_index = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[last_unique_index] = nums[r]
            last_unique_index += 1
    return last_unique_index


def removeElement(nums: List[int], val: int) -> int:
    """_Neetcode_Easy_

    You are given an integer array `nums` and an integer `val`. Your task is to remove all occurrences of val from `nums` in-place.
    After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of `nums` do not contain val.

    Note:
    The order of the elements which are not equal to val does not matter.
    It is not necessary to consider elements beyond the first k positions of the array.
    To be accepted, the first k elements of `nums` must contain only elements not equal to val.
    Return k as the final result.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    unique_elements = [x for x in nums if x != val]
    length_unique_elements = len(unique_elements)
    nums[0:length_unique_elements] = unique_elements
    return length_unique_elements


def removeElement2(nums: list[int], val: int) -> int:
    """_Neetcode_Easy_

    A better implementation of `removeElement`, using two pointers, `k` and `l`
    Time complexity: O(n)
    Space complexity: O(1)
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
