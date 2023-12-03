from print_colors import bcolors


def parse_input(filename):
    with open(filename, "r") as file:
        rows_data = file.read().splitlines()
        columns_data = list(zip(*rows_data))

        return rows_data, columns_data


def count_viewing_distance(trees_list, current_tree_height):
    count = 0
    for tree in trees_list:
        count += 1
        if tree >= current_tree_height:
            break

    return count


def part_one(puzzle_input):
    rows_data, columns_data = parse_input(puzzle_input)
    count_visible_trees = 0

    for y in range(len(rows_data)):
        for x in range(len(columns_data)):

            current_tree_height = int(rows_data[y][x])

            left_side = [int(l) for l in rows_data[y][:x]]
            right_side = [int(r) for r in rows_data[y][x+1:]]
            top_side = [int(t) for t in columns_data[x][:y]]
            bottom_side = [int(d) for d in columns_data[x][y+1:]]

            # compare each side if current tree is the max height, note -1 is for edges / empty lists
            is_max_for_left = current_tree_height > max(left_side if left_side else [-1])
            is_max_for_right = current_tree_height > max(right_side if right_side else [-1])
            is_max_for_top = current_tree_height > max(top_side if top_side else [-1])
            is_max_for_bottom = current_tree_height > max(bottom_side if bottom_side else [-1])

            # tree is visible as long as its height is the max for one of the sides
            if is_max_for_left or is_max_for_right or is_max_for_top or is_max_for_bottom:
                count_visible_trees += 1
                # print(f'{bcolors.WARNING}Tree is Visible!{bcolors.ENDC}')

    return count_visible_trees


def part_two(puzzle_input):
    rows_data, columns_data = parse_input(puzzle_input)
    highest_scenic_score = 0

    for y in range(len(rows_data)):
        for x in range(len(columns_data)):
            current_tree_height = int(rows_data[y][x])

            left_side = [int(l) for l in rows_data[y][:x]]
            right_side = [int(r) for r in rows_data[y][x+1:]]
            top_side = [int(t) for t in columns_data[x][:y]]
            bottom_side = [int(d) for d in columns_data[x][y+1:]]

            # count viewing distance for each side, the left and top sides need to be reversed for nearest to farthest
            left_distance = count_viewing_distance(reversed(left_side), current_tree_height)
            right_distance = count_viewing_distance(right_side, current_tree_height)
            top_distance = count_viewing_distance(reversed(top_side), current_tree_height)
            bottom_distance = count_viewing_distance(bottom_side, current_tree_height)

            scenic_score = left_distance * right_distance * top_distance * bottom_distance
            # print(f'{bcolors.WARNING} Scenic Score is : {scenic_score} {bcolors.ENDC}')

            highest_scenic_score = scenic_score if scenic_score > highest_scenic_score else highest_scenic_score

    return highest_scenic_score


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
