#!/bin/bash
source ../../env.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/input/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /nba/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../test-data/shot_logs.csv /nba/input/
/usr/local/spark/bin/spark-submit --master=spark://$SPARK_MASTER:7077 ./try.py hdfs://$SPARK_MASTER:9000/nba/input/