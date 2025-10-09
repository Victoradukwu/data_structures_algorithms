from typing import List


def getConcatenation(self, nums: List[int]) -> List[int]:
    """_Neetcode_Easy_

    You are given an integer array nums of length n. Create an array `ans` of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, `ans` is the concatenation of two nums arrays.

    Return the array ans
    """
    nums_length = len(nums)
    ans_length = 2 * nums_length
    last_idx = nums_length - 1
    ans = [0] * ans_length
    for i in range(ans_length):
        ans[i] = nums[i] if i <= last_idx else nums[i - nums_length]
    return ans
