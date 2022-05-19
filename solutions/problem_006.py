def solution() -> int:
    """
    Use sum of arithmetic progression 1...100 to calculate square of sum of 1...100 then
    manually subtract square of numbers 1...100
    """
    sum_100 = 100 * (1 + 100) // 2
    ans = sum_100 * sum_100
    for i in range(1, 101):
        ans -= i * i
    return ans


def solution() -> int:
    """
    (1 + ... + n) ^ 2 = n ^ 2 * (n + 1) ^ 2 /4
    1 ^ 2 + ... + n ^ 2 = n * (n + 1) * (2n + 1) / 6
    """
    return 100 * 100 * 101 * 101 // 4 - 100 * 101 * 201 // 6


if __name__ == "__main__":
    print(solution())
