#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    header = next(reader)
    street_index = header.index("street_name")
    
    for row in reader:
        if len(row) > street_index:
            street_name = row[street_index].strip().upper()  # Convert to uppercase for standardization
            if street_name and street_name.isalpha():
                print(f"street_{street_name}\t1")

if __name__ == "__main__":
    main()
