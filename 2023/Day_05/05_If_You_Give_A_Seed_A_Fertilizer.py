def new_values(cur: list[int], rows: list[list[int]]) -> list[int]:
    mappings = {num: num for num in cur}

    for row in rows:
        dest, source, length = row

        for num in cur:
            if num >= source and num <= (source + length - 1):
                mappings[num] = dest + num - source

    return mappings.values()


def solve():
    cur = []

    with open("input.txt") as f:
        cur = list(map(int, f.readline().split(':')[1].strip().split()))
        f.readline()
        f.readline()
        rows = []
        for _, line in enumerate(f.readlines()):
            if line == "\n" or line[0].isalpha():
                cur = new_values(cur, rows)
                rows = []
                continue
            rows.append(list(map(int, line.split())))
    cur = new_values(cur, rows)

    print(min(cur))


if __name__ == "__main__":
    solve()
