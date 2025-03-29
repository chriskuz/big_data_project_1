#!/usr/bin/env python3
import sys

def main():
    year_counts = {}
    type_counts = {}

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
        elif key.startswith("type_"):
            vehicle_type = key[len("type_"):]
            type_counts[vehicle_type] = type_counts.get(vehicle_type, 0) + count

    # Determine the most common year and type if there is any data
    if year_counts:
        max_year = max(year_counts, key=year_counts.get)
        max_year_count = year_counts[max_year]
    else:
        max_year = None
        max_year_count = 0

    if type_counts:
        max_type = max(type_counts, key=type_counts.get)
        max_type_count = type_counts[max_type]
    else:
        max_type = None
        max_type_count = 0

    # Output the results
    print(f"Most common year: {max_year}\tCount: {max_year_count}")
    print(f"Most common type: {max_type}\tCount: {max_type_count}")

if __name__ == "__main__":
    main()
