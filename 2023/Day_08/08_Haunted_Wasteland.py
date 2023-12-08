def solve():
    path, nodes = None, None
    with open("input.txt") as f:
        path = f.readline().strip()
        nodes = {}
        f.readline()

        for line in f.readlines():
            line = line.replace(' ', '')
            node, lr = line.strip().split('=')
            lr = lr.replace('(', '').replace(')', '')
            l, r = lr.split(',')

            nodes[node] = (l, r)
    node = "AAA"
    steps = 0

    while node != "ZZZ":
        steps += 1

        for dir in path:
            if dir == 'R':
                node = nodes[node][1]
            else:
                node = nodes[node][0]
    print(steps * len(path))


if __name__ == "__main__":
    solve()
