#!/bin/bash

cd ~

sudo yum install -y git

sudo python3 -m pip install loremipsum boto3

# aws s3 sync $1 .
git clone https://github.com/carloshkayser/aws-emr-hello-world

# bash bootstrap.sh s3://bucket-name