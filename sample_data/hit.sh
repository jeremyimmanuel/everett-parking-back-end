#! /bin/bash

python3 put.py $1 |
while read i;
do
    echo $i
    curl $i
    printf "\n"
done
