from Pos import Pos
from Graph import Graph
from queue import Queue

NORTH = Pos(-1, 0)
SOUTH = Pos(1, 0)
WEST = Pos(0, -1)
EAST = Pos(0, 1)

def parse_input(filename):
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

        start_neighbours = [start + NORTH, start + SOUTH, start + WEST, start + EAST]
        for neighbour in start_neighbours:
            # check if edge from start to it neighbour exists in graph, include edges[start] = neighbour if so
            if start in pipe_graph.edges[neighbour]:
                pipe_graph.add_edge(start, neighbour)

        return start, pipe_graph, rows_len, cols_len


def bfs(start, pipe_graph):
    distance = {start: 0}
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        current_pos = queue.get()
        for neighbour in pipe_graph.edges[current_pos]:
            # already check this neighbour so skip it
            if neighbour in distance:
                continue
            # found new neighbours to check through
            distance[neighbour] = distance[current_pos] + 1
            queue.put(neighbour)

    return distance


def part_one(puzzle_input):
    start, pipe_graph, rows_len, cols_len = parse_input(puzzle_input)
    distance_from_start = bfs(start, pipe_graph)

    return max(distance_from_start.values())


def part_two(puzzle_input):
    start, pipe_graph, rows_len, cols_len = parse_input(puzzle_input)
    distance_from_start = bfs(start, pipe_graph)
    pipe_loop_vertices = set(distance_from_start.keys())
    # print(loop)
    # print(g.edges)

    area = 0
    for i in range(rows_len):
        for j in range(cols_len):
            pos = Pos(i, j)
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

        # walk along horizontal edge
        if next_pos in pipe_loop_vertices and current_pos in pipe_loop_vertices and next_pos in pipe_graph.edges[current_pos]:
            continue

        # if enter or exited points intersect at a vertical type pipe, increase the number of intersections
        # loosely based on ray casting
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

        if next_pos in pipe_loop_vertices:
            entered = next_pos

    return (line_intersections % 2) == 1


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
