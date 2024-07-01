#!/bin/bash
DAY=$(date +%F)
for FILE in *.jpeg
 do
    mv $FILE ${DAY}-${FILE}
 done