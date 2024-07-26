#!/bin/bash

read -p "enter the file name:"  file
read -p "enter the new permission in num" permission

if [ -f $file ]; then
sudo chmod $permission $file
echo "permission for the file has been changed!"
else
echo "error!"
fi
