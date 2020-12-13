import re


def part_1(code):
    already_done = set()
    idx = accumulator = 0

    while idx not in already_done:
        already_done.add(idx)
        instr, val = code[idx]

        if instr == 'acc': accumulator += val
        elif instr == 'jmp': idx += val; continue

        idx += 1
    return accumulator


def part_2(code):
    change = [(i, code[i][0]) for i in range(len(code)) if code[i][0] in ('nop', 'jmp')]

    for c_idx, c_instr in change:
        code_cp = code.copy(); code_cp[c_idx] = ('jmp' if c_instr == 'nop' else 'nop', code_cp[c_idx][1])

        already_done = set()
        idx = accumulator = 0
        while idx < len(code_cp):
            if idx in already_done: break
            already_done.add(idx)
            instr, val = code_cp[idx]

            if instr == 'acc': accumulator += val
            elif instr == 'jmp': idx += val; continue

            idx += 1

        else: return accumulator


def main():
    with open('input_8.txt') as doc: code = doc.read().splitlines()
    code = [((a := re.match(r'(\w+) ([+-]\d+)', c).groups())[0], int(a[1])) for c in code]
    print('Acculumator:', part_1(code))
    print('Accumulator:', part_2(code))


main()
