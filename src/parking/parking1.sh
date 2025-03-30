#!/bin/sh
../../../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /project1/input/

APP_TOKEN="tzksBXvIq9l9Ub985hzK3D5HP"
API_URL="http://api.example.com/ny_parking_tickets?limit=0&app_token=${APP_TOKEN}"

curl -s "$API_URL" -o data.csv

/usr/local/hadoop/bin/hdfs dfs -put data.csv /project1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
  -file mapper1.py -mapper mapper1.py \
  -file reducer1.py -reducer reducer1.py \
  -input /project1/input/* -output /project1/output/

/usr/local/hadoop/bin/hdfs dfs -cat /project1/output/part-00000

/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /project1/output/

../../../../stop.sh
