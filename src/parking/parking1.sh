#!/bin/sh
../../../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /mapreduce-project1/input/

APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
API_URL="https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?limit=0&$$app_token=${APP_TOKEN}"

curl -s "$API_URL" -o data.csv

/usr/local/hadoop/bin/hdfs dfs -put data.csv /mapreduce-project1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file mapper1.py -mapper mapper1.py \
  -file reducer1.py -reducer reducer1.py \
  -input /mapreduce-project1/input/* -output /mapreduce-project1/output/

/usr/local/hadoop/bin/hdfs dfs -cat /mapreduce-project1/output/part-00000

/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /mapreduce-project1/output/

../../../../stop.sh
