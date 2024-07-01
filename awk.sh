#read the file and print the managers salary

#!/bin/bash
cat abc.txt | while read line
do
    echo "$line" | awk '/manager/ {print}'
done 
