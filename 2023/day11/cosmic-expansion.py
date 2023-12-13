def parse_input(filename):
    with open(filename, "r") as file:
        galaxy_data = [[char for char in line] for line in file.read().splitlines()]
        galaxy_points = [(i, j) for i, row in enumerate(galaxy_data) for j, char in enumerate(row) if char == "#"]
        height, width = len(galaxy_data), len(galaxy_data[0])

        empty_rows = [i for i, row in enumerate(galaxy_data) if all(char == '.' for char in row)]
        empty_cols = [j for j, col in enumerate(zip(*galaxy_data)) if all(char == '.' for char in col)]

        return galaxy_points, height, width, empty_rows, empty_cols


def part_one(puzzle_input):
    galaxy_points, height, width, empty_rows, empty_cols = parse_input(puzzle_input)
    expansion = 1
    point_dists = get_dist_between_every_pair_in_galaxy(galaxy_points, height, width, empty_rows, empty_cols, expansion)

    return sum(point_dists.values())


def part_two(puzzle_input):
    galaxy_points, height, width, empty_rows, empty_cols = parse_input(puzzle_input)
    expansion = 1000000 - 1
    point_dists = get_dist_between_every_pair_in_galaxy(galaxy_points, height, width, empty_rows, empty_cols, expansion)

    return sum(point_dists.values())


def get_dist_between_every_pair_in_galaxy(galaxy_points, height, width, empty_rows, empty_cols, expansion):
    galaxy_points = expand_galaxy_points(galaxy_points, height, width, empty_rows, empty_cols, expansion)
    point_dists = get_dist_between_all_points(galaxy_points)

    return point_dists


def expand_galaxy_points(galaxy_points, height, width, empty_rows, empty_cols, expansion):
    i = j = 0

    while i < height:
        if i in empty_rows:
            galaxy_points = [(y + expansion, x) if y > i else (y, x) for y, x in galaxy_points]
            empty_rows = [r + expansion if r > i else r for r in empty_rows]
            i += expansion
            height += expansion
        else:
            i += 1

    while j < width:
        if j in empty_cols:
            galaxy_points = [(y, x + expansion) if x > j else (y, x) for y, x in galaxy_points]
            empty_cols = [c + expansion if c > j else c for c in empty_cols]
            j += expansion
            width += expansion
        else:
            j += 1

    return galaxy_points


def get_dist_between_all_points(galaxy_points):
    point_dists = {}
    for a1, b1 in galaxy_points:
        for a2, b2 in galaxy_points:
            point1 = (a1, b1)
            point2 = (a2, b2)

            if a1 == a2 and b1 == b2 or (point2, point1) in point_dists:
                continue

            distance = abs(a1 - a2) + abs(b1 - b2)
            point_dists[(point1, point2)] = distance

    return point_dists


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
