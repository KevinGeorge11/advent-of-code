def parse_input(filename):
    games_summary = []
    with open(filename, "r") as file:
        for line in file:
            game, cubes_record = line.rstrip('\n').split(":")
            game_id = int(game[4:])
            cubes_pulls = cubes_record.replace(";", ",").split(",")
            cubes_max_summary = {"red": 0, "blue": 0, "green": 0}

            for i, cubes in enumerate(cubes_pulls):
                _, cube_num, cube_type = cubes.split(" ")

                for color in ["red", "blue", "green"]:
                    num = int(cube_num)
                    if cube_type == color and num > cubes_max_summary[color]:
                        cubes_max_summary[color] = num

            games_summary.append((game_id, cubes_max_summary))

    return games_summary


def part_one(puzzle_input):
    game_summary = parse_input(puzzle_input)
    sum_ids = sum([game_id for game_id, cube_summary in game_summary
                   if cube_summary["red"] <= 12 and cube_summary["green"] <= 13 and cube_summary["blue"] <= 14])

    return sum_ids


def part_two(puzzle_input):
    game_summary = parse_input(puzzle_input)
    sum_of_powers_of_min_set = sum([cube_summary["red"] * cube_summary["green"] * cube_summary["blue"]
                   for game_id, cube_summary in game_summary])

    return sum_of_powers_of_min_set


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()