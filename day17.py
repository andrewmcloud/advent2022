from dataclasses import dataclass, field
from itertools import cycle
from typing import Optional

with open("resources/day17.txt") as f:
    instruction_string = f.read().strip()


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def move_left(self):
        return Coord(self.x - 1, self.y)

    def move_right(self):
        return Coord(self.x + 1, self.y)

    def move_down(self):
        return Coord(self.x, self.y - 1)


@dataclass
class Rock:
    start_height: int
    points: set

    def move_right(self, obstructions, boundary=6) -> None:
        shifted_right = {point.move_right() for point in self.points}
        if shifted_right & obstructions:
            return
        for point in shifted_right:
            if point.x > boundary:
                return
        self.points = shifted_right

    def move_left(self, obstructions, boundary=0) -> None:
        shifted_left = {point.move_left() for point in self.points}
        if shifted_left & obstructions:
            return
        for point in shifted_left:
            if point.x < boundary:
                return
        self.points = shifted_left

    def settled(self, obstructions):
        shifted_down = {point.move_down() for point in self.points}
        if shifted_down & obstructions:
            return True
        return False

    def move_down(self, obstructions) -> bool:
        shifted_down = {point.move_down() for point in self.points}
        if shifted_down & obstructions:
            return False
        self.points = shifted_down
        return True

    def get_points(self) -> set:
        return self.points

    def get_height(self) -> int:
        return max(point.y for point in self.points)


@dataclass
class Horizontal(Rock):
    points: set = field(init=False)

    def __post_init__(self):
        self.points = {
            Coord(2, self.start_height),
            Coord(5, self.start_height),
            Coord(3, self.start_height),
            Coord(4, self.start_height),
        }

@dataclass
class Diamond(Rock):
    points: set = field(init=False)

    def __post_init__(self):
        self.points = {
            Coord(2, start_height + 1),
            Coord(4, start_height + 1),
            Coord(3, start_height + 2),
            Coord(3, start_height),
        }

@dataclass
class Angle(Rock):
    points: set = field(init=False)

    def __post_init__(self):
        self.points = {
            Coord(2, start_height),
            Coord(3, start_height),
            Coord(4, start_height),
            Coord(4, start_height + 2),
            Coord(4, start_height + 1),
        }


@dataclass
class Vertical(Rock):
    points: set = field(init=False)

    def __post_init__(self):
        self.points = {
            Coord(2, start_height + 2),
            Coord(2, start_height + 1),
            Coord(2, start_height + 3),
            Coord(2, start_height),
        }


@dataclass
class Square(Rock):
    points: set = field(init=False)

    def __post_init__(self):
        self.points = {
            Coord(2, start_height + 1),
            Coord(3, start_height + 1),
            Coord(3, start_height),
            Coord(2, start_height),
        }


def rock_factory(i, start_height):
    shapes = [Horizontal, Diamond, Angle, Vertical, Square]
    return shapes[i % 5](start_height)


obstructions = {Coord(i, 0) for i in range(7)}
instruction = cycle([i for i in instruction_string])

height = 0
rock_index = 0
start_height = height + 4
while rock_index < 2022:
    rock = rock_factory(rock_index, start_height)
    rock_index += 1
    while True:
        jet = next(instruction)
        if jet == ">":
            rock.move_right(obstructions)
        elif jet == "<":
            rock.move_left(obstructions)
        can_move = rock.move_down(obstructions)
        if not can_move:
            obstructions = obstructions | (rock.get_points())
            height = max(height, rock.get_height())
            start_height = height + 4
            break

print(height)
