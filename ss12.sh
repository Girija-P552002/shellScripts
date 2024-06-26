#!/bin/bash
sum=0
for i in {1..100}
do
    sum=$((sum + i))
done
echo "The sum of numbers from 1 to 100 is $sum"