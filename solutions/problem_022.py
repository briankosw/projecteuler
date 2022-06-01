from functools import lru_cache


@lru_cache
def get_char_num(char: str) -> int:
    return ord(char) - ord("A") + 1


def solution() -> int:
    names = []
    with open("p022_names.txt", "r") as f:
        file_str = f.read()
        names = file_str.split(",")
    for i in range(len(names)):
        names[i] = names[i].strip('"')
    names = sorted(names)
    total_score = 0
    for i in range(len(names)):
        name_score = 0
        for c in names[i]:
            name_score += get_char_num(c)
        total_score += name_score * (i + 1)
    return total_score


if __name__ == "__main__":
    print(solution())
