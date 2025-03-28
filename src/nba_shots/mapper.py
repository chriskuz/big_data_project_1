#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)


#what we need for ques 1
    # player, defender, FGM
#what we need for ques 2
    # player name
    # shot distance
    # defender distance
    # shot clocks




#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    player = row["player_name"]
    defender = row["CLOSEST_DEFENDER"]
    fgm = int(row["FGM"])

    # Emit for Question 1
    print(f"{player}\t{defender}\t{fgm}")

    # Emit for Question 2 (comfort zones)
    shot_dist = int(row["above_mid_shot_dist"])
    def_dist = int(row["above_mid_close_def_dist"])
    shot_clock = int(row["above_mid_shot_clock"])

    zone = f"{shot_dist}_{def_dist}_{shot_clock}"
    print(f"COMFORTZONE|{player}|{zone}\t{fgm}")



#!/usr/bin/env python3
import sys
from collections import defaultdict

current_player_defender = None
fgm_sum = 0
attempts = 0

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3:
        continue

    player, defender, fgm = parts
    key = (player, defender)
    fgm = int(fgm)

    if current_player_defender != key:
        if current_player_defender:
            p, d = current_player_defender
            print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")
        current_player_defender = key
        fgm_sum = 0
        attempts = 0

    fgm_sum += fgm
    attempts += 1

# print last one
if current_player_defender:
    p, d = current_player_defender
    print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")




#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
fgm_sum = 0
attempts = 0

for line in sys.stdin:
    line = line.strip()
    if not line.startswith("COMFORTZONE|"):
        continue

    tag, value = line.split("\t")
    _, player, zone = tag.split("|")
    key = (player, zone)
    fgm = int(value)

    if current_key != key:
        if current_key:
            p, z = current_key
            print(f"{p}\t{z}\t{fgm_sum / attempts:.4f}")
        current_key = key
        fgm_sum = 0
        attempts = 0

    fgm_sum += fgm
    attempts += 1

# Print last group
if current_key:
    p, z = current_key
    print(f"{p}\t{z}\t{fgm_sum / attempts:.4f}")