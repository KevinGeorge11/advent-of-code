import math


def parse_input(filename):
    with open(filename, "r") as file:
        data = file.read().splitlines()
        time_data = [int(x) for x in data[0].split()[1:]]
        distance_data = [int(x) for x in data[1].split()[1:]]

        race_records = []
        for i in range(len(time_data)):
            race_records.append((time_data[i], distance_data[i]))

        big_time = int(''.join(str(x) for x in time_data))
        big_distance = int(''.join(str(x) for x in distance_data))
        final_race = (big_time, big_distance)

    #print(race_records)
    #print(final_race)

    return race_records, final_race


def part_one(puzzle_input):
    race_records, final_race = parse_input(puzzle_input)
    product = 1
    for race_time, record_distance in race_records:
        product *= find_num_ways_to_beat_record(race_time, record_distance)

    return product


def part_two(puzzle_input):
    race_records, final_race = parse_input(puzzle_input)
    race_time = final_race[0]
    record_distance = final_race[1]

    return find_num_ways_to_beat_record(race_time, record_distance)


def find_num_ways_to_beat_record(race_time, record_distance):
    '''
    (race_time - hold_time) * speed > record_distance
    (race_time - hold_time) * hold_time > record_distance          speed = hold_time in this case
    hold_time * race_time - (hold_time)^2 > record_distance
    -1(hold_time)^2 + race_time(hold_time) - record_distance > 0
    a = -1 ,  b = race_time,  c = -record_distance
    '''
    a, b, c = -1, race_time, -record_distance
    hold_time1, hold_time2 = solve_quadratic_formula(a, b, c)

    return abs(hold_time2 - hold_time1) + 1


def solve_quadratic_formula(a, b, c):
    '''
    quadratic equation : ax2 + bx + c = 0
    ax2 + bx + c = 0, where a, b and c are real numbers and a != 0
    '''
    root1, root2 = 0, 0
    discriminant = b * b - 4 * a * c
    sqrt_value = math.sqrt(abs(discriminant))

    if discriminant > 0:
        min_root_decimal = (-b + sqrt_value) / (2 * a)
        max_root_decimal = (-b - sqrt_value) / (2 * a)
        min_root = math.ceil(min_root_decimal)
        max_root = math.floor(max_root_decimal)

        if min_root_decimal == min_root:
            min_root += 1
            max_root -= 1

        root1 = min_root
        root2 = max_root

    elif discriminant == 0:
        root_decimal = -b / (2 * a)
        root = math.ceil(root_decimal)
        root1 = root
        root2 = root

    return root1, root2


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
