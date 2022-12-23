from __future__ import annotations
from dataclasses import dataclass, field
from collections import Counter

with open("resources/day23.txt") as f:
    position_graph = [[x for x in line.strip("\n")] for line in f.readlines()]


@dataclass(frozen=True)
class Position:
    row: int
    col: int

    def neighbors(self) -> set[Position]:
        return {
            Position(self.row-1, self.col),    # N
            Position(self.row-1, self.col+1),  # NE
            Position(self.row, self.col+1),    # E
            Position(self.row+1, self.col+1),  # SE
            Position(self.row+1, self.col),    # S
            Position(self.row+1, self.col-1),  # SW
            Position(self.row, self.col-1),    # W
            Position(self.row-1, self.col-1),  # NW
        }

    def northern_neighbors(self) -> tuple[set[Position], Position]:
        return {
            Position(self.row - 1, self.col),      # N
            Position(self.row - 1, self.col + 1),  # NE
            Position(self.row-1, self.col-1),      # NW
        }, Position(self.row - 1, self.col),       # N

    def eastern_neighbors(self) -> tuple[set[Position], Position]:
        return {
           Position(self.row - 1, self.col + 1),   # NE
           Position(self.row, self.col + 1),       # E
           Position(self.row + 1, self.col + 1),   # SE
        }, Position(self.row, self.col + 1),       # E

    def southern_neighbors(self) -> tuple[set[Position], Position]:
        return {
           Position(self.row + 1, self.col + 1),   # SE
           Position(self.row + 1, self.col),       # S
           Position(self.row + 1, self.col - 1),   # SW
        }, Position(self.row + 1, self.col),       # S

    def western_neighbors(self) -> tuple[set[Position], Position]:
        return {
           Position(self.row + 1, self.col - 1),   # SW
           Position(self.row, self.col - 1),       # W
           Position(self.row - 1, self.col - 1),   # NW
        }, Position(self.row, self.col - 1),       # W


def initialize_elf_locations(position_graph):
    elves = set()
    for i, row in enumerate(position_graph):
        for j, elem in enumerate(row):
            if elem == "#":
                elves.add(Position(i, j))
    return elves


def check_north(elf): return elf.northern_neighbors()


def check_south(elf): return elf.southern_neighbors()


def check_west(elf): return elf.western_neighbors()


def check_east(elf): return elf.eastern_neighbors()


def rotate_checks(checks):
    first = checks.pop(0)
    checks.append(first)
    return checks


def move_elves(elf_set: set[Position], checks):
    elves = elf_set
    new_positions = set()
    proposed = []
    for elf in elves:
        cannot_move = True
        if elf.neighbors() & elves:  # if there is at least one neighboring elf
            for check in checks:
                to_check, new = check(elf)
                if not to_check & elves:
                    proposed.append((elf, new))
                    cannot_move = False
                    break
            if cannot_move:
                new_positions.add(elf)
        else:
            new_positions.add(elf)
    moved = set(new_positions)
    counts = Counter([x[1] for x in proposed])
    for elf, new_position in proposed:
        if counts[new_position] > 1:
            moved.add(elf)
        else:
            moved.add(new_position)
    return moved


def part1(position_graph):
    checks = [check_north, check_south, check_west, check_east]
    elves = initialize_elf_locations(position_graph)
    for _ in range(10):
        elves = move_elves(elves, checks)
        checks = rotate_checks(checks)
    min_row = min(elf.row for elf in elves)
    max_row = max(elf.row for elf in elves)
    min_col = min(elf.col for elf in elves)
    max_col = max(elf.col for elf in elves)

    rows = (max_row - min_row) + 1  # inclusive, add one
    cols = (max_col - min_col) + 1  # inclusive, add one
    return rows * cols - len(elves)


def part2(position_graph):
    checks = [check_north, check_south, check_west, check_east]
    elves = initialize_elf_locations(position_graph)
    count = 0
    while True:
        count += 1
        current = elves.copy()
        elves = move_elves(elves, checks)
        checks = rotate_checks(checks)
        if elves == current:
            return count


print(part1(position_graph))
print(part2(position_graph))
