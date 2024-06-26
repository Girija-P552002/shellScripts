 #!bin/bash                                                                     
age=19
if (( $age > 18 )) && (( $age < 30 ));then
echo valid age
else
echo not valid
fi


age=200
if (( $age == 18 )) || (( $age == 30 ));then
echo valid age
else
echo not valid
fi
