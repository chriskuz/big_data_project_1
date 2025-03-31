#!/usr/bin/env python3
import sys
import csv

# Mapping dictionary for abbreviations to full color names.
COLOR_MAPPING = {
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

def main():
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        # Get the vehicle_color field and strip any extra whitespace.
        vehicle_color = row.get("vehicle_color", "").strip()
        
        # Disregard if the field is empty, or if it equals "nan" or "null" (case-insensitive).
        if not vehicle_color or vehicle_color.lower() in {"nan", "null"}:
            continue
        
        # Convert the color value to uppercase for consistency.
        color_upper = vehicle_color.upper()
        
        # If the value is one of the abbreviations, use the mapped full color.
        if color_upper in COLOR_MAPPING:
            color = COLOR_MAPPING[color_upper]
        else:
            # Otherwise, assume it's already the full color name.
            color = color_upper
        
        # Output the key-value pair: <color, 1>
        print(f"{color}\t1")

if __name__ == "__main__":
    main()
