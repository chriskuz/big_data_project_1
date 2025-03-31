#!/usr/bin/env python3
import sys

def main():
    street_counts = {}

    # Process each line of input from the mapper.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            street, count_str = line.split("\t")
            count = int(count_str)
        except ValueError:
            continue  # Skip lines with formatting issues

        # Aggregate counts for each street.
        street_counts[street] = street_counts.get(street, 0) + count

    # Find the street with the maximum count.
    max_street = None
    max_count = 0
    for street, count in street_counts.items():
        if count > max_count:
            max_count = count
            max_street = street

    if max_street is not None:
        print(f"tickets are most commonly issued at: {max_street} with {max_count} tickets")

if __name__ == "__main__":
    main()
