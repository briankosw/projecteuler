NUM = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076904224219022671055626321111109370544217506941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077541002256983155200055935729725716362695618826704282524836008232575304207529634500"

def solution() -> int:
    """
    Use a sliding window of length equals to 13 in order to calculate maximum product,
    while avoiding zeros altogether by skipping the start of the window to after the
    zeros' positions
    """
    max_product = 0
    curr_product = 1
    i = 0
    for j in range(len(NUM)):
        if NUM[j] == "0":
            i = j + 1
            curr_product = 1
        else:
            curr_product *= int(NUM[j])
        if j - i == 12:
            max_product = max(max_product, curr_product)
            curr_product //= int(NUM[i])
            i += 1
    return max_product


if __name__ == "__main__":
    print(solution())
