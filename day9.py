from dataclasses import dataclass
from enum import Enum
with open("resources/day9.txt") as f:
    instructions = [x.strip() for x in f.readlines()]


@dataclass(frozen=True)
class Point:
    x: int
    y: int


class Dir(Enum):
    LEFT = "L"
    UP_LEFT = "UL"
    DOWN_LEFT = "DL"
    RIGHT = "R"
    UP_RIGHT = "UR"
    DOWN_RIGHT = "DR"
    UP = "U"
    DOWN = "D"

    def move(self, position):
        if self == Dir.UP:
            return Point(position.x, position.y + 1)
        if self == Dir.DOWN:
            return Point(position.x, position.y - 1)
        if self == Dir.LEFT:
            return Point(position.x - 1, position.y)
        if self == Dir.UP_LEFT:
            return Point(position.x - 1, position.y + 1)
        if self == Dir.DOWN_LEFT:
            return Point(position.x - 1, position.y - 1)
        if self == Dir.RIGHT:
            return Point(position.x + 1, position.y)
        if self == Dir.UP_RIGHT:
            return Point(position.x + 1, position.y + 1)
        if self == Dir.DOWN_RIGHT:
            return Point(position.x + 1, position.y - 1)


def is_adjacent(point1: Point, point2: Point):
    return abs(point1.x - point2.x) <= 1 and abs(point1.y - point2.y) <= 1


def move_tail(head: Point, tail: Point) -> Point:
    if is_adjacent(head, tail):
        return tail
    if head.x - tail.x > 1 and head.y == tail.y:
        return Dir.RIGHT.move(tail)
    if tail.x - head.x > 1 and head.y == tail.y:
        return Dir.LEFT.move(tail)
    if head.y - tail.y > 1 and head.x == tail.x:
        return Dir.UP.move(tail)
    if tail.y - head.y > 1 and head.x == tail.x:
        return Dir.DOWN.move(tail)
    if head.x > tail.x and head.y > tail.y:
        return Dir.UP_RIGHT.move(tail)
    if head.x < tail.x and head.y > tail.y:
        return Dir.UP_LEFT.move(tail)
    if head.x > tail.x and head.y < tail.y:
        return Dir.DOWN_RIGHT.move(tail)
    if head.x < tail.x and head.y < tail.y:
        return Dir.DOWN_LEFT.move(tail)


def move_snake(snake: list[Point], dir: Dir) -> list[Point]:
    snake[0] = dir.move(snake[0])
    for i in range(len(snake) - 1):
        snake[i+1] = move_tail(snake[i], snake[i+1])
    return snake


def solve() -> tuple[int]:
    visited1 = set()
    visited2 = set()
    tail = head = Point(0, 0)
    snake = [Point(0, 0) for _ in range(10)]

    for instruction in instructions:
        dir, dist = instruction.split()
        for _ in range(int(dist)):
            head = Dir(dir).move(head)
            tail = move_tail(head, tail)
            snake = move_snake(snake, Dir(dir))
            visited1.add(tail)
            visited2.add(snake[-1])
    return {"part1": len(visited1), "part2": len(visited2)}


answer = solve()
print(answer["part1"])
print(answer["part2"])
