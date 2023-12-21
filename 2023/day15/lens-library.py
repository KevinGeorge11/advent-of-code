from collections import defaultdict


def parse_input(filename):
    with open(filename, "r") as file:
        sequence_data = file.read().strip().split(",")
        return sequence_data


def part_one(puzzle_input):
    sequence = parse_input(puzzle_input)

    return sum(map(hash_algorithm, sequence))


def part_two(puzzle_input):
    sequence = parse_input(puzzle_input)
    box_hashmap = defaultdict(list)

    for step in sequence:
        if '=' in step:
            label, focus_length = step.split('=')
            box_num = hash_algorithm(label)
            lens = (label, int(focus_length))

            is_lens_in_box = False
            for i, item in enumerate(box_hashmap[box_num]):
                if item[0] == label:
                    box_hashmap[box_num][i] = lens
                    is_lens_in_box = True
                    break

            if not is_lens_in_box:
                box_hashmap[box_num].append(lens)
        else:
            label, focus_length = step.split('-')
            box_num = hash_algorithm(label)

            for item in box_hashmap[box_num]:
                if item[0] == label:
                    box_hashmap[box_num].remove(item)
                    break

    return calculate_total_focus_power(box_hashmap)


def hash_algorithm(step, value=0):
    for char in step:
        value = ((value + ord(char)) * 17) % 256

    return value


def calculate_total_focus_power(box_hashmap):
    total = 0
    for box_num, lenses in box_hashmap.items():
        focus_power = sum((int(box_num) + 1) * (i + 1) * lens[1] for i, lens in enumerate(lenses))
        total += focus_power

    return total


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
