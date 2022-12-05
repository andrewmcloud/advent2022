with open("resources/day3.txt") as f:
    rucksacks = f.read().strip().split("\n")

priority = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def chunk(s: str) -> tuple[str, str]:
    half = len(s)//2
    return s[:half], s[half:]


def part1(rucks: list[str]) -> int:
    total = 0
    for ruck in rucks:
        compartment1, compartment2 = chunk(ruck)
        total += priority.index((set(compartment1) & set(compartment2)).pop())
    return total


def part2(rucks: list[str]) -> int:
    if rucks and len(rucks) >= 3:
        elf1, elf2, elf3 = rucks[:3]
        return priority.index((set(elf1) & set(elf2) & set(elf3)).pop()) + part2(rucks[3:])
    return 0


# part 1
print(part1(rucksacks))
# part 2
print(part2(rucksacks))

