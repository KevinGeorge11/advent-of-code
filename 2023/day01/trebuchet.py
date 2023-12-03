def find_all_word_numbers(string):
    numbers = []
    word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, char in enumerate(string):
        if char.isdigit():
            numbers.append(char)
        else:
            for j, word in enumerate(word_numbers):
                if string[i:i + len(word)] == word:
                    numbers.append(str(j + 1))

    return numbers


def part_one(puzzle_input):
    sum_of_values = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            numbers = [s for s in line if s.isdigit()]
            calibration_value = int(numbers[0] + numbers[-1])
            sum_of_values += calibration_value

    return sum_of_values


def part_two(puzzle_input):
    sum_of_values = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            numbers = find_all_word_numbers(line)
            calibration_value = int(numbers[0] + numbers[-1])
            sum_of_values += calibration_value

    return sum_of_values


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
