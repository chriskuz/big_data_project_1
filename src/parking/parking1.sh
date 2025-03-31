#!/bin/sh

../../../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../../../../mapreduce-test/mapreduce-project1/big_data_project_1/src/parking/data.csv /mapreduce-project1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-files mapper1.py,reducer1.py \
-mapper "python mapper1.py" \
-reducer "python reducer1.py" \
-input /mapreduce-project1/input/* \
-output /mapreduce-project1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /mapreduce-project1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/
../../../../stop.sh
