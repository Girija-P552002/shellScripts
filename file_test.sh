#!/bin/bash
echo  -e "enter the name of the file: \c"        #meaning the cursor stays on the same line after displaying the prompt
read file


if [ -f "$file" ];then       #[ -d file_name ] [ -e file_name ] -s=to check empty,-r,-w,-x
   echo "$file found"
else
   echo "$file not found"
fi
