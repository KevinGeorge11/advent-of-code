def parse_input(filename):
    with open(filename, "r") as file:
        patterns_data = file.read().split("\n\n")
        patterns = [[[char for char in line.strip()] for line in pattern.split()] for pattern in patterns_data]

        return patterns


def part_one(puzzle_input):
    patterns = parse_input(puzzle_input)

    return summarize_patterns(patterns)


def part_two(puzzle_input):
    patterns = parse_input(puzzle_input)

    return summarize_patterns(patterns, has_smudge=True)


def summarize_patterns(patterns, has_smudge=False):
    total = 0
    for pattern in patterns:
        rows = [row for row in pattern]
        horizontal_reflection_index = find_reflection(rows, has_smudge)
        total += 100 * horizontal_reflection_index

        cols = [col for col in zip(*pattern)]
        vertical_reflection_index = find_reflection(cols, has_smudge)
        total += vertical_reflection_index

    return total


def find_reflection(pattern, has_smudge):
    for i in range(len(pattern) - 1):
        if has_smudge:
            if is_reflecting_with_fixed_smudge(pattern, i):
                return i + 1
        else:
            if is_reflecting(pattern, i):
                return i + 1

    return 0


def is_reflecting(pattern, index):
    start, end = index, index + 1

    while start >= 0 and end < len(pattern):
        if pattern[start] != pattern[end]:
            return False
        start -= 1
        end += 1

    return True


def is_reflecting_with_fixed_smudge(pattern, index):
    start, end = index, index + 1
    fixed_smudge = False

    while start >= 0 and end < len(pattern):
        if pattern[start] != pattern[end]:
            # we already fixed smudge, but there are still corresponding lines that do not reflect
            if fixed_smudge:
                return False
            # found potential smudge that we can fix
            elif is_fixable_by_one_smudge(pattern[start], pattern[end]):
                fixed_smudge = True
            else:
                return False
        start -= 1
        end += 1

    return fixed_smudge


def is_fixable_by_one_smudge(line_start, line_end):
    count_mismatches = 0
    for char_a, char_b in zip(line_start, line_end):
        if char_a != char_b:
            count_mismatches += 1

    return count_mismatches == 1


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
