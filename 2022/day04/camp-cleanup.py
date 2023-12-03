def part_one(puzzle_input):
    num_pairs_that_fully_overlap = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            # get section numbers for each elf
            elf1_start, elf1_end, elf2_start, elf2_end = [int(x) for x in line.replace("-", ",").split(",")]

            # check section range bounds between a pair of elves
            if elf1_start <= elf2_start and elf1_end >= elf2_end or elf1_start >= elf2_start and elf1_end <= elf2_end:
                num_pairs_that_fully_overlap += 1

    return num_pairs_that_fully_overlap


def part_two(puzzle_input):
    num_pairs_that_overlap = 0
    with open(puzzle_input, "r") as file:
        for line in file:
            # get section numbers for each elf
            elf1_start, elf1_end, elf2_start, elf2_end = [int(x) for x in line.replace("-", ",").split(",")]

            # check section range bounds between a pair of elves
            overlap_range = range(max(elf1_start, elf2_start), min(elf1_end, elf2_end) + 1)
            if len(overlap_range):
                num_pairs_that_overlap += 1

    return num_pairs_that_overlap


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
