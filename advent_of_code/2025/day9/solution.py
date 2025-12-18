import argparse
import numpy as np


def read_text_file_as_grid(file_path: str) -> np.ndarray:
    with open(file_path, "r") as file:
        grid = [
            np.array(line.strip().split(",")).astype(float)
            for line in file
            if line.strip()
        ]
    return np.array(grid)


def select_k_far_candidates(points: np.ndarray, k: int = 50) -> list[tuple[float, float]]:
    pts = [tuple(p) for p in points]
    pts_by_x = sorted(pts, key=lambda p: p[0])
    left = pts_by_x[:k]
    right = pts_by_x[-k:]

    pts_by_y = sorted(pts, key=lambda p: p[1])
    bottom = pts_by_y[:k]
    top = pts_by_y[-k:]

    candidates = list({p for p in (left + right + bottom + top)})
    return candidates


def compute_max_area(points: list[tuple[float, float]]) -> tuple[float, tuple[int, int]]:
    n = len(points)
    best_area: float = 0.0
    best_pair: tuple[int, int] = (0, 0)

    for i in range(n - 1):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > best_area:
                best_area = area
                best_pair = (i, j)

    return best_area, best_pair


def part1(file_path: str) -> int:
    grid = read_text_file_as_grid(file_path)
    candidates = select_k_far_candidates(grid, k=200)
    best_area, _ = compute_max_area(candidates)
    return int(round(best_area))


def part2(file_path: str) -> int:
    pass


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 9")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
