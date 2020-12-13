import re


def part_1(passwords):
    valid_counter = 0

    for password in passwords:
        p = password.split()
        if len(p) == 8 or (len(p) == 7 and 'cid:' not in password): valid_counter += 1

    return valid_counter


def part_2(passwords):
    years = {'byr': (1920, 2002+1), 'iyr': (2010, 2020+1), 'eyr': (2020, 2030+1)}
    patterns = {'hcl': r'^#[\da-f]{6}$', 'pid': r'^\d{9}$'}
    eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    heights = {'cm': (150, 193+1), 'in': (59, 76+1)}
    valid_counter = 0

    for password in passwords:
        info = dict(re.findall(r'([\d\w]+):([\d\w#]+)', password))
        if len(info) < 7 or (len(info) == 7 and 'cid' in info): continue

        for i, val in info.items():
            if i in ['byr', 'iyr', 'eyr'] and not (len(val) == 4 and int(val) in range(*years[i])): break
            elif i in ['hcl', 'pid'] and not re.findall(patterns[i], val): break
            elif i == 'ecl' and val not in eye_color: break
            elif i == 'hgt':
                num, code = re.match(r'(\d+)(\w+)', val).groups()
                if not (code in heights and int(num) in range(*heights[code])): break
        else:
            valid_counter += 1

    return valid_counter


def main():
    with open('input_4.txt') as doc: passwords = doc.read().split('\n\n')
    print('Valid passwords part 1:', part_1(passwords))
    print('Valid passwords part 2:', part_2(passwords))


main()
