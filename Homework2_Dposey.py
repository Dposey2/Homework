# #1
# # This program outputs a specified pattern and displays it the opposite way, both using loops.
# for temp in range(1,6):
#     for temp2 in range(0,temp):
#         print("*",end=" ")
#     print("")

# print("")
# for temp in range(5, 0, -1):
#     for temp2 in range(temp, 1, -1):
#         print(" ",end=" ")
#     for temp2 in range(temp, 6):
#         print("*",end=" ")
#     print()

# #2
# #This program takes 2 integer inputs from the user and puts them through 2 calculations and displays the output
# from math import factorial

# int_r = int(input("Please enter the number for r"))
# int_n = int(input("Please enter the number for n (must be bigger than or equal to r)"))
# # ii)
# equation_1 = factorial(int_n)/(factorial(int_r)*factorial(int_n - int_r))
# print("The number of possible equations is",equation_1)
# equation_2 = factorial(int_n)/(factorial(int_n-int_r))
# print("The number of possible subsets is",equation_2)


# #3
# #This program takes a list and sorts it using a loop. It then displays this new list.
# lst_nums = [20,68,41,88,16,40,65,97,85]
# print("Old list",lst_nums)
# for i in range(0,len(lst_nums)-1):
#     smallest = i
#     for j in range(i+1,len(lst_nums)):
#         if lst_nums[j] < lst_nums[smallest]:
#             smallest = j
#     temp = lst_nums[i]
#     lst_nums[i] = lst_nums[smallest]
#     lst_nums[smallest] = temp

# print("New list",lst_nums)

# #4
# #This program takes a list and finds the sum of all elements in that list, it then creates a new list which only contains the even numbers and finds the sum of that list, it does the same for odd numbers.
# lst_nums = [20,68,41,88,16,40,65,97,85]
# lst_even_nums = []
# lst_odd_nums = []
# sum = 0
# for i in range(0,len(lst_nums)):
#     sum = sum + lst_nums[i]
# print("The sum of the original list is",sum)

# for i in range(0,len(lst_nums)):
#     if lst_nums[i] % 2 == 0:
#         lst_even_nums.append(lst_nums[i])

# sum_e = 0
# for i in range(0,len(lst_even_nums)):
#     sum_e = lst_even_nums[i] + sum_e

# print("List of even numbers",lst_even_nums)
# print("Sum of the even list",sum_e)

# for i in range(0,len(lst_nums)):
#     if lst_nums[i] % 2 == 1:
#         lst_odd_nums.append(lst_nums[i])

# sum_o = 0
# for i in range(0,len(lst_odd_nums)):
#     sum_o = lst_odd_nums[i] + sum_o

# print("List of even numbers",lst_odd_nums)
# print("Sum of the even list",sum_o)

# #5
# #This program finds all the prime numbers between 2 and 50 and prints them.
# for i in range(2,51):
#         for j in range(2,i):
#             if (i % j) == 0: 
#                 break
#         else:
#             print(i, end = " ")


#6 
#This program puts question 1,2, and 3 into functions 
def question_1():
    for temp in range(1,6):
        for temp2 in range(0,temp):
            print("*",end=" ")
        print("")

    print("")
    for temp in range(5, 0, -1):
        for temp2 in range(temp, 1, -1):
            print(" ",end=" ")
        for temp2 in range(temp, 6):
            print("*",end=" ")
        print()


def question_2(int_n,int_r):
    from math import factorial
    print("The number of possible equations is",factorial(int_n)/(factorial(int_r)*factorial(int_n - int_r)))
    print("The number of possible subsets is",factorial(int_n)/(factorial(int_n-int_r)))

int_r = int(input("Please enter the number for r"))
int_n = int(input("Please enter the number for n (must be bigger than or equal to r)"))
if int_r < 0 or int_n < 0:
    while int_r < 0 or int_n < 0:
        print("Please enter a positive values only")
        int_r = int(input("Please enter the number for r"))
        int_n = int(input("Please enter the number for n (must be bigger than or equal to r)"))
        

def question_3(lst_nums):
    print("Old list",lst_nums)
    for i in range(0,len(lst_nums)-1):
        smallest = i
        for j in range(i+1,len(lst_nums)):
            if lst_nums[j] < lst_nums[smallest]:
                smallest = j
        temp = lst_nums[i]
        lst_nums[i] = lst_nums[smallest]
        lst_nums[smallest] = temp

    print("New list",lst_nums)

lst_nums = [20,68,41,88,16,40,65,97,85]

if __name__ == '__main__':
    question_1()
    question_2(int_n,int_r)
    question_3(lst_nums)

# #9
# #This program only prints the even numbers in the range (1,10)
# loop_counter = 1
# while loop_counter <= 10:
#     if loop_counter%2 == 0:
#             print(loop_counter)
#     loop_counter += 1 #Here we are increasing loop count by 1
