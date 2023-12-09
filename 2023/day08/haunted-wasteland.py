import math
from collections import defaultdict


def parse_input(filename):
    with open(filename, "r") as file:
        network_dict = defaultdict(lambda: ("", ""))
        data = file.read().splitlines()
        left_right_instructions = [d for d in data[0]]

        for line in data[2:]:
            node_and_network_data = line.split(" = ")
            node = node_and_network_data[0]

            network_data = node_and_network_data[1].split(", ")
            node_left = network_data[0][1:4]
            node_right = network_data[1][0:3]

            network_dict[node] = (node_left, node_right)

        # print(network)
        # print(left_right_instructions)
        return network_dict, left_right_instructions


def part_one(puzzle_input):
    network_dict, left_right_instructions = parse_input(puzzle_input)

    return count_steps_from_start_node_to_z_node("AAA", network_dict, left_right_instructions)


def part_two(puzzle_input):
    network_dict, left_right_instructions = parse_input(puzzle_input)

    a_nodes = [x for x in network_dict.keys() if x.endswith("A")]
    a_nodes_steps = [count_steps_from_start_node_to_z_node(node, network_dict, left_right_instructions)
                     for node in a_nodes]

    # LCM can be used since in this case/input file, the steps from each node ending in A to a node ending in Z
    #   always loops the same number of steps, making it them multiples of their step count from part one
    return math.lcm(*a_nodes_steps)


def count_steps_from_start_node_to_z_node(start_node, network_dict, left_right_instructions):
    node = start_node
    i = 0
    steps = 0
    while not node.endswith("Z"):
        if i >= len(left_right_instructions):
            i = 0

        direction = left_right_instructions[i]
        left_or_right_index = 1 if direction == 'R' else 0
        next_node = network_dict[node][left_or_right_index]
        # print(f'Node {node} going {direction} -> {next_node}')
        node = next_node
        i += 1
        steps += 1

    return steps


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
