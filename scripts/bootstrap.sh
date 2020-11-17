#!/bin/bash

cd ~

pip install loremipsum

# aws s3 sync $1 .
git clone https://github.com/carloshkayser/aws-emr-hello-world

# bash bootstrap.sh s3://bucket-name