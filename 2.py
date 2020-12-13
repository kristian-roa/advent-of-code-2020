import re


def part_1(passwords):
    valid_counter = 0
    for line in passwords:
        low, high, char, password = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
        if int(low) <= password.count(char) <= int(high): valid_counter += 1
    return valid_counter


def part_2(passwords):
    valid_counter = 0
    for line in passwords:
        first, second, char, password = re.match(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
        if (password[int(first)-1] == char) != (password[int(second)-1] == char): valid_counter += 1
    return valid_counter


def main():
    with open('input_2.txt') as doc: passwords = doc.read().splitlines()
    print('Valid passwords part 1:', part_1(passwords))
    print('Valid passwords part 2:', part_2(passwords))


main()
