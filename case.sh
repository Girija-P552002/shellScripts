#!/bin/bash
echo "enter the number from 1 to 3"
read num

case "$num" in
    1)
      echo "you have selected 1";;
    2)  
     echo  "you have selected 2"
     echo "enter A or B:"
     read letter
     case "$letter" in
       A)
        echo "you have selected A";;
       B)
        echo "you have selected B" ;;  
     esac
      ;;    
    3)
     echo  "you have selected 3";; 
    *)
      echo "invalid num";;
esac       
     
     

