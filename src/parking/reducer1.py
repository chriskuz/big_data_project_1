#!/usr/bin/env python3
import sys

def main():
    counts = {}

    # Process each line from the mapper's output
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Each line is expected to be in the format: hour \t 1
        try:
            hour, count_str = line.split("\t")
            count = int(count_str)
        except ValueError:
            continue

        # Accumulate counts per hour
        if hour in counts:
            counts[hour] += count
        else:
            counts[hour] = count

    # Find the hour with the maximum count
    try:
        max_hour = max(counts, key=counts.get)
        max_count = counts[max_hour]
        # Output the hour with the maximum ticket count
        print(f"{max_hour}\t{max_count}")
    except ValueError:
        # Handle the case where counts is empty
        pass

if __name__ == "__main__":
    main()