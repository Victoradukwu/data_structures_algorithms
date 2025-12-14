
from typing import Literal


def reverse_triplets(s: str) -> str:
    """_Misc_

    you are given a string s, and your goal is to produce a new string following a specific pattern. You are to take characters in sets of three, reverse the characters in each set, and then place them back into the string in their original positions, preserving the reverse order within each set. If 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should be left as they are.
    """
    result = []

    for i in range(0, len(s), 3):
        chunk = s[i : i + 3]
        if len(chunk) == 3:
            result.append(chunk[::-1])
        else:
            result.append(chunk)  # leave as-is

    return "".join(result)



def solution(s: str) -> str:
    """Codesignal

    You are provided with a string of alphanumeric characters in which each number, regardless of the number of digits, is always followed by at least one alphabetic character before the next number appears. The task requires you to return a transformed version of the string wherein the first alphabetic character following each number is moved to a new position within the string and characters in between are removed.

    Specifically, for each number in the original string, identify the next letter that follows it, and then reposition that character to directly precede the number. All spaces and punctuation marks between the number and the letter are removed.

    The length of the string `s` ranges from 3 to 10**6 (inclusive), and the string contains at least one number. The numbers in the string are all integers and are non-negative.
    """
    result = ""
    i = 0
    n = len(s)

    while i < n:
        while i < n - 1 and not s[i].isdigit():
            result += s[i]
            i += 1

        number = ''
        while i < n - 1 and s[i].isdigit():
            number += s[i]
            i += 1
        # i now holds the first non-digit xter

        while i < n - 1 and not s[i].isalpha():
            i += 1

        letter = s[i]  # First letter after number
        i += 1  # Next iteration starts from the second letter after the number

        result += f"{letter}{number}"

    return result


def add_days(date: str, n: int) -> str:
    """_Codesignal_

    You are given an initial date as a string in the format YYYY-MM-DD, along with an integer n which represents a number of days. Your task is to calculate the date after adding the given number of days to the initial date and return the result in the YYYY-MM-DD format.

    The given integer n is the number of days you have to add to the initial date and will be up to 50,000
    """

    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, date.split("-"))

    def is_leap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    while n > 0:
        month_days[2] = 29 if is_leap(year) else 28
        days_left_in_month = month_days[month] - day

        if n > days_left_in_month:
            n -= days_left_in_month + 1  # the +1 takes us the 1st of the next month
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1
        else:
            day += n
            n = 0

    return f"{year:04d}-{month:02d}-{day:02d}"


def evaluate_path(numbers):
    """_Codesignal

    A player moves along a path. The path is an array of integers, each ranging from -100 to 100, inclusive. The size of the array, n, can range from 1 to 500, inclusive. Each integer a_i in the array signifies how many steps the player can move and in which initial direction:
    - A positive integer allows the player to move that many steps to the right.
    - A negative integer directs the player to move that many steps to the left.
    - Zero signifies a blockade that prevents further movement.

    The game proceeds along the following rules:
    The player starts at the first position of the array and moves according to the value at the player's current position.
    If the value in the current position is zero, then the game ends. If the player's current position leads them outside of the array's boundaries, then their ability to move in the current direction ceases.
    If the latter happens, then the player reverses their direction and continues to move according to similar rules, but now the directions are inverted: positive integers lead the player to the left, and negative integers point to the right.

    The game ends when the player encounters a blockade or the array boundaries for the second time and so can no longer move.
    Return a tuple of (position, moves)
    """
    n = len(numbers)
    pos = 0
    moves = 0

    direction_reversed = False

    while True:
        step = numbers[pos]

        # Hitting a blockade ends game
        if step == 0:
            return (pos, moves)

        # Determine effective direction
        if not direction_reversed:
            target = pos + step
        else:
            # Flip meaning: + = left, - = right
            target = pos - step

        # Check if the move goes out of bounds
        if target < 0 or target >= n:
            if direction_reversed:
                # Second boundary hit → game ends
                return (pos, moves)
            else:
                direction_reversed = True
                # Retry from same pos
                continue

        # Valid move → jump to target; and the loop repeats
        pos = target
        moves += 1


def board_game(board, obstacle):
    """Codesignal

    Given an array `board`, you are to traverse the board. From each position on the board, determine the number of moves needed to get to the end of the board without hiting the `obstacle`. If it is not possible to traverse without hitting the obstacle, return -1 as the number of moves. board[i] indicates
    the number of steps that can be taken from `i`
    """
    n = len(board)
    moves = []

    for i in range(n):
        pos = i
        count = 0

        while pos < n:
            if board[pos] == obstacle:
                count = -1
                break
            jump = board[pos]
            pos += jump
            count += 1

        moves.append(count)

    return moves


def multiply_strings(num1: str, num2: str) -> str:
    """Codesignal

    You are tasked with writing a Python function to multiply two extremely large positive integers.

    Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.
    Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.
    Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.
    Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.
    """
    if len(num1.lstrip("0")) == 0 or len(num1.lstrip("0")) == 0:
        return "0"

    num1 = num1.lstrip("0")[::-1]
    num2 = num2.lstrip("0")[::-1]
    n1 = len(num1)
    n2 = len(num2)

    res = [0] * (n1 + n2)
    for i in range(n1):
        for j in range(n2):
            prod = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
            res[i + j] += prod
            res[i + j + 1] += res[i + j] // 10
            res[i + j] = res[i + j] % 10

    final_res = "".join([str(d) for d in reversed(res)])
    return final_res.lstrip("0")


def solution0(arrayA, arrayB, arrayC):
    """_Codesignal

    You are provided with three arrrays, with the following movt:
    First hop: arrayA to arrayB
    Second hop: arrayB to arrayA
    Third hop: arrayA to arrayC
    Fourth hop: arrayC to arrayA
    Then the pattern starts over, continuing until the journey ends.

    The rule to decide Gloria's move is: She uses the current element's value in the array as an index for her next array. For example, if Gloria is at arrayA[1]=2, she would move to arrayB[2].

    The pattern repeats itself until one of the following occurs:
    - Gloria's path repeats by visiting a position in arrayB or arrayC that was already visited, indicating that she is stuck in a loop and cannot progress further, OR
    - Gloria tries to access an index that exceeds the length of an array (for example, attempting to access arrayA[4] when arrayA only contains 4 items indexed from 0 to 3), in which case Gloria's journey should also stop.

    Your task is to calculate the sum of the maximum values that Gloria encounters in arrayB and arrayC during her journey.
    """
    indexA = 0
    curr = "A"
    prev = None
    visited_B = []
    visited_C = []
    max_B = 0
    max_C = 0
    while True:
        if curr == "A" and prev in [None, "C"]:
            if indexA >= len(arrayA):
                return sum([max_B, max_C])
            prev, curr = curr, "B"
            pos = arrayA[indexA]
            if pos in visited_B or pos >= len(arrayB):
                return sum([max_B, max_C])
            visited_B.append(pos)
            max_B = max(max_B, arrayB[pos])
            indexA = arrayB[pos]
        elif curr == "A" and prev == "B":
            if indexA >= len(arrayA):
                return sum([max_B, max_C])
            prev, curr = curr, "C"
            pos = arrayA[indexA]
            if pos in visited_C or pos >= len(arrayC):
                return sum([max_B, max_C])
            visited_C.append(pos)
            max_C = max(max_C, arrayC[pos])
            indexA = arrayC[pos]
        else:  # curr is either 'B' or 'C'
            prev, curr = curr, "A"


def solution1(roadA, roadB):
    """_Codesignal

    The game begins with Alice choosing a starting point on roadA, and then moving according to the following rules:

    Alice chooses a starting point on roadA.
    Each element in both the roads dictate exactly where to jump on the other road.
    Alice continues these jumps until she ends up at an already visited spot on either road in the current route, which signifies the end of this game.
    The distance covered in each jump is defined as 1 unit, no matter where she jumps to on the other road.
    Your task is to create a function that receives these two roads, roadA and roadB, as its parameters. The function should calculate and return an array of total distances Alice covers during her game for each possible starting point on roadA. More specifically, the result should be an array results, where results[i] denotes the total distance covered if Alice starts from roadA[i].
    """
    res = []
    for i in range(len(roadA)):
        count = 0
        is_A = True
        visited_a = [i]
        visited_b = []
        next = roadA[i]
        while True:
            if is_A:
                count += 1
                if next in visited_b:
                    res.append(count)
                    break
                visited_b.append(next)
                next = roadB[next]

            else:
                count += 1
                if next in visited_a:
                    res.append(count)
                    break
                visited_a.append(next)
                next = roadA[next]
            is_A = not is_A
    return res


def solution2(s):
    """Codesignal

    Given a string of n lowercase English characters, return a dictionary where each key-value pair represents a letter k and its corresponding numerical representation v, sorted in ascending order by the characters.
    The numerical representation v of each character k is computed as follows: replace k with the character that comes three characters before it in the alphabetical order (wrap around to z when this is less than a), then multiply the ASCII value of the new character by the frequency of k in the provided string.
    """
    from collections import Counter

    ORD_A = ord("a")
    ORD_Z = ord("z")
    res = {}
    ctr = Counter(list(s))

    for k, v in ctr.items():
        x = ord(k) - 3
        if x < ORD_A:
            x = ORD_Z - (ORD_A - x) + 1
        res[k] = x * v
    return dict(sorted(res.items()))


def calculate_jump(forest: list[int], start: int, direction: Literal[-1, 1]) -> int:
    """Codesignal

    `forest` is a list containing `1` (an obstacle) and `0`(an available position). Write a function that returns the minimum step
    size that can successfully take you from the `start` to the end of the forest without htting an obstacle. If it is not possible to navigate without hitting an obstacle, return `-1`. The `direction` is either `1` (moving rightwards) or `-1` (moving leftward)
    """

    jump = 1
    n = len(forest)

    while 0 <= start + (direction * jump) < n:
        pos = start
        while 0 <= pos < n:
            if forest[pos] == 1:
                break
            pos += direction * jump
        else:
            return jump
        jump += 1

    return jump


def best_step_size(dungeon, health):
    """_Codesignal

    You are given an array of n integer values, with n ranging from 1 to 500, inclusive. The array represents a path through a virtual dungeon, with certain positions marked as traps.

    Each element in the array ranges from −100000000000  to 100000000000 , inclusive, and represents the trap power. A value of 0 signifies a safe position, whereas positive integers indicate trap power — the higher the value, the harder it is to avoid and, hence, the more dangerous it is. Negative integers are traps that are easier to avoid, with negative values implying that the trap could potentially aid you rather than hinder.

    Your task is to move from the start position to the end position. For each step, you can move by x elements in the right direction only, where x ranges from 1 to n. Each time you step on a trap, you lose health points equal to the trap's power. You originally have h health points, where h is a positive integer ranging from 1 to 10^100

    Find the x that you must choose such that you lose the least amount of health points upon reaching the end of the array. Also, determine if there is no possible x that allows you to reach the end of the array with any remaining health points. In the latter case, return -1 to indicate that it's impossible to traverse the dungeon without succumbing to a fatal trap. If at any point your health points reach 0 or less, you are considered out of the game.
    """
    n = len(dungeon)
    best_x = -1
    best_rem = 0

    for x in range(1, n + 1):
        rem = health
        pos = 0

        while pos < n:
            rem -= dungeon[pos]
            pos += x

        if rem > best_rem:
            best_rem = rem
            best_x = x

    return best_x


def largest_step(garden, start, direction):
    """Codesignal

    Assume you have a community garden composed of n different types of flowers, with n ranging from 1 to 100. Each type is represented by a distinct number (1, 2, 3, ..., n). The garden is depicted as a 1D array, wherein each element indicates the type of flower planted in that specific location.

    Your task involves visiting each type of flower at least once, traversing the garden in a specific direction (either from left to right with smaller to larger indices, or from right to left). You can take exactly k number of steps in the chosen direction, visiting a new location.

    Write a Python function, largest_step(garden, start, direction), that accepts as input the garden as an array, your starting position, and the direction in which you want to travel. This function is expected to compute and return the largest-sized step step that you can take so that you can visit each type of flower existing in the garden at least once.

    If no such value of step enables you to visit all types of flowers at least once, the function should return -1. The direction is given as an integer — 1 indicates moving towards larger indices (right), while -1 suggests moving towards smaller ones (left).
    """
    n = len(garden)
    x = n  # setting x to maximum and be decrementing, since we are looking for highest value that satisfies the condition
    flower_set = set(garden)  # a set of UNIQUE flowers, since the garden can have the same flower in multiple places
    while x > 0:
        visited = set()
        pos = start
        visited.add(garden[pos])  # the flower at the starting positon must always be visited
        while 0 <= pos + (x * direction) < n:
            pos = pos + (direction * x)
            visited.add(garden[pos])
        if visited == flower_set:
            return x
        x -= 1
    return -1


def best_rotation_with_min_manhattan0(array1, array2):
    """Codesignal

    Prepare to challenge your array manipulation skills! Consider two arrays, array1 and array2, each consisting of n non-negative integers.

    Your task is to discover a rotation of array1 that minimizes the Manhattan distance with array2.
    You need to return the smallest possible Manhattan distance obtained through this operation.

    Let's say that you find multiple rotations of array1 that yield the same smallest Manhattan distance with array2. In this case, you should return the rotated array that, when converted into an integer number by concatenating all of its digits (from left to right), would be the smallest.

    Consider the array as periodic; that is, after the last element, the first one follows.

    Keep in mind that the size of the two arrays is always the same, and the arrays are not necessarily sorted at the beginning.

    If array1 is exactly the same as array2 from the beginning, output the original array1 and the Manhattan distance 0

    Remember, the ultimate goal is to minimize the Manhattan distance between array1 and array2 through the least alterations possible to array1. Let's see how small you can get!
    """

    def manhattan(arr1, arr2):
        sum_ = 0
        for i in range(len(arr1)):
            sum_ += abs(arr1[i] - arr2[i])
        print(arr1, arr2, sum_)
        return sum_

    if array1 == array2:
        return array1, 0
    res = []
    n = len(array1)
    arr = array1.copy()  # Copy to avoid mutating the input
    for _ in range(n):
        manh = manhattan(arr, array2)
        res.append((arr.copy(), manh))
        arr.insert(0, arr.pop())
    res2 = sorted(res, key=lambda x: (x[1], int("".join(map(str, x[0])))))

    return res2[0]


def best_rotation_with_min_manhattan(array1, array2):
    """Codesignal

    Prepare to challenge your array manipulation skills! Consider two arrays, array1 and array2, each consisting of n non-negative integers.

    Your task is to discover a rotation of array1 that minimizes the Manhattan distance with array2.
    You need to return the smallest possible Manhattan distance obtained through this operation.

    Let's say that you find multiple rotations of array1 that yield the same smallest Manhattan distance with array2. In this case, you should return the rotated array that, when converted into an integer number by concatenating all of its digits (from left to right), would be the smallest.

    Consider the array as periodic; that is, after the last element, the first one follows.

    Keep in mind that the size of the two arrays is always the same, and the arrays are not necessarily sorted at the beginning.

    If array1 is exactly the same as array2 from the beginning, output the original array1 and the Manhattan distance 0

    Remember, the ultimate goal is to minimize the Manhattan distance between array1 and array2 through the least alterations possible to array1. Let's see how small you can get!
    """
    n = len(array1)
    if array1 == array2:
        return array1, 0

    def manhattan(arr1, arr2):
        return sum(abs(x - y) for x, y in zip(arr1, arr2))

    best_distance = manhattan(array1, array2)
    best_rotation = array1

    for k in range(n):
        rotated = array1[k:] + array1[:k]  # left rotation (anti-clockwise rotation) ie 1st item is moved to the last

        dist = manhattan(rotated, array2)

        if dist < best_distance:
            best_distance = dist
            best_rotation = rotated
        elif dist == best_distance:
            # Break ties by comparing concatenated integer form
            if int("".join(map(str, rotated))) < int("".join(map(str, best_rotation))):
                best_rotation = rotated

    return best_rotation, best_distance


def solution3(s: str):
    """Codesignal

    You are given a string s containing only uppercase letters, with its length n ranging from 1 to 100, inclusive. Your task involves series of sequential comparisons resulting in the removal of certain characters, following this process:

    Form neighbouring pairs in the string sequentially (pair the first and second characters, the third and fourth, and so forth). If the string length is odd, keep the last character unpaired.
    For each pair, compare the characters and remove the character that comes earlier in the lexicographical order. If they are the same, remove the first character in the pair.
    These two steps define a round of operation. Perform these rounds until the string becomes empty.
    If the string length after a round is 1, in the next round the last remaining character is removed and the process terminates.
    Your task is to implement a Python function, solution(s), where s is the initial input string. The function should follow the described process and return a list of the removed letters in the order of their removal.

    As an example, if s = "BCAAB", the output should be ['B', 'A', 'A', 'B', 'C'].
    """
    removed = []

    while s:
        if len(s) == 1:
            removed.append(s[0])
            break
        i = 0
        rem = ""
        while i <= len(s) - 1:
            if i == len(s) - 1:
                rem += s[i]
                break
            else:
                removed.append(min(s[i + 1], s[i]))
                rem += max(s[i + 1], s[i])
                i += 2

        s = rem
    return removed


def solution4(knights: list[int]) -> int:
    """Codesignal

    Imagine a medieval tournament where knights participate in jousting matches. The knights are arranged in a circular formation (represented as an array in your program), and each knight is initially assigned strength, represented as integers from 1 to 100, determined randomly.

    The game consists of rounds. On each round, each knight fights the knight on his right side by subtracting the strength of his opponent from his own. Since this is a circular game, the knight on the right side of the last knight in the array is the first knight. Note that all matches are played in parallel, so the strengths are updated only after all matches are played. If after a match, a knight's strength becomes equal to or less than zero, symbolizing the knight's defeat, the knight is removed from the game in the next round.

    The game continues until a situation develops in which no more moves can be made. This happens either when there is just one knight standing or all remaining knights have equal strength meaning no knight can win a match.

    Given the list of knights' strengths in the initial order, your program should calculate the number of rounds in the tournament.
    """

    rounds = 0
    knights_copy = knights.copy()
    while True:
        # If all knight powers are equal or no knight is left standing
        if not knights_copy or len(set(knights_copy)) == 1:
            return rounds

        n = len(knights_copy)
        new_knights = []
        for i in range(n):
            x = knights_copy[i] - knights_copy[(i + 1) % n]
            if x > 0:
                new_knights.append(x)
        rounds += 1
        knights_copy = new_knights


def house_game(houses):
    """Codesignal

    In a unique town, there's a popular game that involves the town's houses and their numbers. What's special about this town is that each house is sequentially numbered from 1 to n. The game is played based on an interesting rule regarding these house numbers.

    At each step of the game, every house number must "donate" one of its digits to the house on its right (or to the first house in the case of the last house). The particular digit to be transferred in each step is determined by the current game step: during the i-th step, the i-th digit from the right of each house number (1-indexed) is transferred. If a house number doesn't have the specified number of digits for a step, it doesn't donate any digit in that step.

    During the transfer, the chosen digit is removed from its position in the donor house number and then added to the front (leftmost side) of the receiving house number. All numbers change simultaneously.

    The function, house_game(houses), should simulate each step of the game, starting from transferring the rightmost (1st digit) and proceeding one digit position towards the left in each successive step, until there is no change in the house numbers from one step to the next. It should return the sequence of house numbers at the end.

    It is guaranteed that there are at least two houses and there is no digit 0 in the numbers.
    """
    houses = [str(h) for h in houses]
    step = 1

    while True:
        n = len(houses)
        donated = [""] * n
        new_houses = houses[:]  # Use a copy to avoid inadvertent mutation

        # Determine donations
        for i in range(n):
            s = houses[i]
            if len(s) >= step:
                pos = len(s) - step
                donated[i] = s[pos]
                new_houses[i] = s[:pos] + s[pos + 1 :]

        # Apply donations simultaneously
        for i in range(n):
            if donated[i]:
                next_i = (i + 1) % n
                new_houses[next_i] = donated[i] + new_houses[next_i]

        if new_houses == houses:
            return [int(h) for h in houses]

        houses = new_houses
        step += 1
