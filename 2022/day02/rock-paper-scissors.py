def part_one(puzzle_input):
    rock_points = 1         # opponent action is rock if A
    paper_points = 2        # opponent action is paper if B
    scissors_points = 3     # opponent action is scissors if C

    lose_points = 0
    draw_points = 3
    win_points = 6
    total_points = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            opponent_move = line[0]
            player_move = line[2]

            match player_move:
                # X is rock
                case "X":
                    total_points += rock_points

                    if opponent_move == "A":
                        total_points += draw_points
                    elif opponent_move == "C":
                        total_points += win_points
                # Y is paper
                case "Y":
                    total_points += paper_points

                    if opponent_move == "B":
                        total_points += draw_points
                    elif opponent_move == "A":
                        total_points += win_points
                # Z is scissors
                case "Z":
                    total_points += scissors_points

                    if opponent_move == "C":
                        total_points += draw_points
                    elif opponent_move == "B":
                        total_points += win_points

    return total_points


def part_two(puzzle_input):
    rock_points = 1         # opponent action is rock if A
    paper_points = 2        # opponent action is paper if B
    scissors_points = 3     # opponent action is scissors if C

    lose_points = 0
    draw_points = 3
    win_points = 6
    total_points = 0

    with open(puzzle_input, "r") as file:
        for line in file:
            opponent_move = line[0]
            player_move = line[2]

            match player_move:
                # X is to lose the game
                case "X":
                    total_points += lose_points

                    # scissors loses to rock(A)
                    if opponent_move == "A":
                        total_points += scissors_points
                    # rock loses to paper(B)
                    elif opponent_move == "B":
                        total_points += rock_points
                    # paper loses to scissors(C)
                    elif opponent_move == "C":
                        total_points += paper_points
                # Y is to draw the game
                case "Y":
                    total_points += draw_points

                    # rock draws with rock(A)
                    if opponent_move == "A":
                        total_points += rock_points
                    # paper draws with paper(B)
                    elif opponent_move == "B":
                        total_points += paper_points
                    # scissors draws with scissors(C)
                    elif opponent_move == "C":
                        total_points += scissors_points
                # Z is to win the game
                case "Z":
                    total_points += win_points
                    # paper beats rock(A)
                    if opponent_move == "A":
                        total_points += paper_points
                    # scissors beats paper(B)
                    elif opponent_move == "B":
                        total_points += scissors_points
                    # rock beats scissors(C)
                    elif opponent_move == "C":
                        total_points += rock_points

    return total_points


def main() -> None:
    puzzle_input = "input.txt"
    print(part_one(puzzle_input))
    print(part_two(puzzle_input))


if __name__ == "__main__":
    main()
