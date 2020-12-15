def part_1(numbers):
    return game(numbers, 2020)


def part_2(numbers):
    return game(numbers, 30000000)


def game(numbers, n):
    spoken = {}

    for i, num in enumerate(numbers[:-1]): spoken[num] = i
    num = numbers[-1]

    for i in range(len(numbers)-1, n-1):
        if num in spoken:
            recent = spoken[num]
            spoken[num] = i
            num = v if (v := spoken[num] - recent) != 0 else 1
        else:
            spoken[num] = i
            num = 0

    return num


def main():
    numbers = [20, 9, 11, 0, 1, 2]
    print('2020th number:', part_1(numbers))
    print('30 000 000th number:', part_2(numbers))


main()
