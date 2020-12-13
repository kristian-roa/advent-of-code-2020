import numpy as np
import re
compass = dict(zip(('N', 'S', 'E', 'W'), [np.array(v).reshape(2, 1) for v in ((1, 0), (-1, 0), (0, 1), (0, -1))]))


def part_1(instructions):
    left = dict(zip((a := ('N', 'W', 'S', 'E')), a[1:] + a[:-1]))
    right = dict(zip((a := ('N', 'E', 'S', 'W')), a[1:] + a[:-1]))

    pos = np.array((0, 0)).reshape(2, 1); direction = 'E'

    for i, val in instructions:
        val = int(val)
        if i in ('N', 'S', 'E', 'W'): pos += compass[i] * val
        elif i in ('L', 'R'):
            for _ in range(val // 90): direction = left[direction] if i == 'L' else right[direction]
        else: pos += compass[direction] * val

    return np.sum(np.abs(pos))


def part_2(instructions):
    rot_left = np.array([[0, 1], [-1, 0]])
    rot_right = np.array([[0, -1], [1, 0]])

    pos = np.array((0, 0)).reshape(2, 1)
    waypoint = np.array((1, 10)).reshape(2, 1)

    for i, val in instructions:
        val = int(val)
        if i in ('N', 'S', 'E', 'W'): waypoint += compass[i] * val
        elif i in ('L', 'R'):
            for _ in range(val // 90): waypoint = rot_left @ waypoint if i == 'L' else rot_right @ waypoint
        else: pos += waypoint * val

    return np.sum(np.abs(pos))


def main():
    with open('input_12.txt') as doc: instructions = [re.search(r'(\w)(\d+)', instr).groups() for instr in doc]
    print('Manhattan distance:', part_1(instructions))
    print('Manhattan distance:', part_2(instructions))


main()
