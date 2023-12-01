def find_names(s: str, inds: list[int, int]) -> int:
    name_to_val = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for name, val in name_to_val.items():
        first = s.find(name)

        if first != -1:
            inds.append((first, val))

        last = s[::-1].find(name[::-1])

        if last != -1:
            last = len(s) - (last + len(name))
            inds.append((last, val))


def find_nums(s: str, inds: list[int, int]) -> int:
    for i in range(len(s)):
        if s[i].isdigit():
            inds.append((i, int(s[i])))
            break

    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            inds.append((i, int(s[i])))
            break


def solve(s: str, inds: list[int, int]) -> int:
    find_names(s, inds)
    find_nums(s, inds)
    inds.sort()
    return inds[0][1] * 10 + inds[-1][1]


res = 0


with open("input.txt") as f:
    for s in f.readlines():
        inds = []
        s = s.strip()
        res += solve(s, inds)


print(res)
