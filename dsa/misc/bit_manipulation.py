from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        """_Leetcode_Easy_

        You are given an unsigned integer n. Return the number of 1 bits in its binary representation.
        You may assume n is a non-negative integer which fits within 32-bits.
        """
        # res = 0
        # for i in range(32): # Assuming a 32-bit integer
        #     if (1 << i) & n:
        #         res += 1
        # return res

        count = 0
        while n > 0:
            if n & 1: # If bitwise AND between n and 1 returns 1
                count += 1
            n = n >> 1 # same as n // 2
        return count

    def countBits(self, n: int) -> List[int]:
        """_Neetcode_Easy_

        Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
        Return an array output where output[i] is the number of 1's in the binary representation of i.
        """
        count_list = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                if i & 1:
                    count += 1
                i = i >> 1
            count_list.append(count)
        return count_list

    def reverseBits(self, n: int) -> int:
        """_Neetcode_Easy_

        Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.
        """
        res = 0
        for i in range(32):
            x = n >> i
            bit = x & 1
            res += bit << (31 - i)
        return res
