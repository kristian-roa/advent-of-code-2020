def part_1(jolts):
    jolt_rate = 0
    device = max(jolts) + 3

    differences = []
    for jolt in jolts + [device]:
        diff = jolt - jolt_rate
        jolt_rate = jolt

        if len(differences) <= diff - 1:
            for _ in range(diff - len(differences)): differences.append(0)
        differences[diff - 1] += 1

    return differences[0] * differences[2]


def part_2(jolts):
    device = max(jolts) + 3
    visited = {}

    def tree(jolts, parent=0):
        if device - parent <= 3: return 1
        if parent in visited: return visited[parent]

        ans = 0
        for i, jolt in enumerate(jolts):
            if jolt - parent > 3: break
            ans += tree(jolts[i+1:], jolt)

        visited[parent] = ans
        return ans

    return tree(jolts)


def main():
    with open('input_10.txt') as doc: jolts = [int(i) for i in doc]
    jolts.sort()
    print('1-jolt difference * 3-jolt difference:', part_1(jolts))
    print('Distinct arrangements:', part_2(jolts))


main()
