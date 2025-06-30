from typing import Any, List

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
        if not swapped:
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
    This sorting algorithm divides the array into two: sorted (initially empty) and unsorted. It loops though the unsorted array. Takes one element at a time, determines it right position in the sorted array and inserts it there to mainttain the sorting order
    
    1. Start with the first item and add it to the sorted array
    2. Pick the next item. loop through the sorted array, determine where it fits and insert it there
    3. Repeat step two until the unsorted array is exhausted
    """
    
    array_length = len(arr)
    for i in range(1, array_length):
        curr_val = arr[i]
        insert_index = i
        for j in range(i):
            if curr_val < arr[j]:
                insert_index = j
                break
        if insert_index != i:
            arr.insert(insert_index, arr.pop(i))
    return arr


def quick_sort(arr, low=0, high=None):
    def partition(array:List[Any], low:int, high:int)->int:
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[high] = array[high], array[i]
        
        return i
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        idx = partition(arr, low, high)
        quick_sort(arr, low=low, high=idx-1)
        quick_sort(arr, low=idx+1, high=high)
    return arr


def merge_soft(arr):
    if len(arr)<=1:
        return arr
    
    def merge(left_half, right_half):
        result = []
        
        i = j = 0
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
    
    sorted_left = merge_soft(left_half)
    sorted_right = merge_soft(right_half)
    
    return merge(sorted_left, sorted_right)
    
    
    

                
print('original: ', int_lst, str_lst)
# print(f'Bubble sort: {bubble_sort(int_lst)}')
# print(f'Bubble sort: {bubble_sort(str_lst)}')

# print(f'Selection sort: {selection_sort(int_lst)}')
# print(f'Selection sort: {selection_sort(str_lst)}')

# print(f'Insertion sort: {insertion_sort(int_lst)}')
# print(f'Insertion sort: {insertion_sort(str_lst)}')

# print(f'Quick sort: {quick_sort(int_lst)}')
# print(f'Quick sort: {quick_sort(str_lst)}')

print(f'Merge sort: {merge_soft(int_lst)}')
print(f'Merge sort: {merge_soft(str_lst)}')