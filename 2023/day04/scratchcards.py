import math


def parse_input(filename):
    with open(filename, "r") as file:
        card_points = []
        card_matches = []
        for line in file:
            data = ' '.join(line.split())
            card_data, winning_numbers_data, my_numbers_data = data.replace("|", ":").split(":")
            winning_numbers = winning_numbers_data.split(" ")[1:]
            my_numbers = my_numbers_data.split(" ")[1:]

            winning_numbers_set = set(winning_numbers)
            my_numbers_set = set(my_numbers)
            common_numbers = winning_numbers_set & my_numbers_set
            card_matches.append(len(common_numbers))

            points = pow(2, len(common_numbers) - 1) if len(common_numbers) > 0 else 0
            card_points.append(points)

    return card_points


def part_one(puzzle_input):
    card_points = parse_input(puzzle_input)

    return sum(card_points)


def part_two(puzzle_input):
    card_points = parse_input(puzzle_input)
    card_matches = [int(math.log2(card)) + 1 if card != 0 else 0 for card in card_points]
    num_cards = [1 for _ in card_points]

    for i, matches in enumerate(card_matches):
        for _ in range(num_cards[i]):
            for k in range(matches):
                num_cards[i + 1 + k] += 1

    return sum(num_cards)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
