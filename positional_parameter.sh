#!/bin/bash
echo "Script name: $0"

echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"

echo "Total number of arguments: $#"

#
echo "All arguments as a single string: $*"

echo "All arguments as separate strings: $@"


echo "Loop through each argument:"
for arg in "$@"
do
    echo "$arg"
done

