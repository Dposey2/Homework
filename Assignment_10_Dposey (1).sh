#!/bin/bash
clear

# 1
# This script uses a function to read in from a file and gets the summation of the numbers in the file.
# filename="test_num.txt"

# while read line
# do
#     arr[i]=$line
#     let i+=1
# done < $filename

# echo "${arr[@]}"
# sum=0
# text_summation(){
#     sum=$2
#     index=$1
#     if [ ${#arr[@]} -lt 1 ]
#     then
#         return $sum
#     else
#         temp=${arr[index]}
#         let sum+=temp
#         unset arr[index]
#         let temp2=index+1
#         text_summation $temp2 $sum
#     fi
# }

# text_summation 0 $sum
# total_sum=$sum
# echo "The summation is: "
# echo "$total_sum"


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

# filename="test_num.txt"

# while read line
# do
#     arr[i]=$line
#     let i+=1
# done < $filename

# echo "${arr[@]}"
# sum=0
# text_summation(){
#     sum=$2
#     index=$1
#     if [ ${#arr[@]} -lt 1 ]
#     then
#         return $sum
#     else
#         temp=${arr[index]}
#         let sum+=temp
#         unset arr[index]
#         let temp2=index+1
#         text_summation $temp2 $sum
#     fi
# }

# text_summation 0 $sum
# total_sum=$sum
# echo "The summation is: "
# echo "$total_sum"

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
# echo "$total_sum" >> $filename

#4
#this script creates a random array. And sorts it using recursion, and prints the sorted array to a file.
# sort_array(){
#     for (( i = 0; i < 10; i++ ))
#     do
#     number[i]=$RANDOM
#     done
#     for ((i = 0; i<10; i++))
#     do
#         for((j = 0; j<10-i-1; j++))
#         do
#             if [ ${number[j]} -gt ${number[$((j+1))]} ]
#             then
#                 temp=${number[j]}
#                 number[$j]=${number[$((j+1))]}  
#                 number[$((j+1))]=$temp
#             fi
#         done
#     done
# echo ${number[*]}
# }

# filename="question_4.txt"
# sorted_array=$(sort_array)
# echo "Sorted array:"
# echo "${sorted_array[@]}"
# echo  "${sorted_array[*]}" >>$filename