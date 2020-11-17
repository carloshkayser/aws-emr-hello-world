#!/bin/bash

hdfs dfs -rm -r /data/$2
hdfs dfs -mkdir /data/$2

python lorem-ipsum-generator.py $1 $2

echo "Copying file to Hadoop..."

hdfs dfs -put $2 /data/$2

hdfs dfs -ls /data/$2

rm $2

# bash word-count-dataset-generator.sh 10000 word-count-dataset == 57 MB
# bash word-count-dataset-generator.sh 200000 word-count-dataset > 1 GB