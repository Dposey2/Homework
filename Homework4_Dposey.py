#1
#This progarm creates the employee class and employees dictionary, then outputs a menu for the user to enter what they want to do in the dictionary.
# class Employee:
#     def __init__(self,name,ID_number,department,job_title):
#         self.__name = name
#         self.__ID_number = ID_number
#         self.__department = department
#         self.__job_title = job_title
    
#     def __str__(self):
#         return "Name: % s ID number: % s Department: % s Job Title: % s" % (self.__name,self.__ID_number,self.__department,self.__job_title)


# if __name__ == '__main__':
#         employees = {
#             "47899":Employee("Susan Meyers",47899,"Accounting","Vice President"),
#             "39119":Employee("Mark Jones",39119,"IT","Programmer"),
#             "81774":Employee("Joy Rogers",81774,"Manufacturing","Engineer")
#         }
#         choice = ""
#         while choice.upper() != "Q":
#             print("Please choose a choice, A, B, C, D, or Q to quit")
#             choice = str(input(" A. Look up a person in the dictionary.\n B. Add a new employee to the dictionary.\n C. Change an existing employee's name,department, and job title in the dictionary.\n D. Delete an employee from the dictionary.\n Q. To quit the program\n"))
#             if choice == "A" or choice == "a":
#                 employee_lookup = input(str("Please enter the ID number of the employee you wish to look up\n"))
#                 if employee_lookup in employees:
#                     print(employees[employee_lookup])
                    
#                 else:
#                     print("There is no employee with that ID")
#                     continue
               
#             elif choice == "B" or choice == "b":
#                 new_employee_name = str(input("Please enter the name of the new employee\n"))
#                 ID_number = str(input("Please enter the ID number of the new employee\n"))
#                 new_department = str(input("Please enter the new employees department\n"))
#                 new_job_title = str(input("Please enter the new employees job title\n"))
#                 employees[ID_number] = Employee(new_employee_name, ID_number,new_department,new_job_title)
#                 print("New employee in dictionary: ")
#                 for i  in employees:
#                     print(employees[i])
#             elif choice == "C" or choice == "c":
#                 employee_choice = str(input("Please enter the employee you wish to change\n A. 47899 \n B. 39119 \n C. 81774 \n"))
#                 changed_employee_name = str(input("Please enter the name you would like to change the employee to"))
#                 changed_employee_department = str(input("Please enter the new department"))
#                 changed_employee_job_title = str(input("Please enter the new job title"))
#                 if employee_choice == "A":
#                     employees["47899"] = Employee(changed_employee_name,47899, changed_employee_job_title, changed_employee_department)
#                     print("Employee with changed values")
#                     for i in employees:
#                         print(employees[i])
#                 elif employee_choice == "B":
#                     employees["39119"]= Employee(changed_employee_name,39119, changed_employee_job_title, changed_employee_department)
#                     print("Employee with changed values")
#                     for i in employees:
#                         print(employees[i])
#                 elif employee_choice == "C":
#                     employees["81774"]= Employee(changed_employee_name,81774, changed_employee_job_title, changed_employee_department)
#                     print("Employee with changed values")
#                     for i in employees:
#                         print(employees[i])
#             elif choice == "D" or choice == "d":
#                 employee_delete = str(input("Please enter the employee you wish to delete\n A. 47899 \n B. 39119 \n C. 81774 \n"))
#                 if(employee_delete == "A" or employee_delete == "a"):
#                     del employees["47899"]
#                 elif(employee_delete == "B" or employee_delete == "b"):
#                     del employees["39119"]
#                 elif(employee_choice == "C" or employee_choice == "c"):
#                     del employees["81774"]
#                 print("Dictionary with deleted employee")
#                 for i in employees:
#                     print(employees[i])

#2
#This program gets a list of 20 numbers, and finds the lowest number,  highest number, total of the numbers,  and the average of the numbers.
# lst_nums = []
# for i in range(0,20):
#     num = int(input("Please enter a series of 20 numbers"))
#     lst_nums.append(num)
# print(lst_nums)

# lowest = lst_nums[0]
# for i in range(0,len(lst_nums)):
#     if(lst_nums[i] < lowest):
#         lowest = lst_nums[i]
# print("The lowest number in the list is",lowest)

# highest = lst_nums[0]
# for i in range(0,len(lst_nums)):
#     if(lst_nums[i] > highest):
#         highest = lst_nums[i]
# print("The highest number in the list is",highest)

# total = 0
# for i in range(0,len(lst_nums)):
#     total += lst_nums[i]
# print("The total of the numbers in the list is",total)


#3
#This program asks the user to enter a number and displays all the numbers up to and including that number, with their squared value next to them.
# n = int(input("Please input your max"))
# num_dictionary = dict()
# for i in range(1, n+1):
#     num_dictionary[i] = i * i

# print(num_dictionary)


#4
#This program generates a random list of 100 numbers, and finds the second largest without sorting, it then removes the repeating elemnts in the list and displays it.
import random

def find_highest():
    highest = lst_nums[0]
    second_highest = lst_nums[0]
    for i  in range(0,len(lst_nums)):
        if(lst_nums[i] > highest):
            highest = lst_nums[i]
        if(lst_nums[i] > second_highest and highest != lst_nums[i]):
            second_highest = lst_nums[i]
    return second_highest


    
if __name__ == '__main__':
    lst_nums = []
    count = 0
    for i in range(0,100):
        num = random.randint(0,20)
        lst_nums.append(num)
    print(lst_nums)
    print("The second largest number in the list is:", find_highest())

    new_lst_nums = []
    for i in lst_nums:
        if i not in new_lst_nums:
            new_lst_nums.append(i)
            
    
    print("The new list without duplicates:\n",new_lst_nums)
