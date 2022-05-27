def solution() -> int:
    num = 2 ** 1000
    digits_sum = 0
    while num > 0:
        digits_sum += num % 10
        num //= 10
    return digits_sum


if __name__ == "__main__":
    print(solution())
