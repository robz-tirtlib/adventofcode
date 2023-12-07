from collections import Counter


CARDS = "AKQT98765432J"[::-1]
CARDS_STRENGTHS = {card: val for val, card in zip(range(len(CARDS)), CARDS)}


def compare_strengths(hand1: str, hand2: str) -> int:
    """
    1 - hand1 >= hand2
    0 - hand2 > hand1
    """

    for card1, card2 in zip(hand1, hand2):
        if CARDS_STRENGTHS[card1] > CARDS_STRENGTHS[card2]:
            return 1
        if CARDS_STRENGTHS[card1] < CARDS_STRENGTHS[card2]:
            return 0

    return 1


def get_hand_score(hand: str) -> int:
    def _get_hand_score(hand: str) -> int:
        hand = ''.join(sorted(list(hand)))
        counts = Counter(hand)

        if 5 in counts.values():
            return 6
        elif 4 in counts.values():
            return 5
        elif 3 in counts.values() and 2 in counts.values():
            return 4
        elif 3 in counts.values():
            return 3

        pairs = 0
        highest_card = hand[0]

        for char, count in counts.items():
            if count == 2:
                pairs += 1

            if CARDS_STRENGTHS[char] > CARDS_STRENGTHS[highest_card]:
                highest_card = char

        if pairs == 2:
            return 2
        elif pairs == 1:
            return 1
        return 0

    if 'J' not in hand:
        return _get_hand_score(hand)

    max_score = 0
    alpha = set(hand)

    for char in alpha:
        new_hand = hand.replace('J', char)
        max_score = max(max_score, _get_hand_score(new_hand))

    return max_score


def compare_hands(hand1: str, hand2: str) -> int:
    """
    1 - hand1 >= hand2
    0 - hand2 > hand1
    """

    score1 = get_hand_score(hand1)
    score2 = get_hand_score(hand2)

    if score1 > score2:
        return 1
    elif score1 == score2:
        return compare_strengths(hand1, hand2)
    return 0


def get_hands_ratings(hands: list[str]) -> list[tuple[str, int]]:
    ratings = {}

    for hand1 in hands:
        for hand2 in hands:
            score = compare_hands(hand1, hand2)
            ratings[hand1] = ratings.get(hand1, 0) + score

    return ratings.items()


def solve():
    hands_bids = {}
    with open("input.txt") as f:
        for line in f.readlines():
            hand, bid = line.split()
            hands_bids[hand] = int(bid)

    ratings = [(c, r) for c, r in get_hands_ratings(hands_bids.keys())]
    ratings.sort(key=lambda x: x[1])

    res = 0

    for i, pair in enumerate(ratings):
        hand, _ = pair
        res += (i + 1) * hands_bids[hand]
        if i > 0:
            assert compare_hands(ratings[i - 1][0], hand) == 0
    print(res)


if __name__ == "__main__":
    solve()
