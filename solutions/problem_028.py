def solution() -> int:
    """
    Calculate the numbers in the diagonals and sum them up
    """
    diagonal_sum = 1
    curr_num = 1
    d = 2
    for _ in range(500):
        for _ in range(4):
            curr_num += d
            diagonal_sum += curr_num
        d += 2
    return diagonal_sum


if __name__ == "__main__":
    print(solution())
