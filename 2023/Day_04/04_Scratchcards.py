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

    return 0 if count == 0 else 2 ** (count - 1)


def solve():
    res = 0

    with open("input.txt") as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            res += solve_line(line)

    print(res)


if __name__ == "__main__":
    solve()
