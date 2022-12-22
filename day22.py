from enum import Enum
from dataclasses import dataclass
from itertools import zip_longest, chain
import re
with open("resources/day22.txt") as f:
    input = f.readlines()

input_commands = "50R45L25R43L9R45R39L11R3L33L37R31L5L25L14R45L3L19L31R5L30R29R35R50L36L47R49L40L31L19R7L37R40L41R20L46L40R26R49L49L14L3R21R16L48R21L47L38R11L37R23R45L32L40L6R11L45L37R24R10R12L24L12L38R14R14R48R41R47R47L33L22L19R33R37R46R23R2L2L44R43L3R39L6R24R15L38L43L20R19R48L20R2R9R11L38L32R21L17L34L18L37R43R22L10L48L38L30R48R9R17R4R29R23L23R15R49L17R23L8L8L23L50R14L43R14L31R29L33L7L4R36L14L14L37L33L31R2R38R4R24R2L13L26L50R22R50R11R34L40L22R43L30L43L49R47L10L42L6R26R14R18R15R31L15R19R29L50L45R40L46R46L4L50L22L50R30R8L47L12L42L46L19L32R46R44R49L6L37R2R12L40L27R19R3R46R33L12R1L3R3L20L23R11L39R30R25R31L39L49L18L4L38R22L35L36L35R47R41R49L12R18L11L20L40L25R9L47L32L33L22L1L36L50L37R20R21R39R5L33R10R8L36L33L18R39R12R50R41R22R28R48R37L42L9L47R6R50L1L37R14L20L41L34L3L34R42R17R2R20L8R38L13R49R45R14L2R37L2L4L26L37R2L10L46L40R27R4L47R11R40L24L17L46R30L42L50R37R16L34R20L47L25R11L44R49L28L3L36R8L23L38R40L29R37R40R38R32L32R49R48L48R50L45R24R14R44R39R35L1L10R25L33L25L24R33R32R20R31R28R10R7L29R40R48L34L50R37R19R49L34R50R21R10L49L6R38R18L50R8R19L37L9R6R23L4R9L49R50R6L9R36L37L8L33R40L28R24L15L35L13L3R46L39R21R46L2R34L17L11L11L3L10R20R9R11R8L1L29R20L45R26R24R3R42L40L5L19L23L16L48R22L27R16R48R24R33L13R25L44L18L44L31L15R26R1L7R7L20L42L7R43L25L44L15R50L18L23L26R34R8L38L48R5R38L13L25L13L16L48L10R13R12L6L18R1L23R28L43L30L40R4R27R34L15L42R24R31L43R21L3R1L26R7R5R5L33R29R13R4R11R50L8R20R4L39R12R23L26R34L23L22R1L33R38L24R17R8R35R27R8R9L49R46R25R20R17L2R20L28L4R34R17L24L27R50L18L8L13L6L33L34L35L38L2R19L17R11L44R39R32R4L9L48L29L6R17R12R23R43R43R32R15R44R17R38R41R5R46R33L34R49L24L36R42L16L32L28R46L32L3L7L9R34L49R29L10R14R43R19R48L24R21R17R26R50R32L46R11L34L9L37L15L9L36R13R30R3R9L8R49L44L1R28L4R29L6L22L29L21R9L11R5R18R35R16R22L37L24R14L22L22R26L4R38L35R2R39L21L49R31R46R49L20L13R9R34L33R15L45R27L2R23L30R18L30L39L39L50L4R19R25L26L42L3L4R22R29R45L39L48L15L39L45L24R4R1L43L1L37L3R38R36R14L3L47L2R4L31L5R43L31L42R25L5L17R30R21L14R7R46L47R43L37L43R12R42R28L11R26L11L44L48L6L36L16R46L27L5L1L32L33L48R1L11L4L41L1L38L6R7R31R13R30R36R8R11R5R45R49L24R33R43L4R42L21R22R4R8L11R16L32R30L49R27L41L47L19R1L16R27L31R7L45R22L25L17L20L19L49R50R38R19R6R1R11R25L37R35L12L46R6R35L9L42L5L9R19L44R45L34L3L47L14R24R34R12L34R15R19R14R5R17R41R1R4L7L10R21R17L2L19R23R38R2L3L28L9L14L12L3R31L30R41R48L50R16L40L1L37L31R22L41L14R23R45L42R19R23L18R43R26L43L19R28L22R42L24R26R20R37R26L31R19L43R18L37L9L4L34R7L16L39R1L31R40L3L11L33R1R29L6R14L32R35R12R8R39R19R1R48R1R39L37L44L26L24L26R7R48L44R14L38L38R50L18R1R38L48R17L49L48R9R47R39L20R45L46L4L29R11L35R32R39L9R42L43L42R18R10R14R27R13R7L37R4L38L40R17L24L22R18L24L5L9L24L3R20L21R28L15L45L33R8R18L28R31L18L45R34R24L31R33R45R5L32L48L10L23R47R22R16L40L11R45R30R1R49L20R3R47L47L11R20L36R9R23L8R19L4L32L19L19R47R10L40L47R33L37R20R26R19L24L30L2R20L1R16R10L48R3R24L10L11R14R44L14R19L43L26L13R32L4R43L39L2R43L43R20L16L32R1L30L26R43L46L50R37L50R38L6R4R40R46L29R40R42R12L19L9R4L49L36R32R8L30R25R22R9L4L41L5R18L23L2R31R29R28L30R31R45L46L9L19R38L13L49R27L16L21R45R4L36R49L11L42L14L35R39R39L20R20L20L7R3L17L36R13R36L16R17R19L25L30R48L34L24L40R44L14R24L41R21L5L1R45L1R37R17R18L28R10L24R40R14L43R40R50R47R43R10L22L6R42L16R3L49L9R15L20R34R21L5L45L17L25L42R10L47R14L42R26L14R11L39L15R2R34L14L9R41R26R41R45R13L15R48L30L17R22R46L35R17L48L40L47L13R40L35L36L32R44R17R33L39R36L25L28L22L10R41R50R31L9R24R43R42L29R31R37L44L27R8R37R10R34R9L11L33R47L15L19L45L31R5R4R22L15R44L22R21L22L33R11L33L48R37R23R4L25L43R20L22L22R6R33L4R25R9L14R32R42R1R50R21L46R3L13L36L38R12L47R13L25R15L29R11R37L30L36R16L21L38L24L25L36R25R46R29R16R32R27R10R3L46L22R32R5R47L23L39L46R25L23R4R12R21R31R40L50R22R46L44L9L3R30R43L23R7R23R37R43R11R8R25L42L41L47R43L27L36L33L21R32L45R8R26L27R36L32L33R50R19R48L22L11L44R6L44R19L43R15R43R43L25L4R30R10L37L41L38L43L15R35R15L5R44L33L40R21L9R41R28R1L37L10R28L49L20R25R31L15R28L21R28R30L15R19R9R32R25L9L49R22R19R34R17L22R19L49R41L40L32R39L37L4L40R19L22R25L44R33R26L39L28R33R11R27R18R44R42R31R30R12L1L9L35L32L22L20L11L35R38L7L22R12R8R33L43L47R47R15R6L46L10L3R6R10L22R12L5R48L17R35R23R25L23L29R21R21R20L22R41L22L33R35R21L50L2L46R25R21L46R29L42R47R23L8L17L50L49L31L42R31L14L37R33L25L15L42L40L39L6R3L10L22R27L34L8R8R31R1L50R14L37R27R29R49R32R19R8L31L44R20R5L45L49R16L36R31L33L27L7L45L2L12R7R30R25L47L25L26R5L35L15R44R49L50L33L25R9R45L40L16R34R37L9L18L31R27R44L12L33R14R47R46R40R18R30R31R10L35L12L20R47R6L41L34L29L19L29L42L23R38R11R16L7L12R6R1R28L47R18L3L31R38L14R47L12R7L26R21L33R37L7L26R17L50L42R40R3L36R25R16L38L47R1L20R50L4L36L18R2R38L32R38L20R50L29L2R26R47L35R40L9L27L6R10R50R49R48R35R5R6R3R24R37L42L24L34R7L29L46L35L50L20R8L42L5L42L23R43R30R18R1R22R27L5L42L47R7L8R47R9R10R19R20R32R42R47R49L32R44R37L23L40R9R8L10L38L50R38R48R3R44R48R45L1L24L24L14L48R34L2L32R34L45L45R26L29R9R33L21R25L30L15R32R33R31R12R2R14R32L41R44R18L11R18L1R31L24L7L45L14L43R28L15L37L44R35R38R35R32L31L11R36L28R47L29R32L7L44L14L6R14R47R28R30L4R25R12L28R31R2R38R48L42L21L5R35L31R50L31R9R6R47L12R42L1R31L20L38R15L48R29R39L27R21R35L10R47L8R41R5R44R19L50R20L43R40R45R39L7L32L42R28L5L1R12R25L27R19L49L17R27R32L26L35R15R36L31R39L1R39R44L42L31R13L33L12R19R6L13L10L49R6R34L25L26R20R21L38R33L13L38L39L23R18L33R31R46L20L31L3L10R24L7R50R12R46R30L10R30R7L32L42L30L35L20R42R38R43R8L35R33L24L41L34L29L4L4R8R27L22L35L50L11R21R37R7R9R47L37L17R12R19L3R42L39L35L9R39L2R49L14R8L35L45L16L9R4R37L45R37L40L37R23R12R7L11L32L7L8L43L30R26R27R33L38L33L25L13R4L26R45L33L8L40L8R33R1R25R1R50R10L34L38L43L12R35R49L41R45R16L28R50L48R4L24L48L11R14L47L6L18L49R4R9R25L23R9L13L11R44L35L11R10R25L1R1R31L26L34R27L24R46L16R26L43L42R15L29R23L38R36L41R4R38R27R9R2L35L30R31L40L28R13R35L31R35R8R20R50L8R14R16L10L37R34R36L45L16R13R20L28R46R27L3R38R29R39L15R33L26L1R30L33L6R27R4L16R23R19R32L32L45R21R15R43L2R31R33R32L7L31L28L20R18R41L15L29"
steps = [int(x) for x in re.findall(r"[0-9]+", input_commands)]
turns = re.findall(r"[A-Z]", input_commands)
commands = [x for x in chain(*zip_longest(steps, turns)) if x is not None]


@dataclass
class Position:
    row: int
    col: int

    def up(self):
        self.row -= 1

    def down(self):
        self.row += 1

    def left(self):
        self.col -= 1

    def right(self):
        self.col += 1


class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"

    def turn(self, command):
        turn_right = {
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP,
            Direction.UP: Direction.RIGHT,
        }
        turn_left = {
            Direction.RIGHT: Direction.UP,
            Direction.UP: Direction.LEFT,
            Direction.LEFT: Direction.DOWN,
            Direction.DOWN: Direction.RIGHT,
        }
        if command == "R":
            return turn_right[self]
        elif command == "L":
            return turn_left[self]

    def move(self, graph, position, moves):
        if self == Direction.UP:
            for _ in range(moves):
                try:
                    new_position = Position(position.row-1, position.col)
                    space = graph[new_position.row][new_position.col]
                except IndexError:
                    new_position = Position(get_end(get_col(position.col, graph)), position.col)
                    space = graph[new_position.row][new_position.col]
                if space == '#':
                    return position
                if space == '.':
                    position = new_position
                if space == ' ':
                    new_position = Position(get_end(get_col(position.col, graph)), position.col)
                    if graph[new_position.row][new_position.col] == '#':
                        return position
                    position = new_position
            return position
        if self == Direction.DOWN:
            for _ in range(moves):
                try:
                    new_position = Position(position.row+1, position.col)
                    space = graph[new_position.row][new_position.col]
                except IndexError:
                    new_position = Position(get_start(get_col(position.col, graph)), position.col)
                    space = graph[new_position.row][new_position.col]
                if space == '#':
                    return position
                if space == '.':
                    position = new_position
                if space == ' ':
                    new_position = Position(get_start(get_col(position.col, graph)), position.col)
                    if graph[new_position.row][new_position.col] == '#':
                        return position
                    position = new_position
            return position
        if self == Direction.LEFT:
            for _ in range(moves):
                try:
                    new_position = Position(position.row, position.col-1)
                    space = graph[new_position.row][new_position.col]
                except IndexError:
                    new_position = Position(position.row, get_end(get_row(position.row, graph)))
                    space = graph[new_position.row][new_position.col]
                if space == '#':
                    return position
                if space == '.':
                    position = new_position
                if space == ' ':
                    new_position = Position(position.row, get_end(get_row(position.row, graph)))
                    if graph[new_position.row][new_position.col] == '#':
                        return position
                    position = new_position
            return position
        if self == Direction.RIGHT:
            for _ in range(moves):
                try:
                    new_position = Position(position.row, position.col+1)
                    space = graph[new_position.row][new_position.col]
                except IndexError:
                    new_position = Position(position.row, get_start(get_row(position.row, graph)))
                    space = graph[new_position.row][new_position.col]
                if space == '#':
                    return position
                if space == '.':
                    position = new_position
                if space == ' ':
                    new_position = Position(position.row, get_start(get_row(position.row, graph)))
                    if graph[new_position.row][new_position.col] == '#':
                        return position
                    position = new_position
            return position

def get_row(i, graph):
    return graph[i]

def get_col(j, graph):
    return [graph[i][j] for i in range(len(graph))]

def get_start(l):
    for i in range(len(l)):
        if l[i] == " ":
            continue
        return i

def get_end(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] == " ":
            continue
        return i

def build_graph(input):
    max_length = 0
    for line in input:
        max_length = max(max_length, len(line.strip("\n")))

    graph = [[" " for _ in range(max_length)] for __ in input]

    for row in range(len(graph)):
        for col in range(max_length):
            try:
                graph[row][col] = input[row].strip("\n")[col]
            except IndexError:
                continue
    return graph

graph = build_graph(input)

for j in range(len(graph[0])):
    if graph[0][j] == ".":
        start = j
        break


def traverse(graph=graph, commands=commands, facing=Direction.RIGHT, position=Position(0, start)):
    for command in commands:
        if isinstance(command, int):
            position = facing.move(graph, position, command)
            print(position)
        else:
            facing = facing.turn(command)
            print(facing)

# part 1
traverse()


