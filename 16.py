import re
from itertools import chain


def part_1(info, nearby_tickets):
    scanning_error = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(l1 <= value <= l2 or h1 <= value <= h2 for (l1, l2), (h1, h2) in info.values()):
                scanning_error += value
                break

    return scanning_error


def part_2(info, my_ticket, nearby_tickets):
    possible_tickets = nearby_tickets.copy()
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(l1 <= value <= l2 or h1 <= value <= h2 for (l1, l2), (h1, h2) in info.values()):
                possible_tickets.remove(ticket)
                break

    possibilities = [[] for _ in info.keys()]
    for i, val in enumerate(possibilities):
        for field, ((l1, l2), (h1, h2)) in info.items():
            if all(l1 <= ticket[i] <= l2 or h1 <= ticket[i] <= h2 for ticket in possible_tickets): val.append(field)

    while not all(len(p) == 1 for p in possibilities):
        for i, p in enumerate(possibilities):
            if len(p) == 1:
                val = p[0]
                for f in possibilities[:i]:
                    if val in f: f.remove(val)
                for f in possibilities[i+1:]:
                    if val in f: f.remove(val)

    arrangement = list(chain.from_iterable(possibilities))

    prod = 1
    for i, arr in enumerate(arrangement):
        if arr.startswith('departure'): prod *= my_ticket[i]

    return prod


def main():
    with open('input_16.txt') as doc: inp = doc.read()

    info = re.findall(r'^([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)$', inp, re.M)
    info = dict(zip((i[0] for i in info), [((limit := [int(ii) for ii in i[1:]])[:2], limit[2:]) for i in info]))

    tickets = [[int(i) for i in ticket.split(',')] for ticket in re.findall(r'(^[\d,]+$)', inp, re.M)]
    my_ticket, nearby_tickets = tickets[0], tickets[1:]

    print('Scanning error rate:', part_1(info, nearby_tickets))
    print('Product of departure info:', part_2(info, my_ticket, nearby_tickets))


main()
