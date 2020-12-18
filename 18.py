import re
from anytree import Node
from math import prod


def part_1(exp_trees):
    return sum(eval_tree(exp_tree) for exp_tree in exp_trees)


def part_2(exp_trees):
    return sum(eval_tree(exp_tree, advanced=True) for exp_tree in exp_trees)


def build_tree(exp_tree):
    exp_tree = re.sub(r'\)', ' )', re.sub(r'\(', '( ', exp_tree)).split()

    tree = Node(None); parents = [tree]
    for i in exp_tree:
        if i == '(': parents.append(Node(None, parent=parents[-1]))
        elif i == ')': parents.pop()
        else: Node(i, parent=parents[-1])

    return tree


def eval_node(node):
    node.value = int(node.children[0].value); opr = None
    for child in node.children[1:]:
        if type(child.value) is int or child.value.isdigit():
            if opr == '+': node.value += int(child.value)
            else: node.value *= int(child.value)
        else: opr = child.value


def eval_node_advanced(node):
    node.value = int(node.children[0].value)
    vals = [child.value for child in node.children]

    while '+' in vals:
        for i, val in enumerate(vals):
            if val == '+':
                vals[i-1] = int(vals[i-1]) + int(vals[i+1])
                vals.pop(i+1)
                vals.pop(i)
                break

    node.value = prod(int(v) for v in vals[::2])


def eval_tree(exp_tree, advanced=False):
    tree = build_tree(exp_tree)

    # traverse the tree and calculate value of nodes
    def traverse(node):
        if node.is_leaf: node.value = node.name; return
        for child in node.children: traverse(child)

        if advanced: eval_node_advanced(node)
        else: eval_node(node)

    traverse(tree)
    return tree.value


def main():
    with open('input_18.txt') as doc: exp_trees = doc.read().splitlines()
    print('Sum of evaluated trees:', part_1(exp_trees))
    print('Sum of evaluated trees:', part_2(exp_trees))


main()
