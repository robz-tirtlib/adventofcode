def calc_diffs_lists(lst: list[int]) -> list[list[int]]:
    lists = [lst]

    while True:
        diffs = []
        all_zero = True

        for i in range(1, len(lists[-1])):
            diff = lists[-1][i] - lists[-1][i - 1]

            if diff != 0:
                all_zero = False

            diffs.append(diff)

        if all_zero:
            break

        lists.append(diffs)

    return lists


def solve_line(lst: list[int]) -> int:
    lists = calc_diffs_lists(lst)

    cur_add = 0

    for i in range(len(lists) - 1, -1, -1):
        cur_add += lists[i][-1]

    return cur_add


def solve_line2(lst: list[int]) -> int:
    lists = calc_diffs_lists(lst)

    cur_add = 0

    for i in range(len(lists) - 1, -1, -1):
        cur_add = lists[i][0] - cur_add

    return cur_add


def solve(solver):
    res = 0

    with open("input.txt") as f:
        for line in f.readlines():
            lst = [int(num) for num in line.strip().split()]
            res += solver(lst)

    print(res)


if __name__ == "__main__":
    solve(solve_line)  # Part 1
    solve(solve_line2)  # Part 2
