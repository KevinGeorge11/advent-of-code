def find_full_number_in_string(position, string):
    start = position
    end = position

    while start > 0 and string[start - 1].isdigit():
        start -= 1

    while end < len(string) and string[end].isdigit():
        end += 1

    return int(string[start: end])


def parse_input(filename):
    with open(filename, "r") as file:
        engine = file.read().splitlines()
        part_numbers = set()

        for i, line in enumerate(engine):
            for j, char in enumerate(line):
                # found symbol
                if not char.isdigit() and char != ".":
                    # check neighbours
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            neighbour = engine[i + y][j + x]
                            # found digit of part number
                            if neighbour.isdigit():
                                neighbour_pos = j + x
                                line_found_from = engine[i + y]

                                number = find_full_number_in_string(neighbour_pos, line_found_from)
                                part_numbers.add(number)

        return part_numbers


def part_one(puzzle_input):
    all_part_numbers = parse_input(puzzle_input)
    return sum(all_part_numbers)


def part_two(puzzle_input):
    return


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
