#!/usr/bin/env python3
import sys
import csv


#what we need for ques 1
    # player, defender, FGM
#what we need for ques 2
    # player name
    # shot distance
    # defender distance
    # shot clocks


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

# print(reader)

for row in reader:
    try:
        player = row["player_name"].strip().title()
        defender = fix_defender_name(row["CLOSEST_DEFENDER"])
        fgm = int(row["FGM"])
        shot_dist = float(row["SHOT_DIST"])
        def_dist = float(row["CLOSE_DEF_DIST"])
        shot_clock = float(row["SHOT_CLOCK"])

        # shot_dist = int(row["above_mid_shot_dist"])
        # def_dist = int(row["above_mid_close_def_dist"])
        # shot_clock = int(row["above_mid_shot_clock"])
    except (KeyError, ValueError, TypeError):
        continue  # skip bad data

    if not player or not defender:
        continue
    
    #for question 1
    print(f"{player}\t{defender}\t{fgm}")

    #for question 2
    zone = f"{shot_dist}_{def_dist}_{shot_clock}" #underscore delimiter
    print(f"COMFORTZONE|{player}|{zone}\t{fgm}")








# for row in reader:
#     player = row["player_name"]
#     defender = row["CLOSEST_DEFENDER"]
#     fgm = int(row["FGM"])

#     # Emit for Question 1
#     print(f"{player}\t{defender}\t{fgm}")

#     # Emit for Question 2 (comfort zones)
#     shot_dist = int(row["above_mid_shot_dist"])
#     def_dist = int(row["above_mid_close_def_dist"])
#     shot_clock = int(row["above_mid_shot_clock"])

#     zone = f"{shot_dist}_{def_dist}_{shot_clock}"
#     print(f"COMFORTZONE|{player}|{zone}\t{fgm}")