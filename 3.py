import numpy as np


def part_1(tree_map):
    tree_counter = 0

    for y, x in get_index(tree_map.shape, right=3, down=1):
        if tree_map[y, x] == '#': tree_counter += 1

    return tree_counter


def part_2(tree_map):
    trees = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        tree_counter = 0
        for y, x in get_index(tree_map.shape, *slope):
            if tree_map[y, x] == '#': tree_counter += 1
        trees.append(tree_counter)

    return np.product(trees)


def get_index(shape, right, down):
    x = 0
    for y in range(0, shape[0], down):
        yield y, x
        x += right
        if x >= shape[1]: x -= shape[1]


def main():
    with open('input_3.txt') as doc: tree_map = np.genfromtxt(doc, dtype=np.str, comments=None, delimiter=1)
    print('Trees in the path:', part_1(tree_map))
    print('Product of trees in the path:', part_2(tree_map))


main()
