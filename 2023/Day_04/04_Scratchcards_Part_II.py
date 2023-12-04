from collections import Counter


def parse_line(line: str) -> tuple[list[int], list[int]]:
    _, cards = line.split(':')
    numbers, winning = cards.split('|')
    numbers = [int(num) for num in numbers.split()]
    winning = [int(num) for num in winning.split()]
    return numbers, winning


def solve_line(line: str) -> int:
    numbers, winning = parse_line(line)
    numbers_count = Counter(numbers)
    count = 0

    for num in winning:
        count += numbers_count.get(num, 0)

    return count


def count_line(i: int, line_ans: int, cnt: dict[int, int]) -> int:
    for di in range(1, line_ans + 1):
        cnt[i + di] = cnt.get(i + di, 1) + cnt.get(i, 1)

    return cnt.get(i, 1)


def solve():
    res = 0
    cnt = {0: 1}

    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            line_ans = solve_line(line)
            res += count_line(i, line_ans, cnt)
    print(res)


if __name__ == "__main__":
    solve()
