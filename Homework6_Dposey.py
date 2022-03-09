# #Question 1
#This program reads in from a txt file and finds the first name,last name,email, and courses of a student and creates an object of the Student class and puts all the information inside. It then appends 25 students from another assignment to the txt file and sorts all the students combined.
# import re
# class Student:
#     def __init__(self,firstname, lastname,email,all_course):
#         self.__firstname = firstname
#         self.__lastname = lastname
#         self.__email = email
#         self.__all_course = all_course

# def write_contents(student_grade):
#     append_object = open("students.txt",'a')
#     append_object.writelines(student_grade)
#     append_object.write('\n')
    
# if __name__ == '__main__':
#     infile = open("students.txt",'r')
#     all_data = infile.read()
#     find_names = re.findall('([A-Z][a-z]+[a-z])',all_data)
#     find_email = re.findall('[a-z]+@islander.tamucc.edu',all_data)
#     find_courses = re.findall('\d{1,3}',all_data)
#     courses = []
#     names = []
#     first_name = []
#     last_name = []
#     student_courses = []
#     course_data = []
#     students = []
#     student_information = []
#     index = 0
#     for i in range(6,len(find_courses)):
#         courses.append(find_courses[i])
#     for i in range(3,len(find_names)):
#         names.append(find_names[i])
#     for i in range(0,len(names),2):
#         first_name.append(names[i])
#     for i in range(1,len(names),2):
#         last_name.append(names[i])
#     for i in range(0,10):
#         information_courses = []
#         for j in range(0,6):
#             information_courses.append(courses[index])
#             index += 1 
#         student_courses.append(information_courses)
#     for i in range(0,10):
#         info_student = []
#         students.append(Student(first_name[i],last_name[i],find_email[i],student_courses[i]))
        
#     for temp in range(0,25):
#         name_student = ''
#         lst_marks =''
#         name_student += str(input("Please enter the name of the student"))
#         for i  in range(0,6):
#             randnum = str(input("Please the grades for the students 6 courses"))
#             if i > 0:
#                 lst_marks += "," + randnum
#             else:
#                 lst_marks += randnum
#         student_grade = name_student + " " + lst_marks
#         write_contents(student_grade)
#     file_students = open("students.txt",'r')
#     student_data = file_students.read()
#     sorted_data = sorted(student_data)
#     with open('newstudents.txt', 'w') as f:
#         f.write(student_data)
#     infile.close()

# Question 2
# This program will take 3 provided files and write the contents into a single file
# def read_file():
#     file = str(input("Please enter the name of file"))
#     try:
#         infile = open(file,'r')
#         all_data = infile.read()
#         infile.close()
#         return all_data
#     except FileNotFoundError:
#         print("The file was not found")
#     except:
#         print("Something went wrong")

# def write_contents(data):
#     try:
#         append_object = open("final_file.txt",'a')
#         append_object.writelines(data)
#         append_object.writelines('\n')
#         append_object.close()
#     except:
#         print("Something went wrong with the file data")

# if __name__ == '__main__':
#     num_files = int(input("Please enter the number of files you would like for the program to read."))
#     for i in range(0,num_files):
#         data = read_file()
#         write_contents(data)