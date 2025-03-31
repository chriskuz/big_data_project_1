#!/usr/bin/env python3
import sys

def main():
    hour_counts = {}

    # Process each line from standard input.
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            hour, count_str = line.split("\t")
            count = int(count_str)
        except ValueError:
            continue  # Skip lines that don't match the expected format

        # Aggregate counts for each hour
        hour_counts[hour] = hour_counts.get(hour, 0) + count

    # Find the hour with the maximum count
    max_hour = None
    max_count = 0
    for hour, total in hour_counts.items():
        if total > max_count:
            max_count = total
            max_hour = hour

    if max_hour is not None:
        print(f"tickets are most likely to be issued at the hour {max_hour} with {max_count} tickets")

if __name__ == "__main__":
    main()
