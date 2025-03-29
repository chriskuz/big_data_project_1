#!/usr/bin/env python3
import sys

def main():
    year_counts = {}
    make_counts = {}

    # Process each line of the input
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        key, value = line.split("\t")
        count = int(value)
        
        # Check the key prefix to determine which category it belongs to
        if key.startswith("year_"):
            year = key[len("year_"):]
            year_counts[year] = year_counts.get(year, 0) + count
        elif key.startswith("make_"):
            vehicle_make = key[len("make_"):]
            make_counts[vehicle_make] = make_counts.get(vehicle_make, 0) + count

    # Determine the most common year and make if there is any data
    if year_counts:
        max_year = max(year_counts, key=year_counts.get)
        max_year_count = year_counts[max_year]
    else:
        max_year = None
        max_year_count = 0

    if make_counts:
        max_make = max(make_counts, key=make_counts.get)
        max_make_count = make_counts[max_make]
    else:
        max_make = None
        max_make_count = 0

    # Output the results
    print(f"Most common year: {max_year}\tCount: {max_year_count}")
    print(f"Most common make: {max_make}\tCount: {max_make_count}")

if __name__ == "__main__":
    main()
