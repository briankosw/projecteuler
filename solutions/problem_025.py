import math

def solution() -> int:
    """
    Manually calculate Fibonacci sequence
    """
    a, b = 1, 1
    idx = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        idx += 1
    return idx


def solution() -> int:
    """
    Fn = phi ** n / sqrt(5), which needs to be greater than 10 ** 999 in order to have
    1000 digits
    """
    phi = (1 + 5 ** 0.5) / 2
    return math.ceil((999 * math.log(10) + math.log(5) / 2) / math.log(phi))


if __name__ == "__main__":
    print(solution())
