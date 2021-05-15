import math


def printFactor(factor):
    if factor[1] == 1:
        print(f"{factor[0]}", end="")
    else:
        print(f"{factor[0]}^{factor[1]}", end="")


if __name__ == '__main__':
    # verjamem da je to zelo (ce ne najbolj) ucinkovita resitev
    n = int(input())
    input_number = n
    potential_factors = list(range(2, math.floor(math.sqrt(n))))
    for i in range(len(potential_factors)):
        if potential_factors[i] != 0:
            for i2 in range(2 * i + 2, len(potential_factors), i + 2):
                potential_factors[i2] = 0

    potential_factors = [factor for factor in potential_factors if factor != 0]
    factors = []

    for factor in potential_factors:
        power = 0
        while n % factor == 0:
            power += 1
            n /= factor
        if power:
            factors.append((factor, power))

    if n != 1:
        factors.append((int(n), 1))

    print(f"{input_number} = ", end="")
    for factor in factors[:-1]:
        printFactor(factor)
        print("*", end="")
    printFactor(factors[-1])
