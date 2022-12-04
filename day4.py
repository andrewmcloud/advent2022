with open("resources/day4.txt") as f:
    input = f.read().strip().split("\n")


def build_range_set(r1: str, r2: str) -> tuple[set[int]]:
    def parser(x): return [int(x) for x in x.split("-")]
    def set_builder(x): return{x for x in range(x[0], x[1] + 1)}
    return set_builder(parser(r1)), set_builder(parser(r2))


def play(camps: list[str]) -> dict[str, int]:
    contained_ranges = 0
    any_overlaps = 0
    for camp in camps:
        elf1, elf2 = build_range_set(*camp.split(","))
        if len(elf1 & elf2) == len(elf1) or len(elf1 & elf2) == len(elf2):
            contained_ranges += 1
        if elf1 & elf2:
            any_overlaps += 1
    return {"part1": contained_ranges, "part2": any_overlaps}


results = play(input)
print(results["part1"])
print(results["part2"])
