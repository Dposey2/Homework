#!bin/bash/
clear
#Question 1 - This script creates an array of size 20 using random elements, and sorts them from lowest number to highest number using a for loop.
# for(( i = 0; i < 20; i++ ))
# do
#     numbers[$i]=$RANDOM
# done
# echo "Array not sorted"
# echo "${numbers[@]}"
# for ((i = 0; i<20; i++))
# do
#     for((j = 0; j<20-i-1; j++))
#     do
#         if [ ${numbers[j]} -gt ${numbers[$((j+1))]} ]
#         then
#             temp=${numbers[j]}
#             numbers[$j]=${numbers[$((j+1))]}  
#             numbers[$((j+1))]=$temp
#         fi
#     done
# done

# echo "Array in sorted order (lowest to highest)"
# echo "${numbers[@]}"

#Question 2 - This script does the same thing as question 1 just from highest to lowest
# for(( i = 0; i < 20; i++ ))
# do
#     numbers[$i]=$RANDOM
# done
# echo "Array not sorted"
# echo "${numbers[@]}"
# for ((i = 0; i<20; i++))
# do
#     for((j = 0; j<20-i-1; j++))
#     do
#         if [ ${numbers[j]} -lt ${numbers[$((j+1))]} ]
#         then
#             temp=${numbers[j]}
#             numbers[$j]=${numbers[$((j+1))]}  
#             numbers[$((j+1))]=$temp
#         fi
#     done
# done

# echo "Array in sorted order (highest to lowest)"
# echo "${numbers[@]}"

#Question 3 - This script creates an array with numbers 1 to 50
# value=($(seq 1 50))
# echo "Array with values 1-50"
# echo "${value[@]}"

#Question 4 - This script uses a method to find the prime numbers 1-50, then using another method it finds the summation of those numbers.

# get_primes(){
#     count=0
#     for (( i=2; i <= 50; i++))
#     do
#         prime=0
#         for j in $(seq 2 $(expr $i - 1))
#         do 
#             if [ $(expr $i % $j) -eq 0 ]
#             then
#                 prime=1
#                 break
#             fi
#         done
#         if [ $prime -eq 0 ]
#         then
#         let count++
#         prime_values[count]=$i
#         fi
#     done
#     echo "${prime_values[@]}"
#     sum=0
#     for i in "${prime_values[@]}";
#     do
#         let "sum+=i"
#     done
#     echo "The summation of prime numbers 1-50 is $sum"
# }

# get_primes


#Question 5 - This script creates 2 arrays of odd and even numbers 1-50 and finds the summation of both.
#Odd
# sum_idd=0
# count=0
# for (( i = 1; i < 50; i=i+2 ))
# do
#     odd_numbers[count]=$i
#     let sum_odd+=odd_numbers[count]
#     let count++
# done
# echo "${odd_numbers[@]}"
# echo "Summation of odd: $sum_odd"

# #even
# sum_even=0
# count_2=0
# for (( i = 2; i < 50; i=i+2))
# do
#     even_numbers[count_2]=$i
#     let sum_even+=even_numbers[count_2]
#     let count_2++
# done
# echo "${even_numbers[@]}"
# echo "Summation of even: $sum_even"