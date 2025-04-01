#!/usr/bin/env python3
import sys
import csv


#meant to reverse the order of the closest defender to match naming convention of player_name
def fix_defender_name(name):
    if not name or name.strip() == "":
        return None
    if ',' in name:
        parts = name.split(', ')
        if len(parts) == 2:
            return f"{parts[1].title()} {parts[0].title()}"
    return name.title()



reader = csv.DictReader(sys.stdin)


for row in reader:
    try:
        player = row["player_name"].strip().title()
        defender = fix_defender_name(row["CLOSEST_DEFENDER"])
        fgm = int(row["FGM"])
        shot_dist = float(row["SHOT_DIST"])
        def_dist = float(row["CLOSE_DEF_DIST"])
        shot_clock = float(row["SHOT_CLOCK"])

    except (KeyError, ValueError, TypeError):
        continue  # skip bad data

    if not player or not defender:
        continue
    
    #for question 1
    print(f"{player}\t{defender}\t{fgm}")

    #for question 2
    zone = f"{shot_dist}_{def_dist}_{shot_clock}" #underscore delimiter
    print(f"COMFORTZONE|{player}|{zone}\t{fgm}")