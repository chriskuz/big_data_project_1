#!/usr/bin/env python3
import sys
import csv

def normalize_color(color):
    if not color:
        return None
    c = color.strip().upper()
    if c in ("NAN", "NULL", ""):
        return None
    abbreviation_mapping = {
        "BL": "BLUE",
        "BK": "BLACK",
        "WH": "WHITE",
        "GY": "GRAY",
        "YW": "YELLOW",
        "OR": "ORANGE",
        "RD": "RED",
        "SIL": "SILVER",
        "TN": "TAN"
    }
    standard_colors = {"BLUE", "BLACK", "WHITE", "GRAY", "YELLOW", "ORANGE", "RED", "SILVER", "TAN"}
    if c in abbreviation_mapping:
        return abbreviation_mapping[c]
    elif c in standard_colors:
        return c
    else:
        return None

def main():
    reader = csv.reader(sys.stdin)
    header = next(reader)
    color_index = header.index("vehicle_color")
    
    for row in reader:
        if len(row) > color_index and all(row):
            vehicle_color = row[color_index]
            normalized_color = normalize_color(vehicle_color)
            if normalized_color:
                print(f"color_{normalized_color}\t1")

if __name__ == "__main__":
    main()
