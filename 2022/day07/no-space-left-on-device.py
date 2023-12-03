from collections import defaultdict

HOME_LOCATION = "Home:"
MAX_FOLDER_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
UNUSED_SPACE_NEEDED = 30000000


def parse_input(filename):
    folder_sizes = defaultdict(int)
    folder_location_stack = []

    with open(filename, "r") as file:
        for command in file:
            # ignore ls and dir commands since they are not need in the folder size calculations
            if command.startswith("dir") or command.startswith("$ ls"):
                continue

            elif command.startswith("$ cd"):
                param = command.split()[2]

                # $ cd / start at the home folder location
                if param == "/":
                    folder_location_stack.append(HOME_LOCATION)
                # $ cd .. backtracks our folder location by one level, so pop the folder location stack
                elif param == "..":
                    folder_location_stack.pop()
                # $ cd x moves to new folder x by one level,  update the folder location stack
                else:
                    folder_location_stack.append(f'{folder_location_stack[-1]}/{param}')

            else:
                # the command is <size> <filename> , add file size to all folders containing the file
                file_size, file_name = command.split()
                for folder in folder_location_stack:
                    folder_sizes[folder] += int(file_size)

    return folder_sizes


def part_one(puzzle_input):
    folder_sizes = parse_input(puzzle_input)

    # add all folder sizes if their size is at most 100000
    return sum(f for f in folder_sizes.values() if f <= MAX_FOLDER_SIZE)


def part_two(puzzle_input):
    folder_sizes = parse_input(puzzle_input)

    # find size amount required to free
    remaining_disk_space = TOTAL_DISK_SPACE - folder_sizes[HOME_LOCATION]
    size_needed_to_free = UNUSED_SPACE_NEEDED - remaining_disk_space

    # sort the folder sizes and grab smalled folder that just fits the needed size
    for folder in sorted(folder_sizes.values()):
        if folder >= size_needed_to_free:
            return folder


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
