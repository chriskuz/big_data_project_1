#!/usr/bin/env python3
import sys
import csv

def is_valid_violation_time(time_field):
    """
    Return True if time_field meets the expected format "HHMM followed by 'A' or 'P'", else False.
    """
    time_field = time_field.strip()
    if not time_field or time_field.lower() == "null":
        return False
    if len(time_field) < 5:
        return False
    if not time_field[:4].isdigit():
        return False
    if time_field[4].upper() not in ["A", "P"]:
        return False
    return True

def process_row(row, time_index):
    try:
        # Extract and clean the "Violation Time" field
        time_field = row[time_index].strip()
        
        # Validate the time field; skip the row if it doesn't meet criteria
        if not is_valid_violation_time(time_field):
            return
        
        # Extract hour (first two digits) and AM/PM indicator (fifth character)
        hour_str = time_field[:2]
        ampm = time_field[4].upper()  # Should be "A" or "P"
        hour = int(hour_str)
        
        # Convert to 24-hour format:
        if ampm == "P" and hour != 12:
            hour += 12
        elif ampm == "A" and hour == 12:
            hour = 0
        
        # Format the hour as a two-digit string and emit the key-value pair
        formatted_hour = f"{hour:02d}"
        print(f"{formatted_hour}\t1")
    
    except Exception as e:
        # Write any error details to stderr and skip the problematic row.
        sys.stderr.write(f"Error processing row: {row}. Error: {e}\n")

def main():
    reader = csv.reader(sys.stdin)
    
    try:
        # Read header and get the index for "violation_time"
        header = next(reader)
        time_index = header.index("violation_time")
    except Exception as e:
        sys.stderr.write(f"Error reading header or finding 'violation_time' column: {e}\n")
        return
    
    # Process each row using the time_index
    for row in reader:
        # Skip rows with fewer columns than expected or that are completely empty.
        if not row or len(row) <= time_index:
            continue
        
        process_row(row, time_index)

if __name__ == "__main__":
    main()
