from textwrap import wrap
with open("resources/day10.txt") as f:
    instructions = [line.strip() for line in f.readlines()]


def draw_pixel(cycle: int, sprite_center: int) -> str:
    if cycle % 40 in {sprite_center - 1, sprite_center, sprite_center + 1}:
        return "#"
    return "."


def solve(instructions: list[str]) -> tuple[list[int], str]:
    cycles = [1]
    sprite = 1
    crt = ""
    for instruction in instructions:
        cycle = len(cycles) - 1
        match instruction.split():
            case["noop"]:
                crt += draw_pixel(cycle, sprite)
                cycles.append(cycles[-1])
                sprite = cycles[-1]
            case["addx", value]:
                last = cycles[-1]
                crt += draw_pixel(cycle, sprite)
                crt += draw_pixel(cycle + 1, sprite)
                cycles += [last, last + int(value)]
                sprite = cycles[-1]
    return cycles, crt


cycles, crt = solve(instructions)
# part 1
print(sum(cycles[cycle - 1] * cycle for cycle in [20, 60, 100, 140, 180, 220]))
# part 2
print("\n".join(wrap(crt, 40)))
