- need to find out how large the cluster is
    - if its too small for all of this data, how do we navigate this problem of data storage?
    - where specifically is the data stored? manager node or worker nodes? if the data is too large, is it always stored totally on worker nodes?
    - when calling via API end point, do we chunk pull the data? 
    - 
- do our worker nodes need to be individually updated with python3? 
    - if we manually do this, can we write about how to programmatically do this? 
    - each worker is doing the work....so if we ask it to run python 3 and it only has python 2, i imagine the work won't get done correctly


The choice it hardcode

How we uplaod the data

The default dict csv

The use of fgm_sum threshold

Last case condition

talk about why fgm going to 2 is both low, but also most probable for statistically significance (ignoring just 1, but weighing in those who score twice in a game and primarily on the same exact defender)...5 attempts is more of a weighting factor. 



question 2:
- reducer to handle quadrants of all players
- reducer to handle quadrants of 4 filtered down players
- general mapper for data output(?)
- midpoint_mapper for mid point comparison of players

- could use midpoints pre-calculated via pandas (and hard-value set them)----then insert into reducer(s) to compare off of
- run a single round of mapreduce where 





So let's summarize and collect our thoughts on the development needed to answer the question around categorizing every defender's hit rate under specific midpoint clause combinations based on 3 pulled attributes. 



Here is my general mapper code that outputs for 2 questions:
```
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
```

A resulting output general mapper's output looks like this (note that the name "Jarrett Jack" is repeated, but is not considered to be the only unique value displayed in this spot): 
```
Jarrett Jack    Reggie Jackson  0
COMFORTZONE|Jarrett Jack|5.1_2.1_13.8   0
Jarrett Jack    Brandon Jennings        0
COMFORTZONE|Jarrett Jack|15.5_3.1_7.1   0
Jarrett Jack    D.J. Augustin   0
COMFORTZONE|Jarrett Jack|22.1_2.9_7.3   0
Jarrett Jack    D.J. Augustin   1
COMFORTZONE|Jarrett Jack|18.2_1.1_14.3  1
Jarrett Jack    D.J. Augustin   0
COMFORTZONE|Jarrett Jack|22.7_4.0_19.8  0
Jarrett Jack    Rajon Rondo     0
COMFORTZONE|Jarrett Jack|12.6_4.8_11.4  0
Jarrett Jack    Avery Bradley   0
COMFORTZONE|Jarrett Jack|7.4_2.7_19.0   0
Jarrett Jack    Marcus Smart    1
COMFORTZONE|Jarrett Jack|14.5_3.1_7.0   1
Jarrett Jack    Jared Sullinger 1
COMFORTZONE|Jarrett Jack|8.9_5.7_15.3   1
Jarrett Jack    Marcus Smart    0
COMFORTZONE|Jarrett Jack|8.7_0.8_18.3   0
Jarrett Jack    Evan Turner     1
COMFORTZONE|Jarrett Jack|0.6_0.6_19.8   1
Jarrett Jack    Marcus Thornton 1
COMFORTZONE|Jarrett Jack|16.9_4.2_23.0  1
Jarrett Jack    Avery Bradley   0
COMFORTZONE|Jarrett Jack|18.3_3.0_9.1   0
```

For question 1, we use a reducer that works on the outputs whose parts == 3. This works successfully and we are no longer concerned with work done on this question. 

For question 2, we require the need of one reducer to calculate the total maximums of avialble underscore delimited parts for any line that != 3 parts length....examples of such will be lines prefaced `COMFORTZONE` and noted values could be "18.3_3.0_9.1" (this is just a single example value chosen arbitrarily from the sample output and the numbers are subject to change). We want the maximum calculated from each of these values among all values found. From these maximums, I would divide them by 2, to calculate the mid point of such and in the end only omit 3 values from such. These 3 values would then fall into another reducer which will use them to perform other calculations. 

If I wanted the right information, I would skip over anything from the mapper where the length == 3 for parts, to my knowledge. Thats one thing to state I believe. 

The current reducer's structure to find such maximums is indicated as such:
```
#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
current_max = float("-inf")




for line in sys.stdin:
    parts = line.strip().split("\t")
    if len(parts) == 3:
        continue
    try:
        key, value = line.strip.split("\t")
        value = float(value)
    except: 
        continue

    if current_key != key:
        if current_key is not None:
            print(f"{current_key}\t{current_max}")
        current_key = key
        current_max = value
    else:
        current_max = max(current_max, value)

if current_key is not None:
    print(f"{current_key}\t{current_max}")
```

We spoke about this previously and began working a sensible structure for answering this question with the use of several reducers:
- one to apply corresponding hit rate to filtered categories of zones based on boolean combinations of only 2 attributes out of the 3 (shot_dist, def_dist used for comfort zone calculation with boolean combinations denoting such as a hit rate filter) and (shot clock used as an extended filter not truly categorized into a quadrant, but can be treated seperately to be the differentiator between under middle of shot clock and over middle of shot clock)
- one to isolate only on specific players under a filter. 

So, I just tested the reducer, and it fails at the `try` statement. Why? Is there something wrong with how my key is being processed from the general mapper? Can I use the general mapper to get the data I need or should I make a specific mapper entirely meant for the mid point calculation? If I make a specific mapper entirely meant for the mid point calculation, do I then revert back to the use of a general mapper against a reducer that can apply categorizations and ultimately begin answering my questions? 

Where is the midpoint actually calculated? Do we calculate midpoints in the reducer that finds the maximums or is that calculated in another reducer warranting the use of the maximums values pulled in as arguments?

Note this is all going to be plugged into hdfs, meaning shell scripts will be used to execute this question. 