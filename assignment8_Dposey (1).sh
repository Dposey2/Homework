#!/bin/bash
clear
# #1 This script prints numbers from 1 to 15 using while, until, and for loops.

# #while loop
# echo "While loop"
# i=1
# while [ $i -le 15 ]
# do
#         echo $i
#         let "i++"
# done


# #until loop
# echo "Until loop"
# j=1
# until [ $j -ge 15 ]
# do
#         echo $j
#         let "j++"
# done
# echo $j

# #for loop
# echo "For loop"
# for (( k=1; k <= 15; k++ ))
# do
#         echo $k
# done


# #2 This script prints the summation of numbers from 20 to 40 using while,until and for loops

#while loop
# echo "While loop"
# i=20
# sum_while=0
# while [ $i -le 40 ]
# do
#         let "sum_while+=i"
#         let "i++"
# done
# echo $sum_while

# #until loop
# echo "Until loop"
# j=20
# sum_until=0
# until [ $j -ge 40 ]
# do
#         let "sum_until+=j"
#         let "j++"
# done
# let "sum_until+=j"
# echo $sum_until

# #for loop
# echo "For loop"
# sum_for=0
# for (( k=20; k <= 40; k++ ))
# do
#         let "sum_for+=k"
# done
# echo $sum_for


# #3 This script prints prime numbers less than 50 using while, until, and for loops.

# #for loop
# echo "For loop"
# for (( i=2; i <= 50; i++))
# do
#     prime=0
#     for j in $(seq 2 $(expr $i - 1))
#     do 
#         if [ $(expr $i % $j) -eq 0 ]
#         then
#             prime=1
#             break
#         fi
#     done
#     if [ $prime -eq 0 ]
#     then
#     echo $i
#     fi
# done

# #While loop
# echo "While loop"
# i=2
# j=50
# prime=0
# tem_1=2
# while [ $i -ne $j ]
# do
#     temp_2=`echo $i`
#     while [ $temp_2 -ne $tem_1 ]
#     do
#         temp_2=`expr $temp_2 - 1`
#         n=`expr $i % $temp_2`
#         if [ $n -eq 0 -a $prime -eq 0 ]
#         then
#             prime=1
#         fi
#     done
#     if [ $prime -eq 0 ]
#         then
#             echo $i
#         else
#         prime=0
#     fi
#     i=`expr $i + 1`
# done

# #until loop
# echo "Until loop"
# i=2
# j=50
# prime=0
# tem_1=2
# until [ $i -eq $j ]
# do
#     temp_2=`echo $i`
#     until [ $temp_2 -eq $tem_1 ]
#     do
#         temp_2=`expr $temp_2 - 1`
#         n=`expr $i % $temp_2`
#         if [ $n -eq 0 -a $prime -eq 0 ]
#         then
#             prime=1
#         fi
#     done
#     if [ $prime -eq 0 ]
#         then
#             echo $i
#         else
#         prime=0
#     fi
#     i=`expr $i + 1`
# done

# #4 Takes input from user and provides a certain output based on the input
# echo "Please enter which A&M you go to"
# read user_input
# if [[ $user_input == "Corpus" || $user_input == "corpus" ]]
# then
# echo "Texas A&M University Corpus Christi"
# elif [[ $user_input == "Kingsville" || $user_input == "kingville" ]]
# then
# echo "Texas A&M University Kingsville"
# elif [[ $user_input == "commerce" || $user_input == "Commerce" ]]
# then
# echo "Texas A&M University Commerce"
# else
# echo "Please enter a correct input"
# fi

# #Bonus Question
# var_test=20
# #ranges 1 to 10, 11 to 20, more

# if [[ $var_test -ge 1 && $var_test -le 10 ]]
# then
# echo "Between 1 to 10"
# elif [[ $var_test -ge 11 && $var_test -le 20 ]]
# then
# echo "Between 11 to 20"
# elif [ $var_test -gt 20 ]
# then
# echo "Greater than 20"
# else
# echo "Less than 1"
# fi