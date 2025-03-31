#!/usr/bin/env python3
import sys

current_key = None
fgm_total = 0
fga_total = 0

for line in sys.stdin:
    try:
        key, fgm = line.strip().split("\t")
        player, zone = key.split("|")
        fgm = int(fgm)
    except ValueError:
        continue

    if key != current_key:
        if current_key is not None:
            cp, cz = current_key.split("|")
            hit_rate = (fgm_total / fga_total) * 100 if fga_total > 0 else 0.0
            print(f"{cp}\t{cz}\t{fgm_total}\t{fga_total}\t{hit_rate:.2f}")
        current_key = key
        fgm_total = 0
        fga_total = 0

    fgm_total += fgm
    fga_total += 1

# Last line
if current_key:
    cp, cz = current_key.split("|")
    hit_rate = (fgm_total / fga_total) * 100 if fga_total > 0 else 0.0
    print(f"{cp}\t{cz}\t{fgm_total}\t{fga_total}\t{hit_rate:.2f}")
