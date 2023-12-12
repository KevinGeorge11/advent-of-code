def parse_input(filename):
    with open(filename, "r") as file:
        histories = []
        for line in file:
            sequence = [int(x) for x in line.split()]
            histories.append(sequence)

        return histories


def part_one(puzzle_input):
    histories = parse_input(puzzle_input)

    return sum([get_final_num(sequence) for sequence in histories])


def part_two(puzzle_input):
    histories = parse_input(puzzle_input)

    return sum([get_final_num((list(reversed(sequence)))) for sequence in histories])


def get_final_num(sequence):
    last_nums = []
    while set(sequence) != {0}:
        last_nums.append(sequence[-1])
        sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence) - 1)]

    return sum(last_nums)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
