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