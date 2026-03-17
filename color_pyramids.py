#!/usr/bin/env python3
"""Generate colorful random pyramids in the terminal."""

from __future__ import annotations

import random


def random_rgb() -> tuple[int, int, int]:
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def colored(text: str, rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


def build_pyramid(size: int, symbol: str = "#") -> list[str]:
    rows = []
    for level in range(1, size + 1):
        width = 2 * level - 1
        padding = " " * (size - level)
        rows.append(f"{padding}{symbol * width}{padding}")
    return rows


def ask_how_many() -> int:
    while True:
        raw = input("How many colour pyramids do you need? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a positive whole number.")


def main() -> None:
    count = ask_how_many()
    print()

    for index in range(1, count + 1):
        size = random.randint(3, 12)
        rgb = random_rgb()
        print(f"Pyramid {index}: size={size}, color=rgb{rgb}")
        for line in build_pyramid(size):
            print(colored(line, rgb))
        print()


if __name__ == "__main__":
    main()
