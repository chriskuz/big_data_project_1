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
    """
    Process a valid row: Extract the violation_time, convert it to 24-hour format,
    and print the key-value pair.
    """
    time_field = row[time_index].strip()
    hour_str = time_field[:2]
    ampm = time_field[4].upper()  # Should be "A" or "P"
    hour = int(hour_str)
    
    # Convert to 24-hour format
    if ampm == "P" and hour != 12:
        hour += 12
    elif ampm == "A" and hour == 12:
        hour = 0
    
    formatted_hour = f"{hour:02d}"
    print(f"{formatted_hour}\t1")

def clean_rows(reader, time_index):
    """
    Generator that yields only rows with a valid 'violation_time' field.
    Any row that doesn't pass the validation is skipped (and logged to stderr).
    """
    for row in reader:
        # Skip empty rows or rows that don't have enough columns.
        if not row or len(row) <= time_index:
            continue
        time_field = row[time_index].strip()
        if is_valid_violation_time(time_field):
            yield row
        else:
            sys.stderr.write(f"Skipping invalid row: {row}\n")

def main():
    reader = csv.reader(sys.stdin)
    try:
        # Read header and get the index for "violation_time"
        header = next(reader)
        time_index = header.index("violation_time")
    except Exception as e:
        sys.stderr.write(f"Error reading header or finding 'violation_time' column: {e}\n")
        sys.exit(1)
    
    # Process only the rows that pass the cleaning function.
    for row in clean_rows(reader, time_index):
        process_row(row, time_index)

if __name__ == "__main__":
    main()
