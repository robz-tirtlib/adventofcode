def is_smaller_or_equal(
        max_counts: dict[str, int], set_counts: dict[str, int]
) -> bool:
    for name, count in max_counts.items():
        if set_counts.get(name, 0) > count:
            return False

    for name, count in set_counts.items():
        if name not in max_counts:
            return False

    return True


def solve_game(game_line: str) -> int:
    game_name, game_sets = game_line.split(":")
    game_id = int(game_name.split()[1])
    ok = True

    for game_set in game_sets.split(";"):
        set_counts = {}
        for color in game_set.strip().split(","):
            count, color_name = color.split()
            set_counts[color_name] = int(count) + set_counts.get(color_name, 0)
        if not is_smaller_or_equal(max_counts, set_counts):
            ok = False

    return game_id if ok else 0


def solve(max_counts: dict[str, int]) -> None:
    res = 0

    with open("input.txt") as f:
        for game_line in f.readlines():
            game_line = game_line.strip()
            res += solve_game(game_line)

    print(res)


if __name__ == "__main__":
    max_counts = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    solve(max_counts)
