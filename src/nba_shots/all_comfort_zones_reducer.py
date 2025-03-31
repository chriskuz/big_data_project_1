#!/usr/bin/env python3
import sys

current_key = None
fgm_sum = 0
fga_sum = 0

for line in sys.stdin:
    try:
        parts = line.strip().split("\t")
        if len(parts) != 3:
            continue
        player, zone, fgm = parts
        key = (player, zone)
        fgm = int(fgm)
    except:
        continue

    if current_key != key:
        if current_key:
            p, z = current_key
            hit_rate = (fgm_sum / fga_sum) * 100 if fga_sum > 0 else 0.0
            print(f"{p}\t{z}\t{fgm_sum}\t{fga_sum}\t{hit_rate:.2f}")
        current_key = key
        fgm_sum = 0
        fga_sum = 0

    fgm_sum += fgm
    fga_sum += 1

# last record
if current_key:
    p, z = current_key
    hit_rate = (fgm_sum / fga_sum) * 100 if fga_sum > 0 else 0.0
    print(f"{p}\t{z}\t{fgm_sum}\t{fga_sum}\t{hit_rate:.2f}")