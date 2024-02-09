def find_all_word_numbers(string):
    numbers = []
    word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i, char in enumerate(string):
        # check if we found a digit just like from part 1, if so then include it
        if char.isdigit():
            numbers.append(char)
        # here we have found a letter char, check if the substring starting at our current position matches one of the
        #  spelled word numbers
        #  if the substring matches, include its index + 1 (example "one" = index 0 + 1 = 1)
        else:
            for j, word in enumerate(word_numbers):
                if string[i:i + len(word)] == word:
                    numbers.append(str(j + 1))

    return numbers


def part_one(puzzle_input):
    """
    Part 1 Problem Description: \n
    | Something is wrong with global snow production, and you've been selected to take a look. As you get loaded into a trebuchet, the elves discover that the calibration instructions are encoded. \n
    |
    | Every line presented to you contains a specific calibration value, which is a two-digit number. Specifically, it is the combination of the first digit and last digit in the line.
    |
    | Given a list of lines, what is the sum of all calibration values?
    |
    | Solution Algorithm Analysis: O(n)

    :param puzzle_input: the puzzle input file
    :return: sum of all calibration values

    """
    # Solution:
    # 1. every line has a left-most and right-most digit, each is found as a char
    # 2. find all digits in each line
    # 3. the calibration value for each line is just: int(left_most + right_most)
    # 4. sum the calibration values together

    sum_of_values = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            numbers = [s for s in line if s.isdigit()]
            calibration_value = int(numbers[0] + numbers[-1])
            sum_of_values += calibration_value

    return sum_of_values


def part_two(puzzle_input):
    """
    Part 2 Problem Description: \n
    | Your initial calculations are actually wrong. Turns out some numbers are spelled out!
    |
    | The following is now also counted as valid “digits": "one", "two", "three", "four", "five", "six", "seven", "eight", "nine”
    |
    | What is the sum of all calibration values?
    |
    | Solution Algorithm Analysis: O(n^2)

    :param puzzle_input: the puzzle input file
    :return: sum of all calibration values
    """
    # Solution:
    # 1. every line still has a left-most and right-most digit
    # 2. however we need a new function, find_all_word_numbers, to include word numbers alongside the digits found
    # 3. the calibration value for each line is still: int(left_most + right_most)
    # 4. sum the calibration values together

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
