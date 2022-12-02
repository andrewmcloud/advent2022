with open("resources/day2.txt") as f:
    game_rounds = [x for x in f.read().strip().split("\n")]

play_score = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
is_draw = {"A": "X", "B": "Y", "C": "Z"}
is_winning = {"A": "Y", "B": "Z", "C": "X"}
is_loss = {"A": "Z", "B": "X", "C": "Y"}


def part1(elf: str, me: str) -> int:
    if is_winning[elf] == me:
        return 6 + play_score[me]
    if is_draw[elf] == me:
        return 3 + play_score[me]
    return play_score[me]


def part2(elf: str, me: str) -> int:
    if me == "X":
        # loss
        return play_score[is_loss[elf]]
    elif me == "Y":
        # draw
        return 3 + play_score[is_draw[elf]]
    else:
        # win
        return 6 + play_score[is_winning[elf]]

part1_score = 0
part2_score = 0
for r in game_rounds:
    elf, me = r.split(" ")
    part1_score += part1(elf, me)
    part2_score += part2(elf, me)

print(part1_score)
print(part2_score)



