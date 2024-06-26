#/bin/bash
echo  -e "enter the name of the file: \c"
read file

if [ -f "$file" ];then
    if [ -w $file_name ] ;then
        echo this is the 2nd line
        cat >> $file
      else
        echo this file does not have wite permission
    fi
else
    echo "$file not exists"
fi






