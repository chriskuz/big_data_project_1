#!/usr/bin/env python3
import sys

current_key = None
current_max = float("-inf")

for line in sys.stdin:
    try:
        key, value = line.strip().split("\t")
        value = float(value)
    except ValueError:
        continue

    if key != current_key:
        if current_key is not None:
            print(f"{current_key}\t{current_max}")
        current_key = key
        current_max = value
    else:
        current_max = max(current_max, value)

# Final line
if current_key is not None:
    print(f"{current_key}\t{current_max}")