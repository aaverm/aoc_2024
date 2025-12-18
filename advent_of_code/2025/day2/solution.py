import argparse
import numpy as np


def parse_file(file_path: str) -> list[str]:
    ranges = []
    with open(file_path, "r", encoding="utf-8") as file:
        row = file.readline().strip()
        entries = row.split(",")

        for entry in entries:
            parts = entry.split("-")
            if len(parts) == 2:
                try:
                    start = int(parts[0])
                    end = int(parts[1])
                    ranges.append(np.arange(start, end + 1))
                except ValueError:
                    print(f"Skipping invalid entry: {entry}")

    return list(np.concatenate(ranges).astype(str))


def part1(file_path: str) -> int:
    ranges = parse_file(file_path)

    invalid_id_sum = 0
    for id_str in ranges:
        length = len(id_str)
        half_point = length // 2
        if length % 2 == 0 and id_str[:half_point] == id_str[half_point:]:
            invalid_id_sum += int(id_str)

    return invalid_id_sum


def is_repetitive(s: str) -> bool:
    n_chars = len(s)
    if len(set(s)) == 1 and n_chars > 1:
        return True

    pi = [0] * n_chars
    j = 0
    for i in range(1, n_chars):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    period = n_chars - pi[-1]
    return period < n_chars and n_chars % period == 0


def part2(file_path: str) -> int:
    ranges = parse_file(file_path)

    invalid_id_sum_revised = 0
    for id_str in ranges:
        if is_repetitive(id_str):
            invalid_id_sum_revised += int(id_str)

    return invalid_id_sum_revised


def main() -> None:

    parser = argparse.ArgumentParser(description="AoC 2025 Day 2")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
