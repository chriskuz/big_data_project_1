#!/bin/sh

#!/bin/sh

../../../../start.sh

# === SETUP PATHS ===
BASE=/mapreduce-project1
INPUT=$BASE/input
OUTPUT1=$BASE/output1_maxpoints
OUTPUT2=$BASE/output2_comfortzones

# === CLEAN OLD DIRS ===
/usr/local/hadoop/bin/hdfs dfs -rm -r $INPUT
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUTPUT1
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUTPUT2

# === MAKE INPUT DIR + UPLOAD FILE ===
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $INPUT
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/shot_logs.csv $INPUT/

# === FIRST JOB: Maxpoint Calculation ===
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -input $INPUT \
  -output $OUTPUT1 \
  -file maxpoint_mapper.py -mapper maxpoint_mapper.py \
  -file maxpoint_reducer.py -reducer maxpoint_reducer.py

# === Pull Maxpoints Locally ===
/usr/local/hadoop/bin/hdfs dfs -getmerge $OUTPUT1 maxpoints.txt

# === Extract Midpoints ===
read SHOT_DIST CLOSE_DEF SHOT_CLOCK < <(awk '
  $1=="SHOT_DIST"{d=$2/2}
  $1=="CLOSE_DEF_DIST"{c=$2/2}
  $1=="SHOT_CLOCK"{s=$2/2}
  END{printf "%.4f %.4f %.4f", d, c, s}
' maxpoints.txt)

echo "[INFO] Midpoints:"
echo "  SHOT_DIST: $SHOT_DIST"
echo "  CLOSE_DEF: $CLOSE_DEF"
echo "  SHOT_CLOCK: $SHOT_CLOCK"

# === SECOND JOB: Comfort Zone Categorization ===
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -input $INPUT \
  -output $OUTPUT2 \
  -file general_mapper.py -mapper general_mapper.py \
  -file comfort_zone_sort_mapper.py \
  -file comfort_zone_aggregator_reducer.py \
  -reducer "python3 comfort_zone_sort_mapper.py $SHOT_DIST $CLOSE_DEF $SHOT_CLOCK | sort | python3 comfort_zone_aggregator_reducer.py"

# === View Final Output ===
/usr/local/hadoop/bin/hdfs dfs -cat $OUTPUT2/part-00000

# === Cleanup HDFS + Local Temp ===
/usr/local/hadoop/bin/hdfs dfs -rm -r $INPUT
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUTPUT1
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUTPUT2
rm -f maxpoints.txt

../../../../stop.sh