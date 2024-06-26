#!/bin/bash
sum=0
for i in {1..100}
  do 
     sum=$(( sum+i ))
     #i=$(( i+1 ))
   done  
echo $sum
 
