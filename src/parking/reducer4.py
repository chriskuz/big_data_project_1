#!/usr/bin/env python3
import sys

def main():
    color_counts = {}

    # Process each line from standard input
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            key, value = line.split("\t")
            count = int(value)
        except ValueError:
            continue
        
        # Only process keys that start with "color_"
        if key.startswith("color_"):
            color = key[len("color_"):]
            color_counts[color] = color_counts.get(color, 0) + count

    # Find the color with the maximum count
    if color_counts:
        max_color = max(color_counts, key=color_counts.get)
        max_count = color_counts[max_color]
        print("Most common color:", max_color, "Count:", max_count, sep="\t")
    else:
        print("No valid color data found.")

if __name__ == "__main__":
    main()
