#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    #handling each attribute separately
    try:
        shot_dist = float(row["SHOT_DIST"])
        print(f"SHOT_DIST\t{shot_dist}")
    except (KeyError, ValueError):
        pass

    try:
        def_dist = float(row["CLOSE_DEF_DIST"])
        print(f"CLOSE_DEF_DIST\t{def_dist}")
    except (KeyError, ValueError):
        pass

    try:
        shot_clock = float(row["SHOT_CLOCK"])
        print(f"SHOT_CLOCK\t{shot_clock}")
    except (KeyError, ValueError):
        pass