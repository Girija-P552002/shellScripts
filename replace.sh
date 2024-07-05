#!/bin/bash
echo "enter the file"
read  file

echo "enter the replace test"
read replace

echo "enter the alternate text"
read  alternate 

sed -i "s/${replace}/${alternate}/g" "$file"

echo "replaced"

