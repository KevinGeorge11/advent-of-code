from enum import Enum


class Direction(Enum):
    NORTH = 1
    WEST = 2
    SOUTH = 3
    EAST = 4


def parse_input(filename):
    with open(filename, "r") as file:
        platform_data = [[char for char in line] for line in file.read().splitlines()]
        return platform_data


def part_one(puzzle_input):
    platform = parse_input(puzzle_input)

    platform = tilt(platform, Direction.NORTH)
    # print_platform(platform)

    return calculate_load(platform)


def part_two(puzzle_input):
    platform = parse_input(puzzle_input)

    platform, spin_num, repeat_state_spin_len = find_repeated_state(platform)
    platform = run_remaining_cycles(platform, spin_num, repeat_state_spin_len)

    return calculate_load(platform)


def calculate_load(platform):
    rock_points = [(i, j) for i, row in enumerate(platform) for j, char in enumerate(row) if char == "O"]
    rows_len = len(platform)

    return sum([rows_len - rock[0] for rock in sorted(rock_points)])


def find_repeated_state(platform):
    platforms_dict = dict()
    spin_num = 1

    # eventually the platform state repeats itself, so find after how many spins does this happen at
    while True:
        platform = cycle(platform)
        platform_string = "".join(["".join(row) for row in platform])

        # found our repeated platform state
        if platform_string in platforms_dict:
            return platform, spin_num, spin_num - platforms_dict[platform_string]

        platforms_dict[platform_string] = spin_num
        spin_num += 1


def run_remaining_cycles(platform, spin_num, repeat_state_spin_len):
    spins_left = 1_000_000_000 - spin_num
    loops_completed = spins_left // repeat_state_spin_len
    spins_left -= loops_completed * repeat_state_spin_len

    while spins_left > 0:
        platform = cycle(platform)
        spins_left -= 1

    return platform


def cycle(platform):
    for direction in Direction:
        platform = tilt(platform, direction)
    return platform


def tilt(platform, direction):
    rows_len, cols_len = len(platform), len(platform[0])
    new_platform = [row[:] for row in platform]

    match direction:
        # reverse our iteration if we are going bottom to top (from SOUTH) or right to left (from EAST)
        case Direction.SOUTH | Direction.EAST:
            rows_range = range(rows_len - 1, -1, -1)
            cols_range = range(cols_len - 1, -1, -1)

        case Direction.NORTH | Direction.WEST | _:
            rows_range = range(rows_len)
            cols_range = range(cols_len)

    for r in rows_range:
        for c in cols_range:
            if new_platform[r][c] == "O":
                new_row = r
                new_col = c

                match direction:
                    case Direction.NORTH:
                        # check above if it is empty space, if so we can move to it
                        while new_row - 1 >= 0 and new_platform[new_row - 1][c] == ".":
                            new_row -= 1

                    case Direction.WEST:
                        # check left if it is empty space, if so we can move to it
                        while new_col - 1 >= 0 and new_platform[r][new_col - 1] == ".":
                            new_col -= 1

                    case Direction.SOUTH:
                        # check below if it is empty space, if so we can move to it
                        while new_row + 1 < rows_len and new_platform[new_row + 1][c] == ".":
                            new_row += 1

                    case Direction.EAST:
                        # check right if it is empty space, if so we can move to it
                        while new_col + 1 < cols_len and new_platform[r][new_col + 1] == ".":
                            new_col += 1

                new_platform[r][c] = "."
                new_platform[new_row][new_col] = "O"

    return new_platform


# import pprint as
# pp = pprint.PrettyPrint(indent=4)
# pp.pprint(f'{}')
def print_platform(platform):
    rows_len, cols_len = len(platform), len(platform[0])
    for r in range(rows_len):
        for c in range(cols_len):
            print(f'{platform[r][c]}', end="")
        print()


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
