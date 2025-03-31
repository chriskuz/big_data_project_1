#!/bin/sh

../../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/data.csv /mapreduce-project1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-files mapper4.py,reducer4.py \
-mapper "python3 mapper4.py" \
-reducer "python3 reducer4.py" \
-input /mapreduce-project1/input/* \
-output /mapreduce-project1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /mapreduce-project1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/
../../../../stop.sh