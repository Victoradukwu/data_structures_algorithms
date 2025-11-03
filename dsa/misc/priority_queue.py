import heapq
from typing import List


class PriorityQueue:
    """
    The advantage of Priority Queue over BST is that the min/max can be obtaied in time complexity  O(1)
    Anothr one is that building BST is time complexity of O(nlogn), but for Priorit Queue, it is O(n)--heapify

    The downside is that search is O(n), unlike bst where it is O(logn)
    Note: The Priority Queue can be used to sort an array: heapify, and then pop each item, giving a time complexity of O(nlogn)
    Note: Priority Queue is not good for searching
    """
    def __init__(self) -> None:
        self.heap = []
        
    def push(self, val):
        self.heap.append(val)
        # i is the index of the recently added value. The first item in the array is at index 1, with a 0 at index 0
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i] # Swap
            i = i // 2

    def pop(self):
        """
        Time Complexity: O(logn)
        """
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]  # save the return value, since we're going to overwrite it soon

        # Move last value to root. This is to allow us percolate down, since percolate down is more efficient than percolate up
        self.heap[1] = self.heap.pop()
        i = 1

        # Percolate down
        # The last half of the list have no children, so, no need to check for a possible swap while percolating down
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[2 * i + 1] < self.heap[i]
            ):  # if there is a right child and the right child is less than both the node and left child
                # Swap right child
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:  # The left child is less than the node, so swap left child
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break
        return res
    
    def heapify(self, arr: List[int])->None:
        """
        Time Complexity: O(n)
        """
        # 0-th position is moved to the end, so that the 0th position can be ignored
        arr.append(arr[0])

        self.heap = arr
        # The last half of the list have no children, so, no need to check for a possible swap. The check (percolate down) is only done for the first half of the list
        cur = (len(self.heap) - 1) // 2
        while cur > 0:  # Real data starts from index 1, not index 0
            # Percolate down, for each node between 1 and curr inclusive
            i = cur
            while 2 * i < len(self.heap):
                if (
                    2 * i + 1 < len(self.heap)
                    and self.heap[2 * i + 1] < self.heap[2 * i]
                    and self.heap[2 * i + 1] < self.heap[i]
                ):
                    # Swap right child
                    self.heap[i], self.heap[2 * 1 + i] = self.heap[2 * i + 1], self.heap[i]
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                    i = 2 * i
                else:
                    break
            cur -= 1
    

class KthLargest:
    """
    Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

    Implement the following methods:
    `constructor(int k, int[] nums)` Initializes the object given an integer k and the stream of integers nums.
    `int add(int val)` Adds the integer val to the stream and returns the kth largest integer in the stream.
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


def lastStoneWeight(stones: List[int]) -> int:
    """_Neetcode_Easy_

    You are given an array of integers `stones` where `stones[i]` represents the weight of the `ith` stone.
    We want to run a simulation on the stones as follows:

    At each step we choose the two heaviest stones, with weight `x` and `y` and smash them together
    If x == y, both stones are destroyed
    If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    Continue the simulation until there is no more than one stone remaining.

    Return the weight of the last remaining stone or return 0 if none remain.
    """
    import heapq
    
    if not stones:
        return 0
    if len(stones) == 1:
        return stones[0]

    heap = [-x for x in stones] # Create a max-heap, since a pop should return the largest element, 0-indexed
    heapq.heapify(heap)

    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        diff = x - y
        if diff != 0:
            heapq.heappush(heap, diff)
    return abs(heap[0]) if heap else 0


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """_Neetcode_Medium_

    You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
    Return the k closest points to the origin (0, 0).
    The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
    You may return the answer in any order.
    """
    import math
    def sorter(pt):
        return math.sqrt(pt[0]**2 + pt[1]**2) # We could do without the sqrt, though
    
    sorted_points = sorted(points, key=sorter)
    return sorted_points[:k]

def findKthLargest(nums: List[int], k: int) -> int:
    """_Neetcode_Medium_

    Given an unsorted array of integers `nums` and an integer `k`, return the `kth` largest element in the array.
    By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
    """
    # return sorted(nums, reverse=True)[k - 1]. #An alternative implementation
    return heapq.nlargest(k, nums)[-1]

