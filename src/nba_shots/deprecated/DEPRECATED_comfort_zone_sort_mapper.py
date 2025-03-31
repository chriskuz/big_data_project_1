#!/usr/bin/env python3
import sys

SHOT_DIST_THRESH = float(sys.argv[1])
CLOSE_DEF_THRESH = float(sys.argv[2])
SHOT_CLOCK_THRESH = float(sys.argv[3])

def get_zone_label(shot_dist, def_dist):
    shot = 1 if shot_dist >= SHOT_DIST_THRESH else 0
    defender = 1 if def_dist >= CLOSE_DEF_THRESH else 0
    if shot == 0 and defender == 0:
        return "closer_shooting_closer_defender"
    elif shot == 1 and defender == 0:
        return "further_shooting_closer_defender"
    elif shot == 0 and defender == 1:
        return "closer_shooting_further_defender"
    else:
        return "further_shooting_further_defender"

for line in sys.stdin:
    line = line.strip()
    if not line.startswith("COMFORTZONE|"):
        continue

    try:
        tag, fgm = line.split("\t")
        _, player, zone = tag.strip().split("|")
        shot_dist, def_dist, shot_clock = map(float, zone.strip().split("_"))
        fgm = int(fgm.strip())
    except:
        continue

    zone_label = get_zone_label(shot_dist, def_dist)
    clock_tag = "high_clock" if shot_clock >= SHOT_CLOCK_THRESH else "low_clock"
    final_zone = f"{zone_label}_{clock_tag}"

    key = f"{player}\t{final_zone}"
    print(f"{key}\t{fgm}")