lines = open("input.txt", "r").readlines()


def points_for_move(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    if move == "Z":
        return 3


def points_for_win(opp_move, our_move):
    if opp_move == "A":
        if our_move == "X":
            return 3
        if our_move == "Y":
            return 6
        if our_move == "Z":
            return 0
    if opp_move == "B":
        if our_move == "X":
            return 0
        if our_move == "Y":
            return 3
        if our_move == "Z":
            return 6
    if opp_move == "C":
        if our_move == "X":
            return 6
        if our_move == "Y":
            return 0
        if our_move == "Z":
            return 3


total_points = 0
for line in lines:
    opp_move = line[0]
    our_move = line[2]
    total_points += points_for_move(our_move)
    total_points += points_for_win(opp_move, our_move)

print(total_points)
