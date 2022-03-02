#Question 1
# morse_code_str = ' '
# norm_string = str(input("Please eneter a string you want to be translated into morse code"))
# morse_code = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...','8':'---..','9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-','?':'..--..'
# }

# for i in norm_string:
#     if i != ' ':
#         morse_code_str += morse_code[i.upper()] + ' '
#     else:
#         morse_code_str += ' '

# print("Nomral string:")
# print(norm_string)
# print("Modified string:")
# print(morse_code_str)

#Question 2
# def find_vowels(input_string):
#     vowel_count = 0
#     for i in input_string:
#         if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y' and i != ' ':
#             vowel_count += 1
#     return vowel_count

# def find_consonant(input_string):
#     consonant_count = 0
#     for i in input_string:
#         if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != 'y' and i != ' ':
#             consonant_count += 1
#     return consonant_count

# if __name__ in '__main__':
#     input_string = str(input("Please input a string"))
#     print("The number of vowels are:", find_vowels(input_string))
#     print("The number of consonants are:",find_consonant(input_string))


#Question 3

# #1
# def find_digits(str1):

#     num_digits = 0
#     for i in str1:
#         if i != ' ':
#             if i.isdigit():
#                 num_digits += 1
#     return num_digits

# def find_letters(str1):
#     num_letters = 0
#     for i in str1:
#         if i != ' ':
#             if i.isalpha():
#                 num_letters += 1
#     return num_letters

# def find_symbols(str1):
#     num_symbols = 0
#     for i in str1:
#         if i != ' ':
#             if not i.isalnum():
#                 num_symbols += 1
#     return num_symbols


# if __name__ in '__main__':
#     str1 = "P@#yn26at^&i5ve"
#     print("Number of letters", find_letters(str1))
#     print("Number of digits",find_digits(str1))
#     print("Number of symbols", find_symbols(str1))

# #2
# str1 = "/*Jon is @developer & musician"
# modified_str = ' '
# for i in str1:
#     if i.isalnum() and i != ' ':
#         modified_str += i
#     elif i == ' ':
#         modified_str += ' '

# print(modified_str)

# #3 
# str1 = "Emma-is-a-data-scientist"
# modified_str = ''
# modified_str += str1.replace('-', ' ')
# print(modified_str)

# #4 
# str1 = "Hello, have a good day"
# modified_str = " "
# vowels = ['a','e','i','o','u','A','E','I','O','U',]                       
# for i in str1:                             
#     if i not in vowels and i != ' ':                                 
#         continue               
#     else:                 
#         modified_str=modified_str+i      
# print(modified_str)

# #Question 4
# import statistics

# lst_nums = []
# for i in range(0,20):
#     num = int(input("Please enter 20 integers from 0 to 100 inclusive"))
#     while(num > 100 or num < 0):
#         print("Please input a valid number")
#         num = int(input("Please enter an integer from 0 to 100"))
#     lst_nums.append(num)

# total = 0
# for i in range(0,20):
#     total += lst_nums[i]

# average = total/20
# print("The average is: ",average)
# lst_nums.sort()
# mid = len(lst_nums)
# median = statistics.median(lst_nums)
# print("The median is: ", median)
# std_deviation = statistics.stdev(lst_nums)
# print("The standard deviation is:",std_deviation)

# new_lst_nums = []
# for i in range(0,20): 
#     if i != 19:
#         new_num = lst_nums[i]/lst_nums[i+1]
#     new_lst_nums.append("{:.2f}".format(new_num))
# print("The new list is:")
# print(new_lst_nums)

#Question 5
str1 = "this is the string for the class"
#1
count = 0
modified_str = ''
for i in range(0,len(str1)):
    if i == 0 or i == 5 or i == 8 or i ==12 or i == 19 or i == 23 or i == 27:
        modified_str += str1[i].upper()
    else:
        modified_str += str1[i]
print(modified_str)
#2
for i in range(len(modified_str)-1,-1,-1):
    if modified_str[i] == ' ':
        modified_str = modified_str[:i] + modified_str[i+1:]
    
print(modified_str)

#3

for i in range(0,len(str1)):
    if i == 3 or i == 6 or i == 11 or i == 12 or i == 30 or i == 31:
        modified_str = modified_str.replace(str1[i],'$')

print(modified_str)

#4
for i in range(0,len(modified_str)):
    if i == 3 or i == 6 or i == 12 or i == 30 or i == 31:
        modified_str = modified_str.replace(str1[i],'s')

print(modified_str)