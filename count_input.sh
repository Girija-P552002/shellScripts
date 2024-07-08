#!/bin/bash
echo "enter the file"
read input
wc_output=$(echo "$input"| wc)
echo $wc_output
