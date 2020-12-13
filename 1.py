def part_1(nums):
    for num in nums:
        if 2020 - num in nums:
            return f'2020 = {num} + {2020 - num}\nProduct: {num * (2020 - num)}'


def part_2(nums):
    for num_1 in nums:
        for num_2 in nums:
            if num_1 == num_2: continue
            if (num_3 := 2020 - num_1 - num_2) in nums:
                return f'2020 = {num_1} + {num_2} + {num_3}\nProduct: {num_1 * num_2 * num_3}'


def main():
    with open('input_1.txt') as doc: nums = set(map(int, doc.readlines()))
    print(part_1(nums), '\n')
    print(part_2(nums))


main()
