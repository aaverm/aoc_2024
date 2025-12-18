import argparse
import operator
from functools import reduce

import numpy as np


def parse_file_part1(file_path: str) -> tuple[list[list[int]], list[str]]:
    elements = []
    operations = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if "+" in line or "*" in line:
            operations = line.split()
        elif line:
            numbers = line.split()
            elements.append([int(num) for num in numbers])

    return elements, operations


def part1(file_path: str) -> int:
    elements, operations = parse_file_part1(file_path)
    elements_transposed = list(map(list, zip(*elements)))

    ops = {"+": operator.add, "*": operator.mul}
    cumsum = 0

    for e, op in zip(elements_transposed, operations):
        result = reduce(ops[op], e)
        cumsum += result

    return cumsum


def parse_file_part2(file_path: str) -> tuple[np.ndarray, list[str]]:
    grid = []
    operations = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "+" in line or "*" in line:
            operations = line.split()
        else:
            grid.append(list(line.replace("\n", "")))

    return np.array(grid), operations


def part2(file_path: str) -> int:
    grid, operations = parse_file_part2(file_path)

    cols_all_spaces = np.where(np.all(grid == " ", axis=0))[0]

    combined_elements = []
    start_idx = 0
    for col_idx in cols_all_spaces:
        if start_idx < col_idx:
            elements_block = grid[:, start_idx:col_idx].T
            combined_elements.append(
                [int("".join(row).strip()) for row in elements_block]
            )
        start_idx = col_idx + 1
    if start_idx < grid.shape[1]:
        combined_elements.append(
            [int("".join(row).strip()) for row in grid[:, start_idx:].T]
        )

    ops = {"+": operator.add, "*": operator.mul}
    cumsum = 0

    for e, op in zip(combined_elements, operations):
        result = reduce(ops[op], e)
        cumsum += result

    return cumsum


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 6")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
