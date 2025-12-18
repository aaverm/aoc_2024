import argparse
import numpy as np
from collections import deque


def read_text_file_as_grid(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return np.array(grid)


def count_adjacent_at_signs(grid: np.ndarray, x: int, y: int) -> int:
    rows, cols = grid.shape
    count = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "@":
                count += 1
    return count


def part1(file_path: str) -> int:
    grid = read_text_file_as_grid(file_path)
    rows, cols = grid.shape
    mark_counter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == "@":
                neighbors = count_adjacent_at_signs(grid, i, j)
                if neighbors < 4:
                    grid[i][j] = "X"
                    mark_counter += 1

    return mark_counter


def part2(file_path: str) -> int:
    grid = read_text_file_as_grid(file_path)
    rows, cols = grid.shape
    mark_counter = 0

    at_coords = np.where(grid == "@")
    queue = deque(zip(at_coords[0], at_coords[1]))

    while True:
        if not queue:
            break

        current_round = list(queue)
        queue.clear()

        to_change = []
        for x, y in current_round:
            if grid[x][y] != "@":
                continue
            neighbors = count_adjacent_at_signs(grid, x, y)
            if neighbors < 4:
                to_change.append((x, y))

        if not to_change:
            break

        for x, y in to_change:
            grid[x][y] = "X"
            mark_counter += 1

        seen = set()
        for x, y in to_change:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == "@" and (nx, ny) not in seen:
                            queue.append((nx, ny))
                            seen.add((nx, ny))

    return mark_counter


def main() -> None:

    parser = argparse.ArgumentParser(description="AoC 2025 Day 4")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
