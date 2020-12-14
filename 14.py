import re
import numpy as np


def part_1(masks):
    memory = {}
    for mask, values in masks.items():
        for idx, dec in values:
            value = '0' * (36 - len((b := bin(dec)[2:]))) + b
            result = ''.join([v if m == 'X' else m for v, m in zip(value, mask)])

            memory[idx] = int(result, 2)

    return sum(memory.values())


def part_2(masks):
    memory = {}
    for mask, values in masks.items():
        for idx, dec in values:
            value = '0' * (36 - len((b := bin(idx)[2:]))) + b
            result = ''.join([v if m == '0' else m if m == '1' else 'X' for v, m in zip(value, mask)])

            for i in np.ndindex(*[2]*result.count('X')):
                r = result
                for v in i: r = re.sub('X', str(v), r, count=1)
                memory[int(r, 2)] = dec

    return sum(memory.values())


def main():
    masks = {}
    with open('input_14.txt') as doc:
        for line in doc:
            if m := re.match(r'mask = (\w+)', line):
                mask = m.group(1)
                masks[mask] = []
            else:
                masks[mask].append((int((i := re.match(r'mem\[(\d+)] = (\d+)', line).groups())[0]), int(i[1])))

    print('Sum of values left in memory:', part_1(masks))
    print('Sum of values left in memory:', part_2(masks))


main()
