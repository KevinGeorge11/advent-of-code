def parse_input(filename):
    with open(filename, "r") as file:
        stack_lines, instructions_lines = [
            part.split("\n") for part in file.read().split("\n\n")
        ]

    stack_crates = [[] for x in range(10)]
    for line in stack_lines:
        for count, box_value in enumerate(line[::4]):
            if box_value == "[":
                stack_crates[count + 1].insert(0, line[count*4 + 1])

    instructions = []
    for line in instructions_lines:
        _, num_boxes, _, src, _, dst = line.split(" ")
        step = [int(num_boxes), int(src), int(dst)]
        instructions.append(step)

    return stack_crates, instructions


'''
def print_stack(stack):
    for j in range(0, len(stack)):
        print(f' {[j]} :', end="")
        for i in range(0, len(stack[j])):
            print(f' {stack[j][i]} ', end="")
        print("")
'''


def part_one(puzzle_input):
    stack, instructions = parse_input(puzzle_input)

    for step in instructions:
        num_boxes = step[0]
        src = step[1]
        dst = step[2]
        for x in range(0, num_boxes):
            value = stack[src].pop()
            stack[dst].append(value)

    # get top items of stack
    message = ""
    for x in stack[1::]:
        message += x[-1]

    return message


def part_two(puzzle_input):
    stack, instructions = parse_input(puzzle_input)

    for step in instructions:
        num_boxes = step[0]
        src = step[1]
        dst = step[2]

        removed_crates = stack[src][-num_boxes:]
        stack[src] = stack[src][:-num_boxes]

        stack[dst].extend(removed_crates)

    message = ""
    for x in stack[1::]:
        message += x[-1]

    return message


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
