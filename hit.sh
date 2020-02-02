#! /bin/bash

python3 put.py |
while read i;
do
    echo $i
    curl $i
done