#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
fgm_sum = 0
attempts = 0

player_focus = ["James Harden", "Lebron James", "Stephen Curry", "Chris Paul"]

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

#last one clause
if current_key:
    p, z = current_key
    print(f"{p}\t{z}\t{fgm_sum / attempts:.4f}")