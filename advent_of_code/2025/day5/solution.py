import argparse

from intervaltree import IntervalTree


def parse_file(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ids = []

    with open(file_path, "r") as file:
        lines = file.readlines()

    after_empty_line = False

    for line in lines:
        line = line.strip()

        if not line:
            after_empty_line = True
            continue

        if not after_empty_line:
            if "-" in line:
                key, value = line.split("-")
                ranges.append((int(key), int(value)))
        else:
            ids.append(int(line))

    return ranges, ids


def part1(file_path: str) -> int:
    ranges, ids = parse_file(file_path)

    fresh_counter = 0
    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                fresh_counter += 1
                break

    return fresh_counter


def part2(file_path: str) -> int:
    ranges, _ = parse_file(file_path)

    tree = IntervalTree()
    remaining_points = []
    for start, end in ranges:
        if start == end:
            remaining_points.append(start)
            continue
        tree[start:end+1] = True

    tree.merge_overlaps()

    element_count = sum(int(end) - int(begin) for begin, end, _ in tree)

    for p in remaining_points:
        if not tree.at(p):
            element_count += 1

    return element_count


def main() -> None:

    parser = argparse.ArgumentParser(description="AoC 2025 Day 5")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
