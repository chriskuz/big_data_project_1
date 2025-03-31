#!/usr/bin/env python3
import sys

def main():
    year_counts = {}
    make_counts = {}
    
    # Process each line of input
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        
        key, count_str = parts
        try:
            count = int(count_str)
        except ValueError:
            continue
        
        # If the key is all digits, we assume it's a year.
        if key.isdigit():
            year_counts[key] = year_counts.get(key, 0) + count
        else:
            make_counts[key] = make_counts.get(key, 0) + count
    
    # Determine the most common year
    max_year = None
    max_year_count = 0
    for year, total in year_counts.items():
        if total > max_year_count:
            max_year_count = total
            max_year = year
    
    # Determine the most common make
    max_make = None
    max_make_count = 0
    for make, total in make_counts.items():
        if total > max_make_count:
            max_make_count = total
            max_make = make

    if max_year is not None:
        print(f"most common year of car to be ticketed: {max_year} with {max_year_count} tickets")
    if max_make is not None:
        print(f"most common make of car to be ticketed: {max_make} with {max_make_count} tickets")

if __name__ == "__main__":
    main()
