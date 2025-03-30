#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    header = next(reader)
    year_index = header.index("vehicle_year")
    make_index = header.index("vehicle_make")
    
    for row in reader:
        # Make sure the row has enough columns
        if len(row) > max(year_index, make_index):
            vehicle_year = row[year_index].strip()
            vehicle_make = row[make_index].strip()
            
            try:
                year_int = int(vehicle_year)
            except ValueError:
                year_int = 0
                
            if year_int > 0:
                print(f"year_{year_int}\t1")
            
            if vehicle_make:
                print(f"make_{vehicle_make}\t1")

if __name__ == "__main__":
    main()

