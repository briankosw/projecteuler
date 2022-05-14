def solution() -> int:
    """
    Loop from 0 to 1000 and check if the number is a multiple of 3 or 5
    """
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def solution() -> int:
    """
    Calculate the sum of the arithmetic sequences for 3, 5, and 15, and then
    sum up the threes and fives and subtract the fifteens
    """
    three = ((999 - 3) // 3 + 1) * (3 + 999) // 2
    five = ((995 - 5) // 5 + 1) * (5 + 995) // 2
    fifteen = ((990 - 15) // 15 + 1) * (15 + 990) // 2
    return three + five - fifteen


if __name__ == "__main__":
    print(solution())

