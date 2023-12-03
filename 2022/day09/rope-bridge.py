import numpy as np


def parse_input(filename):
    with open(filename, "r") as file:
        moves = [(line.split()[0], int(line.split()[1])) for line in file.readlines()]

    return moves


def part_one(puzzle_input):
    moves = parse_input(puzzle_input)
    head = np.array([0, 0])
    tail = np.array([0, 0])
    tail_history_set = set()
    direction_to_array_dict = {
        'U': np.array([0, -1]),
        'D': np.array([0,  1]),
        'R': np.array([1, 0]),
        'L': np.array([-1, 0])
    }

    for direction, steps in moves:
        for i in range(steps):
            head += direction_to_array_dict[direction]
            distance = head - tail
            if max(abs(distance)) > 1:
                tail += np.sign(distance)
            tail_history_set.add(tuple(tail))

    return len(tail_history_set)


def part_two(puzzle_input):
    moves = parse_input(puzzle_input)
    snake = [np.array([0, 0]) for i in range(10)]
    tail_history_set_1 = set()
    tail_history_set_9 = set()
    direction_to_array_dict = {
        'U': np.array([0, -1]),
        'D': np.array([0, 1]),
        'R': np.array([1, 0]),
        'L': np.array([-1, 0])
    }

    for direction, steps in moves:
        for _ in range(steps):
            snake[0] += direction_to_array_dict[direction]
            for i in range(1, len(snake)):
                distance = snake[i-1] - snake[i]
                if max(abs(distance)) > 1:
                    snake[i] += np.sign(distance)
            tail_history_set_1.add(tuple(snake[1]))
            tail_history_set_9.add(tuple(snake[9]))

    return len(tail_history_set_9)


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
