def part_1(nums):
    for i, n in enumerate(nums[25:]):
        preamble = nums[i:i+25]; preamble.sort()

        low, high = 0, 24
        while low < high:
            if (s := preamble[low] + preamble[high]) == n: break
            if s > n: high -= 1
            elif s < n: low += 1
        else: return n


def part_2(nums):
    invalid = part_1(nums)

    low, high = 0, 1; s = nums[low] + nums[high]
    while low < high < len(nums):
        if s == invalid: return min(r := nums[low:high+1]) + max(r)
        if s > invalid: s -= nums[low]; low += 1
        elif s < invalid: high += 1; s += nums[high]


def main():
    with open('input_9.txt') as doc: nums = [int(i) for i in doc]
    print('Lowest number thats not a sum:', part_1(nums))
    print('Sum of the lowest and highest:', part_2(nums))


main()
