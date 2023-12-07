from collections import defaultdict


def parse_input(filename):
    with open(filename, "r") as file:
        player_list = []
        for line in file:
            poker_data, bid_data = line.split(" ")
            poker_hand = [c for c in poker_data]
            bid = int(bid_data[:-1])
            player_list.append((poker_hand, bid))

        # print(player_list)
        return player_list


def part_one(puzzle_input):
    player_list = parse_input(puzzle_input)
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    sorted_player_hands = get_sorted_hands_list(player_list, card_values, include_jokers=False)

    # player[1] is the bid value, index + 1 is the rank value,
    # so winnings for player = bid * rank =  player[1] * (index + 1)
    total_winnings = sum([player[1]*(index + 1) for index, player in enumerate(sorted_player_hands)])

    return total_winnings


def part_two(puzzle_input):
    player_list = parse_input(puzzle_input)
    card_values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    sorted_player_hands = get_sorted_hands_list(player_list, card_values, include_jokers=True)

    # player[1] is the bid value, index + 1 is the rank value,
    # so winnings for player = bid * rank =  player[1] * (index + 1)
    total_winnings = sum([player[1] * (index + 1) for index, player in enumerate(sorted_player_hands)])

    return total_winnings


def get_sorted_hands_list(player_list, card_values, include_jokers):
    # p[0] is the player hand, so p[0][0] is card 1, p[0][0] is card 2...p[0][4] is card 5
    sorted_hands = sorted(player_list, key=lambda p: (check_hand(p, include_jokers), card_values[p[0][0]], card_values[p[0][1]],
                                                      card_values[p[0][2]], card_values[p[0][3]], card_values[p[0][4]]))
    return sorted_hands


def check_hand(player, include_jokers):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

    hand, bid = player
    jokers = hand.count('J') if include_jokers else 0

    if check_five_of_a_kind(hand):
        # if there are jokers, all cards must be jokers to be five of a kind, doesn't matter if there are jokers or not
        return FIVE_OF_A_KIND

    if check_four_of_a_kind(hand):
        # 2 or 3 jokers means it's not a four of a kind, so skip those cases
        if jokers == 1 or jokers == 4:
            return FIVE_OF_A_KIND
        else:
            return FOUR_OF_A_KIND

    if check_full_house(hand):
        # 1 or 4 jokers means it's not a full_house, so skip those cases
        if jokers == 2 or jokers == 3:
            return FIVE_OF_A_KIND
        else:
            return FULL_HOUSE

    if check_three_of_a_kind(hand):
        # 4 jokers means it's a four of a kind, already handled that case above
        if jokers == 1 or jokers == 3:
            return FOUR_OF_A_KIND
        elif jokers == 2:
            return FIVE_OF_A_KIND
        else:
            return THREE_OF_A_KIND

    if check_two_pairs(hand):
        # 3 or 4 jokers means it's a three of a kind or four of a kind, already handled that case above
        if jokers == 1:
            return FULL_HOUSE
        elif jokers == 2:
            return FOUR_OF_A_KIND
        else:
            return TWO_PAIRS

    if check_one_pair(hand):
        # 3 or 4 jokers means it's a three of a kind or four of a kind, already handled that case above
        if jokers == 1 or jokers == 2:
            return THREE_OF_A_KIND
        else:
            return ONE_PAIR

    # hand type must be high card if it reaches here,
    # more than one joker means it is a different hand type, which is handled above
    if jokers == 1:
        return ONE_PAIR
    else:
        return HIGH_CARD


def check_five_of_a_kind(hand):
    return len(set(hand)) == 1


def check_four_of_a_kind(hand):
    card_counts = defaultdict(lambda: 0)
    for card in hand:
        card_counts[card] += 1

    return set(card_counts.values()) == {1, 4}


def check_full_house(hand):
    card_counts = defaultdict(lambda: 0)
    for card in hand:
        card_counts[card] += 1

    return set(card_counts.values()) == {2, 3}


def check_three_of_a_kind(hand):
    card_counts = defaultdict(lambda: 0)
    for card in hand:
        card_counts[card] += 1

    return sorted(card_counts.values()) == [1, 1, 3]


def check_two_pairs(hand):
    card_counts = defaultdict(lambda: 0)
    for card in hand:
        card_counts[card] += 1

    return sorted(card_counts.values()) == [1, 2, 2]


def check_one_pair(hand):
    card_counts = defaultdict(lambda: 0)
    for card in hand:
        card_counts[card] += 1

    return 2 in card_counts.values()


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
