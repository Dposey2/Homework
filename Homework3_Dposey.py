# class car:
#     def __init__(self, year, make, speed):
#         self.__year_model = year
#         self.__make = make
#         self.__speed = 0
    
#     def accelerate(self):
#         self.__speed +=  5
    
#     def brake(self):
#         self.__speed -=  5
    
#     def car_type(self):
#         print("The year model of the car is ",year,"and the make of the car is",make)

#     def get_speed(self):
#         return self.__speed


# if __name__ == '__main__':
#     year = input("Please enter the year model of the car")
#     make = input(str("Please enter the make of the car"))
#     speed = 0
#     my_car = car(year,make,speed)

#     my_car.car_type()
#     print("The car is accelerating: ")
#     for i in range(0,5):
#         print("The current speed is",my_car.get_speed())
#         my_car.accelerate()
#     print("The car is braking: ")
#     for i in range(0,5):
#         print("The current speed is",my_car.get_speed())
#         my_car.brake()


# class Employee:
#     def __init__(self,name,ID_number,department,job_title):
#         self.__name = name
#         self.__ID_number = ID_number
#         self.__department = department
#         self.__job_title = job_title
    
#     def __str__(self):
#         return "Name: % s ID number: % s Department: % s Job Title: % s" % (self.__name,self.__ID_number,self.__department,self.__job_title)

# if __name__ == '__main__':
#     Employee_1 = Employee("Susan Meyers",47899,"Accounting","Vice President")
#     Employee_2 = Employee("Mark Jones",39119,"IT","Programmer")
#     Employee_3 = Employee("Joy Rogers",81774,"Manufacturing","Engineer")
#     print(Employee_1)
#     print(Employee_2)
#     print(Employee_3)


# class Employee:
#     def __init__(self,first,last):
#         self.__fullname = first + " " + last
#         self.__first = first
#         self.__last = last
    
#     def __str__(self):
#         return (self.__fullname)
    
#     def get_email(self):
#         print(self.__first.lower() + "." + self.__last.lower() + "@company.com")



# if __name__ == '__main__':
#     Employee_1 = Employee("Sander","Fleming")
#     Employee_2 = Employee("Dylan","Posey")
#     Employee_3 = Employee("Gilbert","Garcia")
#     print("The employees full name is" ,Employee_1)
#     print("The employees full name is" ,Employee_2)
#     print("The employees full name is" ,Employee_3)
#     Employee_1.get_email()
#     Employee_2.get_email()
#     Employee_3.get_email()

# import random
# class Student:
#     def __init__(self,name,marks):
#         self.__name = name
#         self.__marks = marks


# if __name__ == '__main__':
#     lst_marks = []
#     lst_Students = []
#     lst_average = []
#     total_sum = 0

#     for temp  in range(0,25):
#         lst_marks = []
#         name_Student = Student("Please enter the name of the student",lst_marks)
#         lst_Students.append(name_Student)
#         for i  in range(0,6):
#             randnum = random.randint(0,100)
#             lst_marks.append(randnum)
#         for i in range(0,6):
#             total_sum = 0
#             total_sum += lst_marks[i]
#         print("The total score of student",temp+1 , "is:",total_sum + "%")
#         lst_average.append(total_sum/600)

    
#     for i in range(0,len(lst_average)-1):
#         smallest = i
#     for j in range(i+1,len(lst_average)):
#         if lst_average[j] < lst_average[smallest]:
#             smallest = j
#     temp = lst_average[i]
#     lst_average[i] = lst_average[smallest]
#     lst_average[smallest] = temp


    




