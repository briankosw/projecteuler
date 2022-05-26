from math import factorial

def solution() -> int:
    """
    Use dynamic programming to calculate total routes for each (i, j) efficiently
    """
    dp = [[0] * 21 for _ in range(21)]
    for i in range(1, 21):
        dp[0][i] = 1
        dp[i][0] = 1
    for i in range(1, 21):
        for j in range(1, 21):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]

def solution() -> int:
    """
    In order to reach the bottom right corner, you need to make 20 moves to the right and
    and 20 moves to the bottom in total, where the number of ways to order these moves
    determine the total number of routes to the bottom right corner. This can be
    expressed as the combination 40 choose 20
    """
    return factorial(40) // factorial(20) // factorial(20)


if __name__ == "__main__":
    print(solution())
