def handle_corner(
        cur: str, cur_i: int, cur_j: int, cur_dir: list[int, int]
) -> tuple[list[int, int], int, int]:
    if cur == 'J':
        if cur_dir == [0, 1]:
            cur_dir = [-1, 0]
            cur_i, cur_j = cur_i - 1, cur_j
        else:
            cur_dir = [0, -1]
            cur_i, cur_j = cur_i, cur_j - 1
    elif cur == '7':
        if cur_dir == [-1, 0]:
            cur_dir = [0, -1]
            cur_i, cur_j = cur_i, cur_j - 1
        else:
            cur_dir = [1, 0]
            cur_i, cur_j = cur_i + 1, cur_j
    elif cur == 'F':
        if cur_dir == [-1, 0]:
            cur_dir = [0, 1]
            cur_i, cur_j = cur_i, cur_j + 1
        else:
            cur_dir = [1, 0]
            cur_i, cur_j = cur_i + 1, cur_j
    else:
        if cur_dir == [0, -1]:
            cur_dir = [-1, 0]
            cur_i, cur_j = cur_i - 1, cur_j
        else:
            cur_dir = [0, 1]
            cur_i, cur_j = cur_i, cur_j + 1
    return cur_dir, cur_i, cur_j


def solve():
    path_length = 0
    i, j = None, None
    a = []

    with open("input.txt") as f:
        for line in f.readlines():
            if 'S' in line:
                i, j = len(a), line.index('S')

            a.append(line.strip())

    cur_i, cur_j = i, j + 1
    cur_dir = [0, 1]  # [1, 0] - down
    path_length += 1

    while a[cur_i][cur_j] != 'S':
        cur = a[cur_i][cur_j]
        if cur in 'FJ7L':
            cur_dir, cur_i, cur_j = handle_corner(cur, cur_i, cur_j, cur_dir)
            path_length += 1
            continue

        while a[cur_i][cur_j] == '-' and cur_dir == [0, -1]:
            path_length += 1
            cur_j -= 1

        while a[cur_i][cur_j] == '-' and cur_dir == [0, 1]:
            path_length += 1
            cur_j += 1

        while a[cur_i][cur_j] == '|' and cur_dir == [-1, 0]:
            path_length += 1
            cur_i -= 1

        while a[cur_i][cur_j] == '|' and cur_dir == [1, 0]:
            path_length += 1
            cur_i += 1

    print(path_length // 2)


if __name__ == "__main__":
    solve()
