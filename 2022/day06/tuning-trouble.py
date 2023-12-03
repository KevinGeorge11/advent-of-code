def parse_input(filename):
    datastream = ""
    with open(filename, "r") as file:
        for line in file:
            datastream += str(line)
    return datastream


def unique_chars_set(s):
    return len(s) == len(set(s))


def part_one(puzzle_input):
    data = parse_input(puzzle_input)
    for i in range(len(data)):
        if unique_chars_set(data[i:i+4]):
            return i + 4


def part_two(puzzle_input):
    data = parse_input(puzzle_input)
    for i in range(len(data)):
        if unique_chars_set(data[i:i+14]):
            return i + 14


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
