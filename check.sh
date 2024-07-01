#check the list of files or directory and list all the files if its a directory
#!/bin/bash
files=$@
for file in $files
   do
     if [ -f "$file" ];then
       echo "$file is regular file"
     elif [ -d "$file" ];then 
       echo "$file is dirctory file"
      else  
       echo "its not file"
     fi 
    ls -l $file  
   done 