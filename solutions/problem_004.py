def is_palindrome(num: int) -> bool:
    """
    Check if num is a palindrome by flipping the second half and comparing it with the
    first half
    """
    if num % 10 == 0:
        return False
    pal = 0
    while num > pal:
        pal = pal * 10 + num % 10
        num //= 10
    return num == pal or num == pal // 10

def solution() -> int:
    """
    Brute force try all the possible products of two 3-digit numbers
    """
    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            if is_palindrome(i * j):
                largest_palindrome = max(largest_palindrome, i * j)
    return largest_palindrome

def solution() -> int:
    """
    A palindrome made from the product of two 3-digit numbers x, y has the following form:

    100000a + 10000b + 1000c + 100c + 10b + 1a = x * y

    which is equal to 100001a + 10010b + 1100c = 11 * (9091a + 910b + 100c) = x * y. We
    now know that either x or y must be divisble by 11, and we can use this information
    to slightly reduce the number of 3-digit numbers to check
    """
    largest_palindrome = 0
    for i in range(110, 1000, 11):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                largest_palindrome = max(largest_palindrome, i * j)
    return largest_palindrome


if __name__ == "__main__":
    print(solution())
