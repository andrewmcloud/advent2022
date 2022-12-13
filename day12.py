from collections import deque
with open("resources/day12.txt") as f:
    map = [[line for line in lines.strip()] for lines in f.readlines()]


def find_starts(elevation_map: list[list[str]]) -> list[tuple[int, int]]:
    starts = []
    for x in range(len(elevation_map)):
        for y in range(len(elevation_map[0])):
            if elevation_map[x][y] == 'a':
                starts.append((x, y))
    return starts


def get_neighbors(x: int, y: int) -> list[tuple[int, int]]:
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


def is_valid_step(visited: set, elevation_map: list[list[str]], elevation: str, x: int, y: int) -> bool:
    elevation = 'a' if elevation == 'S' else elevation
    if 0 <= x < len(elevation_map) and 0 <= y < len(elevation_map[0]):
        next_elevation = elevation_map[x][y]
        if next_elevation == 'E' and (elevation == 'z' or elevation == 'y'):
            return True
        if (ord(next_elevation) - ord(elevation)) <= 1 and next_elevation != 'E':
            if (x, y) in visited:
                return False
            return True
    return False


def find_path(elevation_map: list[list[str]], start: tuple[int, int], goal: str) -> list[tuple[int, int]]:
    queue = deque([[start]])
    seen = set(start)
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        elevation = elevation_map[x][y]
        if elevation_map[x][y] == goal:
            return path[:-1]  # don't count E
        for xx, yy in get_neighbors(x, y):
            if is_valid_step(seen, elevation_map, elevation, xx, yy):
                queue.append(path + [(xx, yy)])
                seen.add((xx, yy))


# part 1
print(len(find_path(map, (20, 0), 'E')))

# part 2
shortest = float('inf')
for start in find_starts(map):
    path = find_path(map, start, 'E')
    if path:
        shortest = min(shortest, len(path))
print(shortest)
