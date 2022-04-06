#!/bin/bash
clear

<<com
#Problem 1
#This script prints "This is assignment 7"
echo "This is assignment 7"
com

<<com
#Problem 2
#This script prints my name and the courses I am taking.
my_name="Dylan Posey"
course_1="Intro to Scripting"
course_2="Into to Problem Solving"
course_3="Writing and Rhetoric"
course_4="Discrete Mathematics"
echo $my_name
echo "Enrolled in: $course_1,$course_2,$course_3,$course_4"
com

<<com
#Problem 3 
#This script does the same thing as problem 2 just with special variables
echo "Name: $1"
echo "Enrolled in: $2, $3, $4, $5"
com

<<com
#Problem 4
#This script shows the current process number of the shell, and all the arguements that are passed.
echo "Current process number of the shell: $$"
echo "All arguements passed: $*"
com

#Problem 5
#This script gets a random number from 0 to 100 and prints the letter grade for that specific number
<<com
RANDOM=$$
rand_num=$((RANDOM%100))
echo $rand_num
if [[ $rand_num -ge 90 && $rand_num -le 100 ]]
then
	echo A
elif [[ $rand_num -ge 80 && $rand_num -le 90 ]]
then
	echo B
elif [[ $rand_num -ge 70 && $rand_num -le 80 ]]
then
	echo C
elif [[ $rand_num -ge 60 && $rand_num -le 70 ]] 
then
	echo D
else
	echo Fail
fi
com


#Problem 6
#This script uses a few number, and performs  addition, subtraction, multiplication, and division, and also shows increment
<<com
num_1=40
num_2=20
echo $((num_1+num_2))
echo $((num_1-num_2))
echo $((num_1*num_2))
echo $((num_1/num_2)) #Not sure why this is giving an error of dividing by zero when it is commented out.
echo "Original numbers: $num_1, $num_2"
let "num_1++"
let "num_2--"
echo "Numbers after increment and decrement: $num_1,$num_2"
com


#Problem 7
#This scipt gets the basic salary of the user and calculates the gross salary according to specific conditions.
<<com
echo "Please enter your salary"
read employee_salary
if [ $employee_salary -le 10000 ]
then
	HRA=$(((employee_salary*20)/100))
	DA=$(((employee_salary*80)/100))
elif [[ $employee_salary -gt 10000 && $employee_salar -le 20000 ]]
then
	HRA=$(((employee_salary*25)/100))
	DA=$(((employee_salary*90)/100))
else
	HRA=$(((employee_salary*30)/100))
	DA=$(((employee_salary*80)/100))
fi

gross_salary=$((employee_salary+HRA+DA))
echo "The gross salary of the employee is: $gross_salary"
com



































