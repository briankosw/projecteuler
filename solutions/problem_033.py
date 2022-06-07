from typing import List


def solution() -> List[str]:
    curious_fractions = []
    for i in range(11, 100):
        for j in range(10, i):
            if str(j)[1] != str(i)[0] or str(i)[1] == "0":
                continue
            fun_div = int(str(j)[0]) / int(str(i)[1])
            if j / i == fun_div:
                curious_fractions.append(f"{j} / {i}")
    return curious_fractions

if __name__ == "__main__":
    print(solution())
