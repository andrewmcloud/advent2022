from dataclasses import dataclass
import re

with open("resources/day16.txt") as f:
    input = f.readlines()

parser = re.compile(r"Valve (.+) has flow rate=(\d+);.+valves? (.+)")


@dataclass
class Valve:
    pressure: int
    neighbors: list[str]


@dataclass(frozen=True)
class Edge:
    node: str
    other: str


def build_graph(input):
    graph = {}
    for line in input:
        groups = re.match(parser, line)
        key = groups[1]
        pressure = groups[2]
        valves = groups[3]
        graph[key] = Valve(pressure=int(pressure), neighbors=valves.split(", "))
    return graph


def non_zero_pressure_valves(graph):
    return {valve for valve in graph if graph[valve].pressure != 0}


def calculate_edge_costs(graph, vertexes, distances, current_valve, depth):
    neighbors = set()
    for vertex in vertexes:
        for valve in graph[vertex].neighbors:
            edge = Edge(current_valve, valve)
            if edge in distances:
                continue
            distances[edge] = depth
            neighbors.add(valve)
    return neighbors


def build_edge_distances_map(graph, start):
    distances = {}
    vertexes = set()
    non_zero_valves = non_zero_pressure_valves(graph)
    for valve in graph:
        if valve in non_zero_valves or valve == start:
            depth = 0
            vertexes.add(valve)
            distances[Edge(valve, valve)] = 0
            while vertexes:
                depth += 1
                vertexes = calculate_edge_costs(graph, vertexes, distances, valve, depth)
    return distances


def traverse(distances, valves, visited, start, seconds):
    visited.add(start)
    max_pressure = 0
    for valve in valves:
        if valve in visited:
            continue
        edge = Edge(start, valve)
        time_remaining = seconds - (distances[edge] + 1)  # one unit time to visit, one unit time to open
        if time_remaining > 0:
            pressure = graph[valve].pressure * time_remaining
            # python is crazy and mutates everything, create a new set from visited, so it isn't shared!
            pressure += traverse(distances, valves, set(visited), valve, time_remaining)
            max_pressure = max(pressure, max_pressure)
    return max_pressure


# part 1
graph = build_graph(input)
edge_distances = build_edge_distances_map(graph, "AA")
non_zero_valves = non_zero_pressure_valves(graph)
print(traverse(edge_distances, non_zero_valves, set(), "AA", 30))
