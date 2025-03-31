#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        street_name = row.get("street_name", "").strip()
        if street_name:
            # Convert street name to uppercase and output as key-value pair
            print(f"{street_name.upper()}\t1")

if __name__ == "__main__":
    main()
