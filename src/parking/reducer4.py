#!/usr/bin/env python3
import sys

def main():
    color_counts = {}

    # Process each line from standard input.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            color, count_str = line.split("\t")
            count = int(count_str)
        except ValueError:
            continue  # Skip lines that don't match the expected format

        # Aggregate counts for each color.
        color_counts[color] = color_counts.get(color, 0) + count

    # Find the color with the maximum count.
    max_color = None
    max_count = 0
    for color, count in color_counts.items():
        if count > max_count:
            max_count = count
            max_color = color

    if max_color is not None:
        print(f"the vehicle color that is most likely to get a ticket is: {max_color} with {max_count} tickets")

if __name__ == "__main__":
    main()
