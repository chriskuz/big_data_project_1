#!/usr/bin/env python3
import sys
import csv


shot_dist_mid = float(sys.argv[1])
def_dist_mid = float(sys.argv[2])
clock_mid = float(sys.argv[3])

for line in sys.stdin:
    if not line.startswith("COMFORTZONE"):
        continue
    try:
        prefix, value = line.strip().split("\t")
        _, player, zone = prefix.split("|")
        shot_dist, def_dist, clock = map(float, zone.split("_"))
        fgm = int(value)
    except ValueError:
        continue

    # Categorize zone
    sd = int(shot_dist >= shot_dist_mid)
    dd = int(def_dist >= def_dist_mid)
    sc = int(clock >= clock_mid)

    # Comfort zone name
    if sd == 0 and dd == 0:
        zone_label = "closer_shooting_closer_defender"
    elif sd == 1 and dd == 0:
        zone_label = "further_shooting_closer_defender"
    elif sd == 0 and dd == 1:
        zone_label = "closer_shooting_further_defender"
    else:
        zone_label = "further_shooting_further_defender"

    clock_label = "high_clock" if sc else "low_clock"
    final_zone = f"{zone_label}_{clock_label}"


    print(f"{player}|{final_zone}\t{fgm}")