def gcd(a: int, b: int) -> int:
    if a == 0:
        return b

    if b == 0:
        return a

    if a >= b:
        return gcd(b, a % b)
    return gcd(a, b % a)


def lcm(a: int, b: int) -> int:
    return a * b / gcd(a, b)


def find_z(path: str, nodes: dict, node: str) -> int:
    res = 0

    while True:
        for dir in path:
            node = nodes[node][1] if dir == 'R' else nodes[node][0]
            res += 1
            if node[-1] == 'Z':
                return res


def solve():
    path, nodes = None, None
    cur_nodes = []
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
            if node[-1] == 'A':
                cur_nodes.append(node)

    zs = []

    for node in cur_nodes:
        z = find_z(path, nodes, node)
        zs.append(z)

    res = zs[0]

    for loop in zs:
        res = lcm(res, loop)

    print(res)


if __name__ == "__main__":
    solve()
