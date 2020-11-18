#!/bin/bash

hdfs dfs -mkdir -p /home/hadoop/$2

wget https://raw.githubusercontent.com/carloshkayser/aws-emr-hello-world/master/scripts/lorem-ipsum-generator.py

python lorem-ipsum-generator.py $1 $2

echo "Copying file to Hadoop..."

hdfs dfs -put $2 /home/hadoop/$2

hdfs dfs -ls /home/hadoop/$2

rm $2

# bash word-count-dataset-generator.sh 10000 word-count-dataset == 57 MB
# bash word-count-dataset-generator.sh 200000 word-count-dataset > 1 GB