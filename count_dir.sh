#!/bin/bash
directory="."
for file in $directory/*
do 
 if [ -f "$file" ]
 then
    wc_output=$(wc "$file")
    echo $wc_output
 fi
done    
