import argparse
import heapq
import numpy as np
from collections import defaultdict, deque


def read_text_file_as_grid(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        grid = [np.array(line.strip().split(",")).astype(float) for line in file if line.strip()]
    return np.array(grid)


def calc_euc_dist(point1: np.ndarray, point2: np.ndarray) -> float:
    return float(np.linalg.norm(np.array(point1) - np.array(point2)))


def get_top_n_closest_pairs(grid: np.ndarray, n: int):
    pq = []
    n_pairs = min(n, 1000)
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            p = tuple(float(x) for x in grid[i])
            q = tuple(float(x) for x in grid[j])
            distance = calc_euc_dist(p, q)
            heapq.heappush(pq, (distance, (p, q)))

    return heapq.nsmallest(n_pairs, pq)


def construct_connected_nodes(pairs) -> list[set[tuple[float]]]:
    graph = defaultdict(set)

    for p, q in pairs:
        graph[p].add(q)
        graph[q].add(p)

    visited = set()
    components = []

    for node in graph:
        if node in visited:
            continue

        queue = deque([node])
        group = set()

        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            group.add(cur)

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    queue.append(neighbor)

        components.append(group)

    return components


def part1(file_path: str) -> float:
    grid = read_text_file_as_grid(file_path)
    top_n = get_top_n_closest_pairs(grid, n=1000)
    _, pairs = zip(*top_n)
    list_connected_nodes = sorted(construct_connected_nodes(list(pairs)), key=len, reverse=True)

    circuits = 1
    for circuit in list_connected_nodes[:3]:
        circuits *= len(circuit)
    return circuits


def part2(file_path: str) -> float:
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 8")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
