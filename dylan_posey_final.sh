#!/bin/bash
#Problem 3
# sort_array(){
#     for(( i=0; i<10; i++))
#     do 
#     number
# }
# count=0
# for((i=0;i<30;i++))
# do
#     numbers[$i]=$RANDOM
# done
# echo "${numbers[@]}"

#problem 7
#for loop
# echo "For loop"
# for (( i=100; i <= 1000; i++))
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
#         echo $i
#     fi
# done

# #While loop
# echo "While loop"
# i=100
# j=1000
# prime=0
# tem_1=100
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

#until loop
# echo "Until loop"
# i=100
# j=1000
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

#Problem 8
# #while loop
# echo "While loop"
# i=50
# sum_while=0
# while [ $i -le 100 ]
# do
#    if [ $((i%2)) -eq 0 ]
#    then
#         let "sum_while+=i"
#         let "i++"
#    fi
#    let "i++"
# done
# echo $sum_while

# #until loop
# echo "Until loop"
# j=50
# sum_until=0
# until [ $j -ge 100 ]
# do
#    if [ $((j%2)) -eq 0 ]
#    then
#         let "sum_until+=j"
#         let "j++"
#    fi
#     let "j++"
# done
# let "sum_until+=j"
# echo $sum_until

# #for loop
# echo "For loop"
# sum_for=0
# for (( k=50; k <= 100; k++))
# do
#    if [ $((k%2)) -eq 0 ]
#    then
#         let "sum_for+=k"
#    fi
# done
# echo $sum_for

#Odd
#while loop
# echo "While loop"
# i=50
# sum_while=0
# while [ $i -le 100 ]
# do
#    if [ $((i%2)) -eq 1 ]
#    then
#         let "sum_while+=i"
#         let "i++"
#    fi
#    let "i++"
# done
# echo $sum_while

# #until loop
# echo "Until loop"
# j=50
# sum_until=0
# until [ $j -ge 100 ]
# do
#    if [ $((j%2)) -eq 1 ]
#    then
#         let "sum_until+=j"
#         let "j++"
#    fi
#     let "j++"
# done
# let "sum_until+=j"
# echo $sum_until

# #for loop
# echo "For loop"
# sum_for=0
# for (( k=50; k <= 100; k++))
# do
#    if [ $((k%2)) -eq 1 ]
#    then
#         let "sum_for+=k"
#    fi
# done
# echo $sum_for

#Problem 9
# for((i=0;i<20;i++))
# do
#     numbers[$i]=$RANDOM
# done
# echo "${numbers[@]}"
# for ((i = 0; i<20; i++))
# do
    
#     for((j = 0; j<20-i-1; j++))
#     do
    
#         if [ ${numbers[j]} -gt ${numbers[$((j+1))]} ]
#         then
#             # swap
#             temp=${numbers[j]}
#             numbers[$j]=${numbers[$((j+1))]}  
#             numbers[$((j+1))]=$temp
#         fi
#     done
# done

# echo "Array in sorted order :"
# echo ${numbers[*]}

#Problem 10
problem_10(){
    num1=$1
    num2=$2
    num=0
    echo "Summation:"
    echo $((num1+num2))
    echo "Subtraction:"
    echo $((num1-num2))
    echo "Multiplication:"
    echo $((num1*num2))
    echo "Exponential:"
    echo $((num1**num2))
}
echo "Please enter a number"
read num1
echo "Please enter another number"
read num2
problem_10 $num1 $num2