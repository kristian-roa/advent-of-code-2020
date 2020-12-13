import re


def part_1(rules):
    rule_reversed = {}

    for key, val in rules.items():
        for v in val:
            if v[1] in rule_reversed: rule_reversed[v[1]].append(key)
            else: rule_reversed[v[1]] = [key]

    visited = set()

    def count_outside(current):
        if current not in rule_reversed: return 0

        count = 0
        for bag in rule_reversed[current]:
            if bag not in visited:
                visited.add(bag)
                count += 1 + count_outside(bag)

        return count

    return count_outside('shiny gold')


def part_2(rules):
    def count_inside(current):
        if not rules[current]: return 0

        count = 0
        for amount, bag in rules[current]:
            count += int(amount) + int(amount) * count_inside(bag)

        return count

    return count_inside('shiny gold')


def main():
    with open('input_7.txt') as doc: rules = doc.read().splitlines()
    bags = [re.findall(r'([\w\s]+) bags contain', rule)[0] for rule in rules]
    contains = [re.findall(r'(\d) ([\w\s]+) bag', rule) for rule in rules]
    rules = dict(zip(bags, contains))

    print('Bags that can contain a shiny gold bag:', part_1(rules))
    print('Bags required inside my shiny gold bag:', part_2(rules))


main()
