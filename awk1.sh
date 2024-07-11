#!/bin/bash
echo "enter the file"
read files
cat "$files"
awk '{print $2,$1}' "$files"



