def parse_input(filename):
    with open(filename, "r") as file:
        calories = 0
        elves_calories = []
        for line in file:
            if line == '\n':
                elves_calories.append(calories)
                calories = 0
            else:
                calories += int(line)

    return elves_calories


def part_one(puzzle_input):
    elves_calories = parse_input(puzzle_input)
    return max(elves_calories)


def part_two(puzzle_input):
    elves_calories_top3 = [0, 0, 0]
    elves_calories = parse_input(puzzle_input)

    for elf in elves_calories:
        if elf > elves_calories_top3[0]:
            old_max = elves_calories_top3[0]
            elves_calories_top3[0] = elf
            elves_calories_top3[1] = old_max
        elif elf > elves_calories_top3[1]:
            old_max = elves_calories_top3[1]
            elves_calories_top3[1] = elf
            elves_calories_top3[2] = old_max
        elif elf > elves_calories_top3[2]:
            elves_calories_top3[2] = elf

    return sum(elves_calories_top3)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
