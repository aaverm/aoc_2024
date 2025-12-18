import argparse
import numpy as np


def read_text_file_as_grid(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        grid = [list(line.strip()) for line in file if line.strip()]
    return np.array(grid)


def is_inside_grid(grid: np.ndarray, x: int, y: int) -> bool:
    rows, cols = grid.shape
    return 0 <= x < rows and 0 <= y < cols


def run_simulation(grid: np.ndarray) -> tuple[int, np.ndarray]:
    """Simulates the agent's movement iteratively to mark visited spots and count splits."""
    delta = {">": (0, 1), "v": (1, 0), "<": (0, -1)}

    start_x, start_y = np.argwhere(grid == "S")[0]
    start_direction = "v"

    stack = [(start_x, start_y, start_direction)]
    visited = set()
    split_counter = 0

    while stack:
        x, y, direction = stack.pop()

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        if grid[x][y] == ".":
            grid[x][y] = "|"

        dx, dy = delta[direction]
        nx, ny = x + dx, y + dy

        if is_inside_grid(grid, nx, ny):
            if grid[nx][ny] == "^":
                split_counter += 1
                for split_dir in ("<", ">"):
                    split_dx, split_dy = delta[split_dir]
                    nnx, nny = nx + split_dx, ny + split_dy

                    if is_inside_grid(grid, nnx, nny) and grid[nnx][nny] != "^":
                        stack.append((nnx, nny, "v"))
            else:
                stack.append((nx, ny, direction))

    return split_counter, grid


def count_paths(grid: np.ndarray) -> int:
    rows, cols = grid.shape
    dp = np.zeros((rows, cols), dtype=int)

    sx, sy = np.argwhere(grid == "S")[0]
    dp[sx][sy] = 1

    for x in range(sx, rows - 1):
        for y in range(cols):
            if dp[x][y] == 0:
                continue

            if grid[x + 1][y] in ["|", "."]:
                dp[x + 1][y] += dp[x][y]
                continue

            if grid[x + 1][y] == "^":
                if y + 1 < cols and grid[x + 1][y + 1] == "|":
                    dp[x + 1][y + 1] += dp[x][y]
                if y - 1 >= 0 and grid[x + 1][y - 1] == "|":
                    dp[x + 1][y - 1] += dp[x][y]

    result = int(sum(dp[rows - 1][c] for c in range(cols)))
    return result


def part1(file_path: str) -> int:
    grid = read_text_file_as_grid(file_path)
    split_counter, _ = run_simulation(grid)
    return split_counter


def part2(file_path: str) -> int:
    grid = read_text_file_as_grid(file_path)
    _, final_grid = run_simulation(grid)
    return count_paths(final_grid)


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 7")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
