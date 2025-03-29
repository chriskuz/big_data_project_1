#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    header = next(reader)
    year_index = header.index("Vehicle Year")
    make_index = header.index("Vehicle Make")
    
    for row in reader:
        if len(row) > max(year_index, make_index):
            vehicle_year = row[year_index].strip()
            vehicle_make = row[make_index].strip()
            
            # Emit key-value pairs only if the field is not empty
            if vehicle_year:
                print(f"year_{vehicle_year}\t1")
            if vehicle_make:
                print(f"make_{vehicle_make}\t1")

if __name__ == "__main__":
    main()
