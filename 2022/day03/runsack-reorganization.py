def calculate_total_priorities(error_chars):
    lower_ascii = 96
    upper_ascii = 38

    return sum([ord(c) - upper_ascii if c.isupper() else ord(c) - lower_ascii for c in error_chars])


def part_one(puzzle_input):
    error_chars = []

    with open(puzzle_input, "r") as file:
        for line in file:
            items_len = len(line) // 2
            first_half = line[:items_len]
            second_half = line[items_len:]

            first_half_set = set(first_half)
            second_half_set = set(second_half)

            common_error_char = first_half_set & second_half_set
            error_chars.append(list(common_error_char)[0])

    return calculate_total_priorities(error_chars)


def part_two(puzzle_input):
    error_chars = []

    with open(puzzle_input, "r") as file:
        lines = file.read().splitlines()
        for i in range(0, len(lines), 3):
            first_elf_items = lines[i]
            second_elf_items = lines[i+1]
            third_elf_items = lines[i+2]

            first_set = set(first_elf_items)
            second_set = set(second_elf_items)
            third_set = set(third_elf_items)

            common_error_char = first_set & second_set & third_set
            error_chars.append(list(common_error_char)[0])

    return calculate_total_priorities(error_chars)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()