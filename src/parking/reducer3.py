#!/usr/bin/env python3
import sys

def main():
    street_counts = {}

    # Process each line from the mapper's output
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            key, value = line.split("\t")
            count = int(value)
        except ValueError:
            continue
        
        # Process only keys that start with "street_"
        if key.startswith("street_"):
            street = key[len("street_"):]
            street_counts[street] = street_counts.get(street, 0) + count

    # Determine the street with the highest count
    if street_counts:
        max_street = max(street_counts, key=street_counts.get)
        max_count = street_counts[max_street]
        print(f"Most common street: {max_street}\tCount: {max_count}")
    else:
        print("No valid street data found.")

if __name__ == "__main__":
    main()
