def count_race(best_time: int, dist: int) -> int:
    res = 0

    for speed in range(best_time + 1):
        travel_time = best_time - speed
        if speed * travel_time > dist:
            res += 1

    return res


def solve():
    res = 1
    with open("input.txt") as f:
        time = list(map(int, f.readline().split(':')[1].strip().split()))
        dist = list(map(int, f.readline().split(':')[1].strip().split()))
        races = [(t, d) for t, d in zip(time, dist)]

        for t, d in races:
            res *= count_race(t, d)

    print(res)


def solve2():
    res = 1
    with open("input.txt") as f:
        time = int(f.readline().split(':')[1].strip().replace(' ', ''))
        dist = int(f.readline().split(':')[1].strip().replace(' ', ''))

        res *= count_race(time, dist)

    print(res)


if __name__ == "__main__":
    # solve()
    solve2()
