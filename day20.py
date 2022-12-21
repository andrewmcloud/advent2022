from __future__ import annotations
from dataclasses import dataclass, field
from typing import Final

with open("resources/day20.txt") as f:
    input = [int(x) for x in f.read().split("\n")]

ENCRYPTION_KEY: Final = 811589153


@dataclass
class Node:
    value: int
    encrypted: int = field(default=None)
    prev: Node = field(default=None, init=False)
    next: Node = field(default=None, init=False)


class Circular:
    nodes = []
    start: Node

    def __init__(self, nodes: list[int], encrypted=False):
        if encrypted:
            self.nodes = [Node(node*ENCRYPTION_KEY % (len(nodes)-1), node*ENCRYPTION_KEY) for node in nodes]
        else:
            self.nodes = [Node(node) for node in nodes]
        self.start = self.nodes[0]
        end = self.nodes[-1]
        for i in range(len(self.nodes) - 1):
            node1 = self.nodes[i]
            node2 = self.nodes[i+1]
            node1.next = node2
            node2.prev = node1
        self.start.prev = end
        end.next = self.start

    def move(self, node):
        # move right node.value steps
        if node.value > 0:
            self.remove(node)
            new_location = self.walk(node, node.value)
            next = new_location.next
            node.next = next
            new_location.next = node
            node.prev = new_location
            next.prev = node

        # move left node.value steps
        if node.value < 0:
            self.remove(node)
            new_location = self.walk(node, node.value)
            prev = new_location.prev
            node.prev = prev
            new_location.prev = node
            node.next = new_location
            prev.next = node

    def mix(self):
        for node in self.nodes:
            self.move(node)

    def print(self):
        s = ""
        node = self.start
        s += f" {node.value} |"
        node = node.next
        while node != self.start:
            s += f"{node.value} | "
            node = node.next
        return s

    def remove(self, node: Node) -> None:
        try:
            node.next.prev = node.prev
            node.prev.next = node.next
        except AttributeError:
            print(f"{node} does not exist in list.")

    def walk(self, start: Node, steps: int):
        node = start
        if steps > 0:
            for _ in range(steps):
                node = node.next
        elif steps < 0:
            for _ in range(abs(steps)):
                node = node.prev
        return node

    def get_zero_node(self):
        for node in self.nodes:
            if node.value == 0:
                return node


def solve():
    solution = {}
    llist = Circular(input)
    llist.mix()
    start = llist.get_zero_node()
    one_thousand = llist.walk(start, 1000).value
    two_thousand = llist.walk(start, 2000).value
    three_thousand = llist.walk(start, 3000).value
    solution["part1"] = one_thousand + two_thousand + three_thousand

    llist = Circular(input, encrypted=True)
    for _ in range(10):
        llist.mix()
    start = llist.get_zero_node()
    one_thousand = llist.walk(start, 1000).encrypted
    two_thousand = llist.walk(start, 2000).encrypted
    three_thousand = llist.walk(start, 3000).encrypted
    solution["part2"] = one_thousand + two_thousand + three_thousand
    return solution


solution = solve()
# part 1
print(solution["part1"])

# part 2
print(solution["part2"])
