from Pos import Pos

UP = Pos(-1, 0)
DOWN = Pos(1, 0)
LEFT = Pos(0, -1)
RIGHT = Pos(0, 1)


def parse_input(filename):
    with open(filename, "r") as file:
        layout_data = [[char for char in line] for line in file.read().splitlines()]

        return layout_data


def part_one(puzzle_input):
    layout = parse_input(puzzle_input)

    return get_energized_tiles_len(layout, Pos(0, -1), RIGHT)


def part_two(puzzle_input):
    layout = parse_input(puzzle_input)
    rows_len, cols_len = len(layout), len(layout[0])
    max_energized_tiles_len = 0

    for i in range(rows_len):
        max_energized_tiles_len = max(max_energized_tiles_len,
                                      get_energized_tiles_len(layout, Pos(i, cols_len), LEFT),
                                      get_energized_tiles_len(layout, Pos(i, -1), RIGHT))
    for j in range(cols_len):
        max_energized_tiles_len = max(max_energized_tiles_len,
                                      get_energized_tiles_len(layout, Pos(rows_len, j), UP),
                                      get_energized_tiles_len(layout, Pos(-1, j), DOWN))

    return max_energized_tiles_len


def get_energized_tiles_len(layout, start_pos, start_direction):
    rows_len, cols_len = len(layout), len(layout[0])
    energized_tiles, visited = set(), set()
    beams = [(start_pos, start_direction)]

    while beams:
        pos, direction = beams.pop()
        visited.add((pos, direction))
        next_pos = pos + direction
        if not (0 <= next_pos.r < rows_len and 0 <= next_pos.c < cols_len):
            continue

        energized_tiles.add(next_pos)
        first_beam, second_beam = (next_pos, direction), (next_pos, direction)
        splitter_found = False
        match layout[next_pos.r][next_pos.c]:
            case '.':
                pass
            case '/':
                next_direction = {RIGHT: UP, DOWN: LEFT, UP: RIGHT, LEFT: DOWN}[direction]
                first_beam = (next_pos, next_direction)
            case '\\':
                next_direction = {RIGHT: DOWN, DOWN: RIGHT, UP: LEFT, LEFT: UP}[direction]
                first_beam = (next_pos, next_direction)
            case '-':
                if direction.r != 0:
                    splitter_found = True
                    first_beam = (next_pos, LEFT)
                    second_beam = (next_pos, RIGHT)
            case '|':
                if direction.c != 0:
                    splitter_found = True
                    first_beam = (next_pos, UP)
                    second_beam = (next_pos, DOWN)

        if first_beam not in visited:
            beams.append(first_beam)

        if splitter_found and second_beam not in visited:
            beams.append(second_beam)

    return len(energized_tiles)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
