#!/bin/bash

# task - get first and last letter from each line, concat into a 2-digit number.
# If there's one digit in line, duplicate it.

INPUT_FIlE=inputs/01.txt
sum=0
while read -r line; do
    left=$(sed -r 's/^[a-z]*([0-9]).*/\1/' <<<"$line")
    right=$(sed -r 's/.*([0-9])[a-z]*$/\1/' <<<"$line")
    sum=$(bc <<<"$sum+$left$right")
done <$INPUT_FIlE
echo $sum
