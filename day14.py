with open("resources/day14.txt") as f:
    lines = [point.strip().split(" -> ") for point in f.readlines()]
    rock_paths = []
    for line in lines:
        rock_path = []
        for point in line:
            x, y = point.split(",")
            rock_path.append((int(x), int(y)))
        rock_paths.append(rock_path)


def init_obstacles(rock_paths: list[list[tuple[int, int]]]):
    obstacles = set()
    for rock_path in rock_paths:
        for i in range(len(rock_path) - 1):
            x, y = rock_path[i]
            xx, yy = rock_path[i+1]
            if x == xx:
                obstacles.update([(x, j) for j in range(y, yy+1)])
                obstacles.update([(x, j) for j in range(yy, y+1)])

            else:
                obstacles.update([(j, y) for j in range(x, xx+1)])
                obstacles.update([(j, y) for j in range(xx, x+1)])

    return obstacles


def move(current: tuple[int, int], direction: tuple[int, int]):
    x, y = current
    xx, yy = direction
    return x + xx, y + yy


def is_unobstructed(floor: bool, threshold: int, obstructions: set[tuple[int, int]], next_position: tuple[int, int]):
    if floor:
        return next_position not in obstructions and next_position[1] < threshold
    return next_position not in obstructions


def drop_sand(start: tuple[int, int], obstructions: set[tuple[int, int]], threshold: int, floor: bool = False):
    directions = [(0, 1), (-1, 1), (1, 1)]
    unobstructed = True
    current = start
    while unobstructed:
        unobstructed = False
        for direction in directions:
            next_position = move(current, direction)
            if is_unobstructed(floor, threshold, obstructions, next_position):
                current = next_position
                unobstructed = True
                break
        if next_position[1] > threshold:
            return None
    if current == start:
        return None
    return current


def pour_sand(obstacles: set[tuple[int, int]], floor: bool = False):
    threshold = max(y for _, y in obstacles)
    count = 1 if floor else 0
    while True:
        if landed := drop_sand((500, 0), obstacles, threshold + 2, floor):
            obstacles.add(landed)
            count += 1
        else:
            break
    return count


# part 1
print(pour_sand(init_obstacles(rock_paths)))
# part 2
print(pour_sand(init_obstacles(rock_paths), True))
