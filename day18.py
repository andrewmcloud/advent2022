from dataclasses import dataclass

with open("resources/day18.txt") as f:
    input = f.readlines()


@dataclass(frozen=True)
class Coord:
    x: int
    y: int
    z: int

    def adjacent(self, other) -> bool:
        adjacent_coords = {
            Coord(self.x + 1, self.y, self.z),
            Coord(self.x - 1, self.y, self.z),
            Coord(self.x, self.y + 1, self.z),
            Coord(self.x, self.y - 1, self.z),
            Coord(self.x, self.y, self.z + 1),
            Coord(self.x, self.y, self.z - 1),
        }
        return other in adjacent_coords

coords = [Coord(*map(int, line.strip().split(","))) for line in input]

total = 0
for coord in coords:
    for x in coords:
        if coord.adjacent(x):
            total += 1

print(len(coords) * 6 - total)
