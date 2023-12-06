def parse_input(filename):
    with open(filename, "r") as file:
        data = file.read().split("\n\n")

        seeds = [int(x) for x in data[0].split(" ")[1:]]
        category_map_lists = []

        for i, category_data in enumerate(data[1:]):
            parsed_category_data = [maps.split(" ") for maps in category_data.splitlines()[1:]]
            category_maps = [(int(line[0]), int(line[1]), int(line[2])) for line in parsed_category_data]
            category_map_lists.append(category_maps)

        # print(seeds)
        # print(category_map_lists)

        return seeds, category_map_lists


def find_mapped_value(num, category_maps):
    converted_num = num
    for dst, src, range_length in category_maps:
        src_start = src
        src_end = src_start + range_length - 1

        if src_start <= num <= src_end:
            delta = num - src_start
            converted_num = delta + dst

    return converted_num


def find_mapped_location_nums(seeds, category_map_lists):
    location_nums = []
    for seed_num in seeds:
        previous_value = seed_num
        converted_value = seed_num

        for category_maps in category_map_lists:
            converted_value = find_mapped_value(previous_value, category_maps)
            previous_value = converted_value

        location_nums.append(converted_value)

    return location_nums


def part_one(puzzle_input):
    seeds, category_map_lists = parse_input(puzzle_input)

    return min(find_mapped_location_nums(seeds, category_map_lists))


def find_mapped_ranges(ranges, category_maps):
    possible_ranges = []
    for start, end in ranges:
        overlap_ranges = []

        for dst, src, range_length in category_maps:
            src_start, src_end = src, src + range_length - 1
            lower_bound = max(start, src_start)
            upper_bound = min(end, src_end)

            if lower_bound <= upper_bound:
                overlap_ranges.append((lower_bound, upper_bound))
                possible_ranges.append((lower_bound - src + dst, upper_bound - src + dst))

        # no overlap_ranges found means we can convert our original range 1-to-1
        if not overlap_ranges:
            possible_ranges.append((start, end))
            continue
        overlap_ranges.sort()

        # check if there is a gap at the beginning and if there is a gap fill it in
        first_range = overlap_ranges[0]
        if first_range[0] > start:
            possible_ranges.append((start, first_range[0] - 1))
        # check if there is a gap at the end and if there is a gap fill it in
        last_range = overlap_ranges[-1]
        if last_range[1] < end:
            possible_ranges.append((last_range[1] + 1, end))
        # check every pair of a, b ranges and if there is a gap fill it in
        for i in range(len(overlap_ranges) - 1):
            range_a_start, range_a_end = overlap_ranges[i]
            range_b_start, range_b_end = overlap_ranges[i + 1]
            if range_b_start > range_a_end + 1:
                possible_ranges.append((range_a_end + 1, range_b_end - 1))

    return possible_ranges


def get_location_ranges(seed_ranges, category_map_lists):
    previous_ranges = seed_ranges
    converted_ranges = seed_ranges
    for category_maps in category_map_lists:
        converted_ranges = find_mapped_ranges(previous_ranges, category_maps)
        previous_ranges = converted_ranges

    return converted_ranges


def part_two(puzzle_input):
    seeds, category_map_lists = parse_input(puzzle_input)
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    locations = get_location_ranges(seed_ranges, category_map_lists)
    return min(locations)[0]


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
