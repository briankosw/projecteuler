def solution() -> int:
    """
    In order for number x to be evenly divisible by all numbers from 1 to 20, x naturally
    needs to be evenly divisble by all factors of all numbers from 1 to 20. Therefore,
    find the factors for all the numbers from 1 to 20.

    1 = 1
    2 = 2
    3 = 3
    4 = 2 ** 2
    5 = 5
    6 = 2 * 3
    7 = 7
    8 = 2 ** 3
    ...
    20 = 2 ** 2 * 5

    x will be the product of the minimum number of necessary factors of numbers 1 to 20
    such that x is evenly divisble by an number from 1 to 20.
    """
    return 2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19


if __name__ == "__main__":
    print(solution())
