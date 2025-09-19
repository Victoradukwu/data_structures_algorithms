# from typing import Any, List, Optional

int_lst = [5, 2, 9, 1, 5, 6]
str_lst = ["banana", "date", "apple", "cherry", "Dated"]


def bubble_sort(arr):
    """
    This algorithm begins at the start of the array and compares each pair of adjacent elements. 
    If the first element is greater than the second, they are swapped. This process is repeated until no swaps are needed, indicating that the array is sorted.
    1. Start at the beginning of the array.
    2. Compare the first element with the second. If the first is bigger than the second, swap their positions. otherwise, leave them and compare the second and the third.
    3. Repeat step 2 until the end of the array. This completes one pass and effectively pushes the biggest item to the extreme right.
    4. Repeat the entire process until no swaps are needed in a complete pass through the array.
    """
    
    arr_length = len(arr)
    for i in range(arr_length-1):
        swapped = False
        for j in range(arr_length-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # The elements from i to the end are already sorted
            break
    return arr


def selection_sort(arr):
    """
    This algorithm divides the input list into two parts: the sorted part and the unsorted part. 
    It repeatedly selects the smallest (or largest, depending on the order) element from the unsorted part 
    and moves it to the end of the sorted part.
    1. Start with the first element as the minimum.
    2. Compare this minimum with the next elements. If a smaller element is found, update the minimum.
    3. Once the end of the array is reached, swap the minimum with the first unsorted element.
    4. Repeat the process for the remaining unsorted elements.
    """
    array_length = len(arr)
    for i in range(array_length - 1):
        min_idx = i
        for j in range(i+1, array_length):
            if arr[j] < arr[min_idx]:
                min_idx=j
        min_val = arr.pop(min_idx)
        arr.insert(i, min_val)
    return arr


def insertion_sort(arr):
    """
    This is a STABLE sorting algorithm with a O(n**2)
    
    This sorting algorithm divides the array into two: sorted (initially empty) and unsorted. It loops though the unsorted array. Takes one element at a time, determines it right position in the sorted array and inserts it there to mainttain the sorting order
    
    1. Start with the first item and add it to the sorted array
    2. Pick the next item. loop through the sorted array, determine where it fits and insert it there
    3. Repeat step two until the unsorted array is exhausted
    """
    arr_length = len(arr)
    for i in range(arr_length):
        j = i - 1
        while arr[j] > arr[j + 1] and j >= 0: # Loop will be skipped for the first element, since the condition j >= 0 evaluates to False
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


def quick_sort(arr, low=0, high=None):
    """_summary_
    Quite similar to merge sort
    
    Worst case Time complexity of O(n**2), but average case time complexity of O(nlogn)
    The worst case space complexity is O(n)
    Quicksort is generally considered as a non-stable algorithm

    The idea behind quicksort is to pick an index, which is called the pivot. We then partition the array such that every value to the left is less than or equal to the pivot and every value to the right is greater than the pivot.
    """
    if not high:
        high = len(arr) - 1

    if high <= low:
        return arr

    pivot = arr[high]
    left = low  # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1

    # Move pivot in-between left & right sides
    arr[left], arr[high] = arr[high], arr[left]

    quick_sort(arr, low, left - 1)  # Quick sort left side
    quick_sort(arr, left + 1, high)  # Quick sort right side

    return arr


def merge_sort(arr):
    """Has a time complexity of O(nlogn) and it is a stable algorithm, used by most programming languages
    Note that logn is more efficiant than n, hence nlogn is more efficient than n**2
    Uses recursion
    """
    if len(arr)<=1:
        return arr
    
    def merge(left_half, right_half):
        result = []
        
        i = j = 0 #Using two pointers; i loops the left half and j loops thru the right half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
        result.extend(left_half[i:])
        result.extend(right_half[j:])
        
        return result 
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    
    return merge(sorted_left, sorted_right)
    

def bucket_sort(arr):
    """
    Bucket sort has the best big O complexity but it is rarely used bue to it's constraints: it can only be used if we already know the range of possible values of the elements of the array. It has a worst case complexity of O(n)
    Increased memory requirements, as each buck needs extra space.

    Works well if the data distribution is (roughly) uniform; skewed data causes overloaded bucket, which leads to decrease in performance

    requires care in chosing number of buckets: two many buckets==>high memory requirement; too few buckets==>slow internal sort. Common choices are are `n` and ` √n

    A difficulty with bucket sort is that data data must be mappable to bucket index. This is not a problem for numbers but quite tricky for string and other complex objects

    Space complexity of O(n + K), where n is the array length and k is the number of buskets
    """
    counts = [0] * len(set(arr))

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
    

                
print('original: ', int_lst, str_lst)
# print(f'Bubble sort: {bubble_sort(int_lst)}')
# print(f'Bubble sort: {bubble_sort(str_lst)}')

# print(f'Selection sort: {selection_sort(int_lst)}')
# print(f'Selection sort: {selection_sort(str_lst)}')

# print(f'Insertion sort: {insertion_sort(int_lst)}')
# print(f'Insertion sort: {insertion_sort(str_lst)}')

print(f'Quick sort: {quick_sort(int_lst)}')
print(f'Quick sort: {quick_sort(str_lst)}')

# print(f'Merge sort: {merge_sort(int_lst)}')
# print(f'Merge sort: {merge_sort(str_lst)}')

# print(f"Bucket sort: {bucket_sort(int_lst)}")