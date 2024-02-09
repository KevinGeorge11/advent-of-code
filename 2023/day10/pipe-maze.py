from Pos import Pos
from Graph import Graph
from queue import Queue

# direction delta constants allow it to be easier to check neighbours of a pipe
NORTH = Pos(-1, 0)
SOUTH = Pos(1, 0)
WEST = Pos(0, -1)
EAST = Pos(0, 1)

# Types of pipes:
# | = vertical pipe north <--> south
# - = horizontal pipe east <--> west

# L = 90-degree bend north <--> east
# J = 90-degree bend north <--> west
# 7 = 90-degree bend south <--> west
# F = 90-degree bend south <--> east

# . = ground
# S = starting position
# Note: there is a pipe on S, but the shape is implicit.


def parse_input(filename):
    # Algorithm Time Complexity: O(n^2)
    with open(filename, "r") as file:
        pipe_graph = Graph()
        for i, line in enumerate(file.readlines()):
            for j, char in enumerate(line.strip()):
                pos = Pos(i, j)

                match char:
                    # start position
                    case 'S':
                        start = pos
                    # vertical pipe connecting north and south
                    case '|':
                        pipe_graph.add_edge(pos, pos + NORTH)
                        pipe_graph.add_edge(pos, pos + SOUTH)
                    # horizontal pipe connecting west and east
                    case '-':
                        pipe_graph.add_edge(pos, pos + WEST)
                        pipe_graph.add_edge(pos, pos + EAST)
                    # 90-degree pipe connecting north and east
                    case 'L':
                        pipe_graph.add_edge(pos, pos + NORTH)
                        pipe_graph.add_edge(pos, pos + EAST)
                    # 90-degree bend connecting north and west.
                    case 'J':
                        pipe_graph.add_edge(pos, pos + NORTH)
                        pipe_graph.add_edge(pos, pos + WEST)
                    # 90-degree bend connecting south and west
                    case '7':
                        pipe_graph.add_edge(pos, pos + SOUTH)
                        pipe_graph.add_edge(pos, pos + WEST)
                    # 90-degree bend connecting south and east
                    case 'F':
                        pipe_graph.add_edge(pos, pos + SOUTH)
                        pipe_graph.add_edge(pos, pos + EAST)

            cols_len = j + 1
        rows_len = i + 1

        # now that we found where S is and have built the graph, include S as the actual pipe type it is
        start_neighbours = [start + NORTH, start + SOUTH, start + WEST, start + EAST]
        for neighbour in start_neighbours:
            # find how start connects to its neighbours and include those edges connect from start,
            #  so edges[start] = neighbour
            if start in pipe_graph.edges[neighbour]:
                pipe_graph.add_edge(start, neighbour)

        return start, pipe_graph, rows_len, cols_len


def travel_bfs(start, pipe_graph):
    # Algorithm Time Complexity: O(V + E) <= O(n^2)
    # use a dictionary to store all visited nodes distance from the start
    distance = {start: 0}
    # use a queue for the pipes to visit
    pipes_to_visit_queue = Queue()
    pipes_to_visit_queue.put(start)

    while not pipes_to_visit_queue.empty():
        # get next pipe and check its neighbours
        current_pos = pipes_to_visit_queue.get()
        for neighbour in pipe_graph.edges[current_pos]:
            # we've already checked this neighbour, so we can skip it
            if neighbour in distance:
                continue
            # here we found new neighbours to check through and update its distance
            distance[neighbour] = distance[current_pos] + 1
            pipes_to_visit_queue.put(neighbour)

    return distance


def part_one(puzzle_input):
    """
    Part 1 Problem Description: \n
    | As we arrive at the next island, we see an animal scurrying into a large single, continuous loop of pipes.
    | We get the layout of the area presented as a 2D grid with various connected and disconnected pipes. The animal entered the loop at the position labeled "S".
    |   . . . . .
    |   . S - 7 .
    |   . | . | .
    |   . L - J .
    |   . . . . .
    | Given the input, how many steps along the loop does it take to get from the start of the loop to the point farthest from the start?

    :param puzzle_input: the puzzle input file
    :return: max step distance from the start position while following the loop
    """

    # Solution:
    # 1. parse the 2D map file input into a pipe graph as an adjacency list
    # 2. since the loop doesn't have other branches, BFS can be a good approach here
    # 3. given the graph and the staring position, use BFS to travel along the loop and find the max distance
    #
    # Algorithm Time Complexity: O(n^2)

    start, pipe_graph, rows_len, cols_len = parse_input(puzzle_input)
    distance_from_start = travel_bfs(start, pipe_graph)

    return max(distance_from_start.values())


def part_two(puzzle_input):
    """
    Part 2 Problem Description: \n
    | We explored the loop, but we never encountered the animal which we were chasing. Maybe its nest is within the area enclosed by the loop?
    |   . . . . .
    |   . S - 7 .
    |   . | . | .
    |   . L - J .
    |   . . . . .
    | Given the loop in our input, how many tiles are enclosed by the loop?

    :param puzzle_input: the puzzle input file
    :return: the tiles area within the loop
    """
    # Solution:
    # 1. the loop forms a polygon. Checking if a point is inside or outside a polygon is a common problem!
    # 2. to determine if a point is inside or outside a polygon, draw a horizontal line from that point
    # 2a.   if it is inside, that horizontal line should intersect the outside edges at least once
    # 2b.   if the number of intersections on the edges is odd, then our point is on the inside of the polygon
    # 3. sum the number of points inside the polygon
    #
    # Algorithm Time Complexity: O(n^2)

    start, pipe_graph, rows_len, cols_len = parse_input(puzzle_input)
    distance_from_start = travel_bfs(start, pipe_graph)
    pipe_loop_vertices = set(distance_from_start.keys())
    # print(loop)
    # print(g.edges)

    area = 0
    for i in range(rows_len):
        for j in range(cols_len):
            pos = Pos(i, j)
            # don't need to check the pipes that are on the loop
            if pos in pipe_loop_vertices:
                continue

            if is_inside_loop(pos, pipe_loop_vertices, pipe_graph, cols_len):
                area += 1
                # print(f'point {pos} is inside loop')

    return area


def is_inside_loop(pos, pipe_loop_vertices, pipe_graph, cols_len):
    line_intersections = 0
    for j in range(pos.c, cols_len + 1):
        current_pos = Pos(pos.r, j)
        next_pos = Pos(pos.r, j + 1)

        # walk along horizontal edge to make it count as only one
        # if both the current pipe and the next pipe is on the loop and are connected, it is a horizontal edge
        # looks like --
        if next_pos in pipe_loop_vertices and current_pos in pipe_loop_vertices and next_pos in pipe_graph.edges[current_pos]:
            continue

        # here our current pipe is on the loop, but the next pipe is not. so the current pipe is our exited position
        # if enter or exited points intersect at a vertical type pipe, increase the number of intersections
        if current_pos in pipe_loop_vertices:
            exited = current_pos
            edge_north = edge_south = False
            for node in (entered, exited):
                if node + NORTH in pipe_graph.edges[node]:
                    edge_north = True
                if node + SOUTH in pipe_graph.edges[node]:
                    edge_south = True
            if edge_north and edge_south:
                line_intersections += 1

        # here our current pipe is not on the loop, but next pipe is on the loop. so next pipe is our entered position
        if next_pos in pipe_loop_vertices:
            entered = next_pos

    return (line_intersections % 2) == 1


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
