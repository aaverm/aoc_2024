import argparse


def parse_file(file_path: str) -> list[str]:
    banks = []

    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            line = row.strip()
            banks.append(line)

    return banks


def pick_two_top_from_left(s: str) -> int:
    n = len(s)
    if n < 2:
        return 0

    max_first = max(s[: n - 1])
    i = s.index(max_first)

    suffix = s[i+1:]
    max_second = max(suffix)

    return int(max_first + max_second)


def part1(file_path: str) -> int:
    banks = parse_file(file_path)
    total_joltage = [pick_two_top_from_left(bank) for bank in banks]
    return sum(total_joltage)


def pick_twelve_top_from_left(s: str) -> int:
    n = len(s)
    if n < 12:
        return 0

    result = []

    for i, digit in enumerate(s):
        remaining = n - i

        while result and result[-1] < digit and len(result) - 1 + remaining >= 12:
            result.pop()

        if len(result) < 12:
            result.append(digit)

    result = result[:12]
    return int("".join(result))


def part2(file_path: str) -> int:
    banks = parse_file(file_path)
    total_joltage = [pick_twelve_top_from_left(bank) for bank in banks]
    return sum(total_joltage)


def main() -> None:
    parser = argparse.ArgumentParser(description="AoC 2025 Day 3")
    parser.add_argument("input_file", help="Path to input file")
    args = parser.parse_args()

    p1 = part1(args.input_file)
    p2 = part2(args.input_file)

    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    main()
