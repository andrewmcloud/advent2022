from __future__ import annotations
from dataclasses import dataclass
from collections import deque

with open("resources/day24.txt") as f:
    position_graph = [[x for x in line.strip("\n")] for line in f.readlines()]


@dataclass(frozen=True)
class Blizzards:
    rows: int
    cols: int
    neighbors: tuple
    left: set
    right: set
    up: set
    down: set


def init_blizzards(position_graph) -> Blizzards:
    left, right, up, down = set(), set(), set(), set()
    for i, row in enumerate(position_graph):
        for j, elem in enumerate(row):
            if elem == "<":
                left.add((i-1, j-1))
            elif elem == ">":
                right.add((i-1, j-1))
            elif elem == "^":
                up.add((i-1, j-1))
            elif elem == "v":
                down.add((i-1, j-1))
    return Blizzards(
        rows=len(position_graph) - 2,
        cols=len(position_graph[0]) - 2,
        neighbors=((-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)),
        left=left,
        right=right,
        up=up,
        down=down,
    )


def find_path(blizzards, start, end, time=0):
    seen = set()
    while True:
        time += 1
        queue = deque([[start[0], start[1], time]])
        seen.add((start[0], start[1], time))
        while queue:
            row, col, t = queue.popleft()
            t += 1
            if (row, col) == end:
                return t
            for neighbor in blizzards.neighbors:
                new_row, new_col = neighbor[0] + row, neighbor[1] + col
                if not is_blocked(blizzards, new_row, new_col, t) and (new_row, new_col, t) not in seen:
                    queue.append((new_row, new_col, t))
                    seen.add((new_row, new_col, t))


def is_blocked(blizzards, new_row, new_col, t):
    return any((
        new_row < 0 or new_row >= blizzards.rows,
        new_col < 0 or new_col >= blizzards.cols,
        (new_row, (new_col - t) % blizzards.cols) in blizzards.right,
        (new_row, (new_col + t) % blizzards.cols) in blizzards.left,
        ((new_row - t) % blizzards.rows, new_col) in blizzards.down,
        ((new_row + t) % blizzards.rows, new_col) in blizzards.up
    ))


blizzards = init_blizzards(position_graph)
start = (0, 0)
finish = (blizzards.rows - 1, blizzards.cols - 1)
goal = find_path(blizzards, start, finish)
snacks = find_path(blizzards, finish, start, goal)
back = find_path(blizzards, start, finish, snacks)

# part 1
print(goal)
# part 2
print(back)
