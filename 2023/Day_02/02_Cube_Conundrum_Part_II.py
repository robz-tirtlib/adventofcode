def solve_game(game_line: str) -> int:
    game_name, game_sets = game_line.split(":")
    maxs = {}
    res = 1

    for game_set in game_sets.split(";"):
        for color in game_set.strip().split(","):
            count, color_name = color.split()
            maxs[color_name] = max(maxs.get(color_name, 0), int(count))

    for _, count in maxs.items():
        res *= count

    return res


def solve() -> None:
    res = 0

    with open("input.txt") as f:
        for game_line in f.readlines():
            game_line = game_line.strip()
            res += solve_game(game_line)

    print(res)


if __name__ == "__main__":
    solve()
