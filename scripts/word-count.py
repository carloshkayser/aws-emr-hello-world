from pyspark import SparkContext, SparkConf

import sys

if __name__ == "__main__":

    # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Word Count")
    sc = SparkContext(conf=conf)
    
    # read a text file
    tokenized = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
    
    # Getting the number of partitions
    print('Number of partitions:', tokenized.getNumPartitions())
    
    # transform each line into words
    tokenized = tokenized.flatMap(lambda line: line.split(" "))

    # counting the occurrence of each word
    wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1+v2)
    
    # saving the output as text file
    wordCounts.saveAsTextFile(sys.argv[2])
    
    sc.stop()
    
# spark-submit --deploy-mode cluster --master yarn --num-executors <num-executors> --executor-cores <executor-cores> --executor-memory <executor-memory> --conf spark.yarn.submit.waitAppCompletion=true word-count.py <input-textfile> <output-textfile>