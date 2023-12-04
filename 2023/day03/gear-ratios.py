def find_full_number_in_string(position, string, found_at_y):
    start = position
    end = position

    while start > 0 and string[start - 1].isdigit():
        start -= 1
    while end < len(string) and string[end].isdigit():
        end += 1

    return int(string[start: end]), start


def parse_input(filename):
    with open(filename, "r") as file:
        engine = file.read().splitlines()
        part_numbers = []
        gears = []
        num_position_found_dict = {}

        for i, line in enumerate(engine):
            for j, char in enumerate(line):

                # found symbol
                if not char.isdigit() and char != '.':

                    # check neighbours
                    neighbour_lst = []
                    for y in [-1, 0, 1]:
                        for x in [-1, 0, 1]:
                            neighbour = engine[i + y][j + x]

                            # found digit of part number
                            if neighbour.isdigit():
                                neighbour_pos = j + x
                                start_y = i + y
                                line_found_from = engine[start_y]

                                number, start_x = find_full_number_in_string(neighbour_pos, line_found_from, start_y)

                                # check if part number was already found
                                if f'({start_x}, {start_y})' not in num_position_found_dict:
                                    num_position_found_dict[f'({start_x}, {start_y})'] = number
                                    part_numbers.append(number)
                                    neighbour_lst.append(number)

                    # found gear and calculates its ratio
                    if char == "*" and len(neighbour_lst) == 2:
                        gear_ratio = neighbour_lst[0] * neighbour_lst[1]
                        gears.append(gear_ratio)

        return part_numbers, gears


def part_one(puzzle_input):
    all_part_numbers, all_gear_ratios = parse_input(puzzle_input)
    return sum(all_part_numbers)


def part_two(puzzle_input):
    all_part_numbers, all_gear_ratios = parse_input(puzzle_input)
    return sum(all_gear_ratios)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
