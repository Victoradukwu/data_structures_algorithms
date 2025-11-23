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

    This implementation uses two pointers, 'next_unique_index' and 'r'
    """
    next_unique_index = 1  # index 0 has already been taken, since nums is sorted
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[next_unique_index] = nums[r]
            next_unique_index += 1
    return next_unique_index


def removeDuplicatesII(nums: list[int]) -> int:
    """_Leetcode_Medium

    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
    Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    This implementation uses two pointers
    """
    left = right = 0
    n = len(nums)

    while right < n:
        count = 1
        while right + 1 < n and nums[right] == nums[right + 1]:
            right += 1
            count += 1
        for _ in range(min(2, count)):
            nums[left] = nums[right]
            left += 1
        right += 1
    return left


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
