#!/usr/bin/env python3
import sys
import csv

def convert_to_24_hour(time_str):
    """
    Converts a time string of format "HHMMX" (e.g., "0143A" or "0400P")
    into 24-hour format.
    """
    # Ensure the string is long enough
    if len(time_str) < 5:
        return None
    
    try:
        hour = int(time_str[:2])
    except ValueError:
        return None

    # Get the period indicator (last character)
    period = time_str[-1].upper()

    if period == 'A':
        # For AM, convert 12 AM to 0 hour.
        if hour == 12:
            hour = 0
    elif period == 'P':
        # For PM, if it's not already 12 PM, add 12.
        if hour != 12:
            hour += 12
    else:
        # Unrecognized period indicator.
        return None

    return hour

def main():
    # Parse the CSV input using a DictReader (expects a header with "violation_time")
    reader = csv.DictReader(sys.stdin)
    for row in reader:
        time_val = row.get("violation_time", "").strip()
        if not time_val:
            continue

        hour = convert_to_24_hour(time_val)
        if hour is None:
            continue  # Skip rows with invalid time formats

        # Output the key-value pair (hour, 1)
        print(f"{hour}\t1")

if __name__ == "__main__":
    main()
