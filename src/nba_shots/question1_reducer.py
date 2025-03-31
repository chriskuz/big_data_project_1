#!/usr/bin/env python3
import sys
from collections import defaultdict

min_fear_scores = {}

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
        if current_player_defender and fgm_sum >= 3:
            p, d = current_player_defender 
            print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")
        current_player_defender = key
        fgm_sum = 0
        attempts = 0

    fgm_sum += fgm
    attempts += 1 #adds attempt by 

#last one clause
if current_player_defender and fgm_sum >= 3:
    p, d = current_player_defender
    print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")