from dataclasses import dataclass, field
from math import prod
import re
with open("resources/day11.txt") as f:
    input = [instruction.split("\n") for instruction in f.read().split("\n\n")]


@dataclass
class Monkey:
    id: int
    items: list[int]
    multiplier: int
    adder: int
    test_factor: int
    throw_true: int
    throw_false: int
    inspections: int = field(default=0)


@dataclass
class Troop:
    monkey_lookup: dict[int, Monkey]
    monkeys: list

    @property
    def modulo(self) -> int:
        return prod(monkey.test_factor for monkey in self.monkeys)

    def add_monkey(self, monkey: Monkey) -> None:
        self.monkeys.append(monkey)
        self.monkey_lookup[monkey.id] = monkey

    def get_monkey(self, id: int) -> Monkey:
        return self.monkey_lookup[id]

    def throw_items(self, monkey: Monkey, divisor: int) -> None:
        for item in monkey.items:
            monkey.inspections += 1
            if monkey.multiplier == -1:
                worry_level = ((item * item + monkey.adder) % self.modulo) // divisor
            else:
                worry_level = ((item * monkey.multiplier + monkey.adder) % self.modulo) // divisor
            if worry_level % monkey.test_factor == 0:
                self.get_monkey(monkey.throw_true).items.append(worry_level)
            else:
                self.get_monkey(monkey.throw_false).items.append(worry_level)
        monkey.items.clear()

    def inspections(self) -> int:
        most = sorted((monkey.inspections for monkey in self.monkeys), reverse=True)
        return most[0] * most[1]


def create_troop_from_input(input) -> Troop:
    troop = Troop(dict(), [])
    for monkey in input:
        adder = 0
        multiplier = 1
        [id] = re.findall(r"\d+", monkey[0])
        items = [int(x) for x in re.findall(r"\d+", monkey[1])]
        [test_factor] = re.findall(r"\d+", monkey[3])
        [throw_true] = re.findall(r"\d+", monkey[4])
        [throw_false] = re.findall(r"\d+", monkey[5])
        if re.findall(r"\+", monkey[2]):
            [adder] = re.findall(r"\d+", monkey[2])
        else:
            if re.findall(r"\d+", monkey[2]):
                [multiplier] = re.findall(r"\d+", monkey[2])
            else:
                multiplier = -1
        troop.add_monkey(
            Monkey(
                id=int(id),
                items=items,
                multiplier=int(multiplier),
                adder=int(adder),
                test_factor=int(test_factor),
                throw_true=int(throw_true),
                throw_false=int(throw_false)
            )
        )
    return troop


def play(troop: Troop, iterations: int, divisor: int) -> Troop:
    for _ in range(iterations):
        for monkey in troop.monkeys:
            troop.throw_items(monkey, divisor)
    return troop


#part 1
print(play(create_troop_from_input(input), 20, 3).inspections())
# part 2
print(play(create_troop_from_input(input), 10000, 1).inspections())
