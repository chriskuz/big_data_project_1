#!/bin/bash

../../../../start.sh

INPUT="/mapreduce-project1/input"
OUTPUT1="/mapreduce-project1/output1_maxpoints"
OUTPUT2="/mapreduce-project1/output2_comfort_mapper"
OUTPUT3="/mapreduce-project1/output3_comfort_reducer"


/usr/local/hadoop/bin/hdfs dfs -rm -r $INPUT $OUTPUT1 $OUTPUT2 $OUTPUT3

/usr/local/hadoop/bin/hdfs dfs -mkdir -p $INPUT
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/shot_logs.csv $INPUT


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file maxpoint_mapper.py -mapper maxpoint_mapper.py \
  -file maxpoint_reducer.py -reducer maxpoint_reducer.py \
  -input $INPUT -output $OUTPUT1

/usr/local/hadoop/bin/hdfs dfs -getmerge $OUTPUT1 maxpoints.txt

read SHOT_DIST CLOSE_DEF SHOT_CLOCK < <(awk '
  $1=="SHOT_DIST"{d=$2/2}
  $1=="CLOSE_DEF_DIST"{c=$2/2}
  $1=="SHOT_CLOCK"{s=$2/2}
  END{printf "%.4f %.4f %.4f", d, c, s}
' maxpoints.txt)

echo "[INFO] Midpoints: $SHOT_DIST $CLOSE_DEF $SHOT_CLOCK"


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file general_mapper.py -mapper general_mapper.py \
  -file all_comfort_zone_sort_mapper.py \
  -reducer "python3 all_comfort_zone_sort_mapper.py $SHOT_DIST $CLOSE_DEF $SHOT_CLOCK" \
  -input $INPUT -output $OUTPUT2


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file player_comfort_zones_reducer.py -reducer player_comfort_zones_reducer.py \
  -mapper cat \
  -input $OUTPUT2 -output $OUTPUT3


/usr/local/hadoop/bin/hdfs dfs -cat $OUTPUT3/part-00000


/usr/local/hadoop/bin/hdfs dfs -rm -r $INPUT $OUTPUT1 $OUTPUT2 $OUTPUT3
rm -f maxpoints.txt

../../../../stop.sh