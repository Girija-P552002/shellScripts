#!/bin/bash

arr=(24 27 84 11 99)

echo "Given array: ${arr[*]}"
arr=($(echo "${arr[*]}" | tr ' ' '\n' | sort -n | tr '\n' ' '))  #transforms spaces into newlines, converting the string into a list of numbers 
echo "Sorted array: ${arr[*]}"
