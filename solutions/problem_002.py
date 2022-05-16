def solution() -> int:
    """
    Calculate the Fibonacci sequence and sum up the even numbers
    """
    even_fib_sum = 0
    a = b = 1
    while b <= 4_000_000:
        if b % 2 == 0:
            even_fib_sum += b
        a, b = b, a + b
    return even_fib_sum


def solution() -> int:
    """
    Observe the first few numbers in the Fibonacci sequence:

    1, 1, 2, 3, 5, 8, 13, 21, 34, ...

    where every third number is even. We can represent the sequence as follows:

    x, y, x + y, x + 2y, 2x + 3y, 3x + 5y, 5x + 8y, 8x + 13y, ...

    We can directly calculate the even numbers and avoid modulo operations
    """
    even_fib_sum = 0
    a = b = 1
    while b <= 4_000_000:
        even_fib_sum += a + b
        a, b = a + 2 * b, 2 * a + 3 * b
    return even_fib_sum


if __name__ == "__main__":
    print(solution())
