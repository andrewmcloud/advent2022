import re
with open("resources/day15.txt") as f:
    input = [re.findall(r"-?\d+", line) for line in f.readlines()]


def coords_from_input_line(line: list[str]):
    ints = [int(num) for num in line]
    x, y, xx, yy = ints
    return (x, y), (xx, yy)


def manhattan(sensor: tuple[int, int], beacon: tuple[int, int]):
    x, y = sensor
    xx, yy = beacon
    return abs(x - xx) + abs(y - yy)


def solve(coord_pairs: tuple, row: list[int], range_min: int, range_max: int, row_index: int):
    sensor, beacon = coord_pairs
    sensor_to_beacon = manhattan(sensor, beacon)
    for x in range(range_min, range_max):
        if manhattan(sensor, (x, row_index)) <= sensor_to_beacon:
            if beacon[0] == x and beacon[1] == row_index:
                row[x-range_min] = 0
            else:
                row[x-range_min] = 1
    return row


range_min = float('inf')
range_max = -(float('inf'))
for line in input:
    sensor, beacon = coords_from_input_line(line)
    distance = manhattan(sensor, beacon)
    range_min = min(range_min, sensor[0] - distance)
    range_max = max(range_max, sensor[0] + distance)

row = [0 for _ in range(range_min, range_max)]
for line in input:
    row = solve(coords_from_input_line(line), row, range_min, range_max, 2000000)
print(sum(row))
