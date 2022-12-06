with open("resources/day6.txt") as f:
    input = f.read().strip()


def sliding_window(input: str, window_size: int) -> int:
    for i in range(len(input) - window_size):
        marker = input[i:i+window_size]
        if len(set(marker)) == window_size:
            return i+window_size


# part 1
print(sliding_window(input, 4))
# part 2
print(sliding_window(input, 14))
