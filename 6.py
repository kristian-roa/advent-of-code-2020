from itertools import chain


def part_1(answers):
    return sum([count(answer, any) for answer in answers])


def part_2(answers):
    return sum([count(answer, all) for answer in answers])


def count(answer, func):
    return sum([func(letter in ans for ans in answer) for letter in set(chain(*answer))])


def main():
    with open('input_6.txt') as doc: answers = [ans.split('\n') for ans in doc.read().strip().split('\n\n')]
    print('Sum of questions any answered:', part_1(answers))
    print('Sum of questions all answered:', part_2(answers))


main()
