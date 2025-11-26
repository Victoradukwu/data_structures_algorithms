

from collections import defaultdict


class MaximumSumSubArray:
    """_Neetcode_medium
    Given an array of integers nums, find the subarray with the largest sum and return the sum.
    A subarray is a contiguous non-empty sequence of elements within an array.
    """
    
    
    def brute_force(self, nums:list[int])->int:
        """
        Time Complexity: O(n**2)
        Space Complexity: O(1)
        """
        
        max_sum = nums[0]
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum
    
    def kadanes(self, nums: list[int])->int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(max_sum, 0)  # Discard sums less than zero
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum
    

class MaximumSumCircularSubArray:
    """_Neetcode_medium
    You are given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
    A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

    A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
    """
    def brute(self, nums:list[int])->int:
        """_Brute force
        Time Complexity: O(n**2)
        Space Complexity: O(1)
        """
        n = len(nums)
        max_sum = nums[0]

        for i in range(n):
            cur_sum = 0
            for j in range(i, i + n):  # i +n causes the iteration to cycle and stop at position just before i
                cur_sum += nums[j % n]  # modulus ensures that the effective index is within the range of the array
                max_sum = max(max_sum, cur_sum)

        return max_sum
    
    def kadanes(self, nums: list[int]) -> int:
        """_Kadane's Algorithm

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax
    

class LongestTurbulentSubarray:
    """Neetcode_Medium

    You are given an integer array `arr`, return the length of a maximum size turbulent subarray of arr.
    A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
    More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

    For i <= k < j:
    arr[k] > arr[k + 1] when k is odd, and
    arr[k] < arr[k + 1] when k is even.
    Or, for i <= k < j:
    arr[k] > arr[k + 1] when k is even, and
    arr[k] < arr[k + 1] when k is odd.
    """
    
    def iteration(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        GREATER_THAN, LESS_THAN, EQUAL_TO = 1, 0, -1
        n = len(arr)
        global_count = 0
        curr_count = 0

        sign = EQUAL_TO  # the relationship btw (i-1)th item and the ith item
        for i in range(n - 1):  # iteration stops at send to the last item, since the last item does not have i + 1
            if arr[i] > arr[i + 1]:
                curr_count = curr_count + 1 if sign == LESS_THAN else 1
                sign = GREATER_THAN
            elif arr[i] < arr[i + 1]:
                curr_count = curr_count + 1 if sign == GREATER_THAN else 1
                sign = LESS_THAN
            else:  # Reset
                curr_count = 0
                sign = EQUAL_TO

            global_count = max(global_count, curr_count)

        return global_count + 1
    
    def sliding_window(self, arr: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right, res, prev = 0, 1, 1, ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and prev != ">":
                res = max(res, right - left + 1)
                right += 1
                prev = ">"
            elif arr[right - 1] < arr[right] and prev != "<":
                res = max(res, right - left + 1)
                right += 1
                prev = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev = ""

        return res
        

class ContainsNearbyDuplicates:
    """_Neetcode_medium_

    You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.
    """
    
    def brute(self, nums: list[int], k:int)-> bool:
        """_summary_

        Time Complexity: O(n*min(n, k))
        Space Complexity: O(1)
        """
        
        n = len(nums)
        for L in range(n):
            for R in range(L+1, min(n, L + k +1)):
                if nums[L] == nums[R]:
                    return True
        return False
    
    def hashmap(self, nums:list[int], k:int)->bool:
        """_Using Hashmap to add memoization to the brute force above

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cache = {} #Mapping values to their indexes
        for idx, val in enumerate(nums):
            if val in cache and idx - cache[val] <= k:
                return True
            cache[val] = idx
        return False
    
    def hashset(self, nums: list[int], k: int) -> bool:
        """_Using Hashset to add memoization to the brute force above

        Time Complexity: O(n)
        Space Complexity: O(min(n, k))
        """
        cache = set()
        L = 0
        n = len(nums)
        for R in range(n):
            if R-L > k:
                cache.remove(nums[L])
                L += 1
            if nums[R] in cache:
                return True
            cache.add(nums[R])
        return False


class MinSubarraryLength:
    """_Neetcode_Medium_
    
    You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
    A subarray is a contiguous non-empty sequence of elements within an array.
    """
    def brute(self, target: int, nums:list[int]):
        res = float("inf")

        n = len(nums)

        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum >= target:
                    res = min(res, j - i + 1)
                    break
        return 0 if res == float("inf") else res
    
    def sliding_window(self, target: int, nums:list[int]):
        n = len(nums)
        res = float("inf")
        left, total = 0, 0
        
        for right in range(n):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if res == float("inf") else res


class LongestSubstringNoRepetition:
    """_Neetcode_medium_

    Given a string s, find the length of the longest substring without duplicate characters.
    A substring is a contiguous sequence of characters within a string.
    """
    
    def brute_force(self, s: str) -> int:
        """
        Time Complexity: O(n*m); n = string length and m = number of unique characters
        Space Complexity: O(m)
        """
        res = 0
        n = len(s)
        for i in range(n):
            charSet = set()
            for j in range(i, n):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
    
    def sliding_window(self, s: str) -> int:
        """
        Time Complexity: O(n); n = string length and m = number of unique characters
        Space Complexity: O(m)
        """
        n = len(s)
        st = set()
        max_length = 0
        left = 0
        for right in range(n):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
            

class LongestRepeartingCharaterReplacement:
    """_Neetcode_Medium_

    You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
    After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
    """
    def brute_force(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n**2)
        Space Cpmlexity: O(m)
        
        n is the length of the string and m is the number of unique characters in the string
        """
        res = 0
        n = len(s)
        for i in range(n):
            count = defaultdict(int)
            maxf = 0
            for j in range(i, n):
                count[s[j]] += 1
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k: # j - i + 1 is the length of the window
                    res = max(res, j - i + 1)
        return res

    def sliding_window(self, s: str, k: int) -> int:
        """
        Time Complexity: O(m*n)
        Space Cpmlexity: O(m)

        n is the length of the string and m is the number of unique characters in the string
        """

        res = 0
        charSet = set(s)

        for c in charSet:
            count = left = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1

                res = max(res, right - left + 1)
        return res
    
    def optimized_sliding_window(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Cpmlexity: O(m)

        n is the length of the string and m is the number of unique characters in the string
        """
        count = defaultdict(int)
        res = 0
        left = 0
        maxf = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res


class TrappingRainWater:
    """_Neetcode_Hard_
    
    You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
    Return the maximum area of water that can be trapped between the bars.
    """
    
    def brute_force(self, height: list[int]) -> int:
        """_summary_

        Time Complexity: O(n**2)
        Space Complexity: O(n)
        """
        n = len(height)
        cap = 0
        for i in range(1, n-1):
            left = max(height[:i]) 
            right = max(height[i+1:])
            h = min(left, right)
            vol = max(h-height[i], 0)
            cap += vol
        return cap
    
    def enhanced_brute_force(self, height: list[int]) -> int:
        """_summary_
        Using Python builtin  max for maxLeft and maxRight would have worsened the time complexity to O(n**2)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i-1])

        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i+1])

        res = 0
        for i in range(1,n-1):
            res += max(min(leftMax[i], rightMax[i]) - height[i], 0)
        return res
    
    def two_pointers(self, height: list[int]) -> int:
        """_summary_

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        return res
    


class RangeSumQuery:
    def __init__(self, nums:list[int]) -> None:
        self.prefix_sums = []
        total = 0
        for val in nums:
            total += val
            self.prefix_sums.append(total)
    
    def sumRange(self, left:int, right:int)->int:
        right_val = self.prefix_sums[right]
        left_val = self.prefix_sums[left - 1] if left > 0 else 0
        return right_val - left_val
    

class RangeSumQuery2D:
    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # A dummy row and a dummy column has been added at the the begining of the sumMatrix. This is why we have range(1, ROW + 1) and range(1, COL + 1). In the sunMat, the dummy elements will be 0 each. The dummies prevents raising of error when evaluating row-1 or col-1. Note that the dummies are not added to the original matrix. Position sumMat[r][c] corresponds to matrix[r-1][c-1]
        for r in range(1, ROWS+1):
            prefix = 0
            for c in range(1, COLS+1):
                prefix += matrix[r-1][c-1]
                above = self.sumMat[r-1][c]
                self.sumMat[r][c] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1 # a dummy row and a dummy col have been added to self.sumMat
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft
    
    def print(self):
        """Just for debugging purposes"""
        for row in self.sumMat:
            print(row)
        


def longest_subarray(arr: list[int]) -> int:
    """_summary_
    Find the length of longest subarray with the same value in each position
    ie longest consecutive repetition of a character
    """
    length = 0
    left = 0

    for right in range(len(arr)):
        if arr[right] != arr[left]:
            left = right
        length = max(length, right - left + 1)
    return length


def longest_consecutive_sequence(nums: list[int])->int:
    """_Leetcode_Medium_

    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    """
    
    st = set(nums)
    max_length = 0
    
    for num in nums:
        if num - 1 not in st:
            curr_length = 0
            while num + curr_length in st:
                curr_length += 1
            max_length = max(max_length, curr_length)
    return max_length


def is_palindrome(s: str) -> bool:
    """Neetcode_Easy

    This version uses two-pointer approach
    Time Complexity: O(n)
    Space
    """

    n = len(s)
    if n == 0:
        return True
    left, right = 0, n - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1  # skip
        while left < right and not s[right].isalnum():
            right -= 1 #skip
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


def container_with_most_water(self, height: list[int]) -> int:
    """_Neetcode_medium_

    You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.
    
    We'll use the two-pointer approach
    """
    
    n = len(height)
    L = 0
    R = n -1
    max_area = 0
    
    while L < R:
        h = min(height[L], height[R])
        w = R -L
        area = w * h
        max_area = max(max_area, area)
        
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1

    return max_area
    

def pivotIndex(self, nums: list[int]) -> int:
    """_Neetcode_Easy

    You are given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
    Return the leftmost pivot index. If no such index exists, return -1.
    """
    total = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1


def productExceptSelf(nums: list[int]):
    """Leetcode_Medium_

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    
    This solution uses two passes. The first pass (prefix) multiplies every element before item i. The second pass multiplies every element after item
    Effectively, all elements except i are multiplied
    
    Time complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    res = [1] * (n)

    prefix = postfix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


def subarraySum(nums: list[int], k: int) -> int:
    """Neetcode_Medium_

    You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    A subarray is a contiguous non-empty sequence of elements within an array.
    """
    total = 0
    counter = 0
    dct = defaultdict(int)
    
    for i in range(len(nums)):
        total += nums[i]
        if total == k:
            counter += 1
        if total - k in dct:
            counter += dct[total-k]
        dct[total] += 1
    return counter