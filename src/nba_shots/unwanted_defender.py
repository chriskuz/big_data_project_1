#!/usr/bin/env python3
import sys
from collections import defaultdict

min_fear_scores = {}

current_player_defender = None
fgm_sum = 0
attempts = 0

fgm_sum_filter = 2
attempts_filter = 5

for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) != 3: #we're only concerned with txt values equating to 3 parts length
        continue

    player, defender, fgm = parts
    key = (player, defender)
    fgm = int(fgm)

    if current_player_defender != key:
        if current_player_defender and fgm_sum >= fgm_sum_filter and attempts >= attempts_filter:
            p, d = current_player_defender 
            hit_rate = fgm_sum / attempts
            if p not in min_fear_scores or hit_rate < min_fear_scores[p][1]:
                min_fear_scores[p] = (d, hit_rate, fgm_sum, attempts)

            # print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")
        current_player_defender = key
        fgm_sum = 0
        attempts = 0

    fgm_sum += fgm #notes boolean presence of fgm and includes as sum. 
    attempts += 1 #adds attempt up regardless

#last one clause
if current_player_defender and fgm_sum >= fgm_sum_filter and attempts >= attempts_filter:
    p, d = current_player_defender
    hit_rate = fgm_sum / attempts
    if p not in min_fear_scores or hit_rate < min_fear_scores[p][1]:
        min_fear_scores[p] = (d, hit_rate, fgm_sum, attempts)
    # print(f"{p}\t{d}\t{fgm_sum / attempts:.4f}")

for player, (defender, fg_pct, fgm, fga) in min_fear_scores.items():
    print(f"{player}\t{defender}\t{fgm}\t{fga}\t{fg_pct:.4f}")