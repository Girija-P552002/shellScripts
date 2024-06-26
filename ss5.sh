#!/bin/bash

read -p "num1:" num1 
read -p "num2:" num2

add=$(( num1 + num2 ))
echo "Addition of $num1 & $num2 is $add"

diff=$(( num1 - num2 ))
echo "Subtraction of $num1 & $num2 is $diff"

prod=$(( num1 * num2 ))
echo "Multiplication of $num1 & $num2 is $prod"

div=$(( num1 / num2 ))
echo "Division of $num1 & $num2 is $div"




