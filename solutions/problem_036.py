def palindrome10(num: int) -> bool:
    """
    Calculate the second half reversed and compare it to the first half
    """
    val = 0
    while num > val:
        val = val * 10 + num % 10
        num //= 10
    return val == num or val // 10 == num

def palindrome2(num: int) -> bool:
    """
    Generate the bits and check to see if it's a palindrome
    """
    bits = []
    while num:
        bits.append(num & 1)
        num >>= 1
    i, j = 0, len(bits) - 1
    while i < j:
        if bits[i] != bits[j]:
            return False
        i += 1
        j -= 1
    return True

def solution() -> int:
    total = 0
    for i in range(1_000_000):
        if palindrome10(i) and palindrome2(i):
            print(i)
            total += i
    return total


if __name__ == "__main__":
    print(solution())
