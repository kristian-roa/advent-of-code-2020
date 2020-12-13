def part_1(codes):
    return max([get_seat_id(code) for code in codes])


def part_2(codes):
    ids = [get_seat_id(code) for code in codes]
    return sum(range(min(ids), max(ids)+1)) - sum(ids)  # sum of all seat IDs - sum of all IDs in the list


def get_seat_id(code):
    row, col = range(128), range(8)

    for c in code[:7]: row = row[:len(row) // 2] if c == 'F' else row[len(row) // 2:]
    for c in code[7:]: col = col[:len(col) // 2] if c == 'L' else col[len(col) // 2:]

    return row[0] * 8 + col[0]  # seat ID


def main():
    with open('input_5.txt') as doc: codes = doc.read().splitlines()
    print('Highest seat id:', part_1(codes))
    print('My seats id:', part_2(codes))


main()
