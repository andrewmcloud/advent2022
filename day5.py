import re
from collections import deque

with open("resources/day5.txt") as f:
    line = f.readline()
    stacks_input = ""
    while line != "\n":
        stacks_input += line
        line = f.readline()
    commands = f.read().strip()

cargo = stacks_input.rstrip().split("\n")[:-1]
labels = stacks_input.strip().split("\n")[-1]
label_indexes = labels
label_ids = [int(x) for x in re.findall("\d", labels)]


def initial_stacks(label_ids: list[int], cargo: list[str]) -> list[list[str]]:
    stacks = [deque([]) for _ in label_ids]
    for _ in range(len(cargo)):
        row = cargo.pop()
        for label_id in label_ids:
            try:
                item = row[label_indexes.index(str(label_id))]
                if item != " ":
                    stacks[label_id-1].appendleft(item)
            except IndexError:
                pass
    return [list(stack) for stack in stacks]


def stack_cargo(commands: str, stacks: list[list[str]], single: bool = True):
    for command in commands.strip().split("\n"):
        instructions = [int(x) for x in re.findall('\d+', command)]
        num, old, new = instructions
        old, new = old - 1, new - 1
        to_move, left = stacks[old][:num], stacks[old][num:]
        stacks[old] = left
        stacks[new] = to_move[::-1] + stacks[new] if single else to_move[:] + stacks[new]
    return "".join([stack[0] for stack in stacks])


stacks = initial_stacks(label_ids, cargo)
# part 1:
print(stack_cargo(commands, stacks[:]))
# part 2:
print(stack_cargo(commands, stacks[:], False))
