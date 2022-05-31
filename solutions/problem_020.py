from math import factorial


def solution() -> int:
    num = factorial(100)
    digit_sum = 0
    while num:
        digit_sum += num % 10
        num //= 10
    return digit_sum


if __name__ == "__main__":
    print(solution())
