import re
from functools import reduce
from itertools import chain


def part_1(rules, messages):
    counter = 0
    for message in messages:
        if message in rules['0']:
            counter += 1
    return counter


def main():
    with open('input_19.txt') as doc: rules, messages = [d.splitlines() for d in doc.read().split('\n\n')]

    for i, rule in enumerate(rules): rules[i] = re.sub('"', '', rule)
    rules = dict(((i := rule.split(':'))[0], [r.split() for r in i[1].split('|')]) for rule in rules)
    rules = fix_rules(rules)

    print(part_1(rules, messages))


def fix_rules(rules):
    new_rules = {}

    def tree(rule):
        if rule not in rules: return rule
        new_rules[rule] = list(chain.from_iterable(perm([tree(_and) for _and in _or]) for _or in rules[rule]))
        return new_rules[rule]

    for rule in rules:
        if rule not in new_rules: tree(rule)
    return new_rules


def perm(inp):
    def permutations(a, b): return [start + end for start in a for end in b]
    return inp[0] if len(inp) == 1 else reduce(permutations, inp)


main()
