COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def solution() -> int:
    """
    Use dynamic programming to generate all possible combinations that sum up to 200
    """
    counts = [0] * 201
    counts[0] = 1
    for coin in COINS:
        for i in range(coin, len(counts)):
            counts[i] += counts[i - coin]
    print(counts)
    return counts[-1]


if __name__ == "__main__":
    print(solution())
