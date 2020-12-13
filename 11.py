import numpy as np
dirs = [(y, x) for y in range(-1, 2) for x in range(-1, 2) if not y == x == 0]


def part_1(seats):
    converged = False
    while not converged:
        occupy, free = [], []
        for idx, seat in np.ndenumerate(seats):
            if not (occupied := occupied_close_neighbours(idx, seats)) and seat == 'L': occupy.append(idx)
            elif occupied >= 4 and seat == '#': free.append(idx)

        converged = len(occupy) + len(free) == 0

        for o in occupy: seats[o] = '#'
        for f in free: seats[f] = 'L'

    return np.count_nonzero(seats == '#')


def part_2(seats):
    converged = False
    while not converged:
        occupy, free = [], []
        for idx, seat in np.ndenumerate(seats):
            if not (occupied := occupied_far_neighbours(idx, seats)) and seat == 'L': occupy.append(idx)
            elif occupied >= 5 and seat == '#': free.append(idx)

        converged = len(occupy) + len(free) == 0

        for o in occupy: seats[o] = '#'
        for f in free: seats[f] = 'L'

    return np.count_nonzero(seats == '#')


def occupied_close_neighbours(idx, seats):
    occupied = [(a, b) for y, x in dirs
                if 0 <= (a := idx[0]+y) < seats.shape[0] and 0 <= (b := idx[1]+x) < seats.shape[1]
                and seats[a, b] == '#']
    return len(occupied)


def occupied_far_neighbours(idx, seats):
    occupied = []
    for y, x in dirs:
        i = 1
        while 0 <= (a := idx[0]+i*y) < seats.shape[0] and 0 <= (b := idx[1]+i*x) < seats.shape[1]:
            i += 1
            if seats[a, b] == '.': continue
            if seats[a, b] == '#': occupied.append((a, b))
            break

    return len(occupied)


def main():
    seats = np.genfromtxt('input_11.txt', delimiter=1, dtype=np.str)
    print('Occupied seats:', part_1(seats.copy()))
    print('Occupied seats:', part_2(seats))


main()
