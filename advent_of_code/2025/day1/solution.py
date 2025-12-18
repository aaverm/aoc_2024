import argparse


def parse_file(file_path: str) -> tuple[list[str], list[int]]:
    directions = []
    steps = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            line = row.strip()

            if len(line) < 2:
                print(f"Skipping invalid line: {line}")
                continue

            try:
                directions.append(line[0])
                steps.append(int(line[1:]))
            except ValueError:
                print(f"Skipping line with non-integer steps: {line}")

    return directions, steps


def part1(file_path: str) -> int:
    directions, steps = parse_file(file_path)

    position = 50
    count_zeros = 0

    for d, s in zip(directions, steps):
        move = s if d == "R" else -s
        position = (position + move) % 100
        if position == 0:
            count_zeros += 1

    return count_zeros


def count_turns(
    directions: list[str], steps: list[int], start_position: int = 50, mod: int = 100
) -> int:
    position = start_position
    turns = 0

    for d, s in zip(directions, steps):
        move = s if d == "R" else -s

        full_turns = abs(move) // mod
        if full_turns > 0:
            turns += full_turns

        remainder = move % mod if move >= 0 else -((-move) % mod)
        end_pos = (position + move) % mod

        if remainder != 0:
            if move > 0 and end_pos < position and position != 0 and end_pos != 0:
                turns += 1
            elif move < 0 and end_pos > position and position != 0 and end_pos != 0:
                turns += 1

        if move != 0 and end_pos == 0:
            turns += 1

        position = end_pos

    return turns


def part2(file_path: str) -> int:
    directions, steps = parse_file(file_path)
    return count_turns(directions, steps)


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 1")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
