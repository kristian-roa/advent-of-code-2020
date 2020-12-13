from math import ceil


def part_1(T_ready, buses):
    T_buses = [(bus, ceil(T_ready / bus)*bus) for bus in buses]
    ID, T_bus = min(T_buses, key=lambda key: key[1])
    return (T_bus - T_ready) * ID


def part_2(buses):
    time, step = 0, 1
    for bus, offset in sorted(buses.items(), reverse=True):
        while (time + offset) % bus: time += step
        step *= bus
    return time


def main():
    with open('input_13.txt') as doc:
        T_ready = int(doc.readline())
        buses = dict([(int(i), idx) for idx, i in enumerate(doc.readline().split(',')) if i != 'x'])

    print('Time difference * ID:', part_1(T_ready, buses))
    print('Earliest timestamp:', part_2(buses))


main()
