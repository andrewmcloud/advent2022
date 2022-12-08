from functools import reduce
with open("resources/day8.txt") as f:
    forest = [[int(tree) for tree in line] for line in f.read().strip().split("\n")]


def is_tallest(height: int, treeline: list[int]):
    return all(height > tree for tree in treeline)


def count_boundary_trees(forest: list[list[int]]):
    return (len(forest) * len(forest[1])) - ((len(forest)-2) * (len(forest[1])-2))


def calculate_view(height: int, treeline: list[int]):
    count = 0
    for tree in treeline:
        if height > tree:
            count += 1
        elif height <= tree:
            return count + 1
    return count


def get_col(index: int, forest: list[list[int]]):
    return [row[index] for row in forest]


def count_visible_trees(forest: list[list[int]]):
    total_visible = []
    for row in range(1, len(forest) - 1):
        for col in range(1, len(forest[1]) - 1):
            tree_height = forest[row][col]
            look_left = forest[row][:col]
            look_right = forest[row][col+1:]
            look_up = get_col(col, forest)[:row]
            look_down = get_col(col, forest)[row+1:]
            views = [look_left, look_right, look_up, look_down]
            total_visible.append(any(is_tallest(tree_height, view) for view in views))
    return total_visible.count(True) + count_boundary_trees(forest)


def calculate_scenic_score(forest: list[list[int]]) -> int:
    best_view = 0
    for row in range(len(forest)):
        for col in range(len(forest[0])):
            tree_height = forest[row][col]
            look_left = forest[row][:col][::-1]
            look_right = forest[row][col + 1:]
            look_up = get_col(col, forest)[:row][::-1]
            look_down = get_col(col, forest)[row + 1:]
            views = [look_left, look_right, look_up, look_down]
            current_view = reduce(lambda x, y: x * y, [calculate_view(tree_height, view) for view in views])
            best_view = max(best_view, current_view)
    return best_view


# part 1
print(count_visible_trees(forest))
# part 2
print(calculate_scenic_score(forest))
