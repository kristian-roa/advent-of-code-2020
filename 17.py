import numpy as np
d = (-1, 0, 1)
dirs_3 = [(y, x, z) for y in d for x in d for z in d if not y == x == z == 0]
dirs_4 = [(y, x, z, w) for y in d for x in d for z in d for w in d if not y == x == z == w == 0]


def part_1(game):
    return simulate(game, dims=3)


def part_2(game):
    return simulate(np.expand_dims(game, axis=3), dims=4)


def simulate(game, dims):
    for _ in range(6):
        set_active, set_inactive = [], []

        game = expand(game, dims)

        for idx, val in np.ndenumerate(game):
            n = alive_neighbours(idx, game, dims)
            if val == '#':
                if n < 2 or n > 3: set_inactive.append(idx)
            else:
                if n == 3: set_active.append(idx)

        for idx in set_inactive: game[idx] = '.'
        for idx in set_active: game[idx] = '#'

    return np.count_nonzero(game == '#')


def expand(game, dims):
    if dims == 3:
        game = np.pad(game, pad_width=((1, 1), (1, 1), (0, 0)), mode='constant', constant_values='.')
        game = np.dstack((np.full((*game.shape[:-1], 1), '.'), game))
        game = np.dstack((game, np.full((*game.shape[:-1], 1), '.')))
    else:
        game = np.pad(game, pad_width=((1, 1), (1, 1), (0, 0), (0, 0)), mode='constant', constant_values='.')
        game = np.dstack((np.full((*game.shape[:-2], 1, game.shape[-1]), '.'), game))
        game = np.dstack((game, np.full((*game.shape[:-2], 1, game.shape[-1]), '.')))
        game = np.concatenate((np.full((*game.shape[:-1], 1), '.'), game), axis=3)
        game = np.concatenate((game, np.full((*game.shape[:-1], 1), '.')), axis=3)
    return game


def get_neighbours(idx, game, dims):
    if dims == 3:
        return [game[i] for i in ((y + idx[0], x + idx[1], z + idx[2]) for y, x, z in dirs_3)
                if all(v >= 0 for v in i) and all(v < game.shape[j] for j, v in enumerate(i))]

    return [game[i] for i in ((y + idx[0], x + idx[1], z + idx[2], w + idx[3]) for y, x, z, w in dirs_4)
            if all(v >= 0 for v in i) and all(v < game.shape[j] for j, v in enumerate(i))]


def alive_neighbours(idx, game, dims):
    return get_neighbours(idx, game, dims).count('#')


def main():
    game = np.expand_dims(np.genfromtxt('input_17.txt', delimiter=1, dtype=np.str, comments='!'), axis=2)
    print('Active cubes:', part_1(game))
    print('Active hypercubes:', part_2(game))


main()
