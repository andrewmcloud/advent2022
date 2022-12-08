from collections import defaultdict
from typing import final
with open("resources/day7.txt") as f:
    commands = f.read().strip().split("\n")

MAX_DIRECTORY_SIZE: final = 100000
FILE_SYSTEM_SIZE: final = 70000000
SYSTEM_UPDATE_SIZE: final = 30000000


def accumulate_dir_size(directory_size_map: dict, current_path: list[str], size: int) -> None:
    if current_path:
        directory_size_map["/".join(current_path)] += int(size)
        accumulate_dir_size(directory_size_map, current_path[:-1], size)
    return


def make_directory_size_mapping(commands: list[str]) -> dict[str, int]:
    directory_size_map = defaultdict(int)
    current_path = []

    for command in commands:
        match command.split():
            # `$ cd ..` must be first case because `$ cd dir` also matches this pattern.
            case['$', 'cd', '..']:
                current_path.pop()
            case['$', 'cd', directory]:
                current_path.append(directory) if directory != "/" else current_path.append("~")
            # discard all other cases besides files
            case['$' | 'dir', _]:
                continue
            case[size, _]:
                accumulate_dir_size(directory_size_map, current_path, size)
    return directory_size_map


size_map = make_directory_size_mapping(commands)
sizes = size_map.values()
root_size = size_map["~"]

# part 1
print(sum([size for size in sizes if size <= MAX_DIRECTORY_SIZE]))
# part 2
print(min(size for size in sizes if size + (FILE_SYSTEM_SIZE - root_size) >= SYSTEM_UPDATE_SIZE))
