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