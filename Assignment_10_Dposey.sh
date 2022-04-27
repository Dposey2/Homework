#!/bin/bash
clear

# 1
# This script uses a function to read in from a file and gets the summation of the numbers in the file.
# text_summation(){

#     filename=test_num.txt
#     sum=0
#     while read line
#     do
#         let "sum+=line"
#     done < $filename
#     echo $sum
# }
#     echo "The summation of the numbers in the text file is:"
#     text_summation

#2
#This script uses recursion to fin the fibonacci number
# Fibonacci ()
# {
#     num=$1                
#     if [ $num -lt 2 ]; then
#         echo "$num"              
#     else
#         (( --num ))              
#         num_1=$( Fibonacci $num )       

#         (( --num ))              
#         num_2=$( Fibonacci $num )       

#         echo $(( num_1 + num_2 ))
#     fi
# }

# echo -n "Enter the number of term : "
# read max

# for (( i=0; i<=$max; i++ ))
# do                      
#     fib_num=$(Fibonacci $i)
#     echo "$fib_num "
# done

# 3
# This script appends the output from q1 and q2 to a file
# Fibonacci ()
# {
#     num=$1                
#     if [ $num -lt 2 ]; then
#         echo "$num"              
#     else
#         (( --num ))              
#         num_1=$( Fibonacci $num )       

#         (( --num ))              
#         num_2=$( Fibonacci $num )       

#         echo $(( num_1 + num_2 ))
#     fi
# }

# text_summation(){

#     filename=test_num.txt
#     sum=0
#     while read line
#     do
#         let "sum+=line"
#     done < $filename
#     echo $sum
# }

# echo -n "Enter the number you want to be your max : "
# read max
# filename="question_3.txt"
# echo "Fibonacci numbers: " >> $filename
# for (( i=0; i<=$max; i++ ))
# do                      
#     fib_num=$(Fibonacci $i)
#     echo "$fib_num " >> $filename
# done

# echo "The summation of the numbers in the text file is:" >> $filename
# summation=$(text_summation)
# echo "$summation " >> $filename

#4
#this script creates a random array. And sorts it using recursion, and prints the sorted array to a file.
#Sorry I wasn't able to find out how to use recursion to sort the array.
sort_array(){
    for (( i = 0; i < 10; i++ ))
    do
    number[i]=$RANDOM
    done
    for ((i = 0; i<10; i++))
    do
        for((j = 0; j<10-i-1; j++))
        do
    
            if [ ${number[j]} -gt ${number[$((j+1))]} ]
            then
                temp=${number[j]}
                number[$j]=${number[$((j+1))]}  
                number[$((j+1))]=$temp
            fi
        done
    done
echo ${number[*]}
}

filename="question_4.txt"
sorted_array=$(sort_array)
echo "Sorted array:"
echo "${sorted_array[@]}"
echo  "${sorted_array[*]}" >>$filename