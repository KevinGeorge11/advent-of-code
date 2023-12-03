
def parse_input(filename):
    with open(filename, "r") as file:
        program = []
        for line in file.read().splitlines():
            if line == "noop":
                instruction, value = line, ""
            else:
                instruction, value = line.split()
            program.append((instruction, value))

        return program


def calculate_x_generator():
    x = 1
    program = parse_input("input.txt")
    for instruction, value in program:
        match instruction:
            case "noop":
                yield x
            case "addx":
                yield x
                yield x
                x += int(value)


def part_one(puzzle_input):
    return sum(i * x for i, x in enumerate(calculate_x_generator(), start=1) if i % 40 == 20)


def part_two(puzzle_input):
    return


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    # print(part_two(puzzle_input))



if __name__ == "__main__":
    main()
