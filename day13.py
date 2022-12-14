from functools import cmp_to_key
from math import prod
with open("resources/day13.txt") as f:
    pairs = f.read().strip().split("\n\n")


class Pass(Exception):
    ...


class Fail(Exception):
    ...


def is_ordered(packet1, packet2):
    for first, second in zip(packet1, packet2):
        if isinstance(first, int) and isinstance(second, int):
            if first < second:
                raise Pass
            if first > second:
                raise Fail
        if isinstance(first, int) and isinstance(second, list):
            if not is_ordered([first], second):
                return False
        if isinstance(first, list) and isinstance(second, int):
            if not is_ordered(first, [second]):
                return False
        if isinstance(first, list) and isinstance(second, list):
            if not is_ordered(first, second):
                return False
    if len(packet1) < len(packet2):
        raise Pass
    if len(packet1) > len(packet2):
        raise Fail
    return True


def compare(p1: list[list | int], p2: list[list | int]):
    if p1 == p2:
        return 0
    try:
        if is_ordered(p1, p2):
            return -1
    except Pass:
        return -1
    except Fail:
        return 1
    return 1


# part 1
answer = 0
for i, pair in enumerate(pairs):
    p1, p2 = pair.split("\n")
    first, second = eval(p1), eval(p2)
    try:
        if is_ordered(first, second):
            answer += i+1
    except Pass:
        answer += i+1
    except Fail:
        continue
print(answer)

# part 2
packets = []
divider_indices = []
for pair in pairs:
    p1, p2 = pair.split("\n")
    packets.extend([eval(p1), eval(p2)])
packets.extend([[[2]], [[6]]])
sorted_packets = sorted(packets, key=cmp_to_key(compare))
for i, packet in enumerate(sorted_packets):
    if packet == [[2]] or packet == [[6]]:
        divider_indices.append(i+1)
print(prod(divider_indices))
