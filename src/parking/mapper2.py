#!/usr/bin/env python3
import sys
import csv

def main():
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        vehicle_year = row.get("vehicle_year", "").strip()
        vehicle_make = row.get("vehicle_make", "").strip()

        # Only output year if it is not "0"
        if vehicle_year and vehicle_year != "0":
            print(f"{vehicle_year}\t1")
        
        # Always output the make if available
        if vehicle_make:
            print(f"{vehicle_make}\t1")

if __name__ == "__main__":
    main()
