#1
#This program will display my name, address,city,state,ZIP, and college major.
print("Name: Dylan Posey , Address: 6300 Ocean Dr, City: Corpus Christi, State: Texas, ZIP: 78412, Telephone number: 361-331-5125, College major: Computer Science")

#2
#This program will ask the user to enter total square ft in a tract of land and calculates the number of acres in the tract.
total_sqft = int(input("Please enter the total square feet in a tract of land "))
total_acres = total_sqft/43560
print("The total amount of acres in the tract is:", total_acres)

#3
#This program calculates the number of miles a car will travel going 70mph in 6,10,and 15 hours.
lst_time = [6,10,15]
speed = 70
print("The distance the car will travel in 6 hours is", speed*lst_time[0], "miles")
print("The distance the car will travel in 10 hours is", speed*lst_time[1], "miles")
print("The distance the car will travel in 15 hours is", speed*lst_time[2], "miles")


#4
#This program prompts the user for a persons age and displays whether or not the person is an infant, child, teenager, or adult
age = int(input("Please enter the person's age"))
if age <= 1:
    print("He or she is an infant")
elif age > 1 and age < 13:
    print("He or she is a child")
elif age >= 13 and age < 20:
    print("He or she is a teenager")
else:
    print("He or she is an adult")

#5
#This program asks the user to enter the number of pennies, quarters, nickels, and dimes. Then checks if the total value is equal to a dollor, otherwise it will display if it was more or less.
num_pennies = int(input("Please enter the number of pennies"))
num_quarters = int(input("Please enter the number of quarters"))
num_nickels = int(input("Please enter the number of nickels"))
num_dimes = int(input("Please enter the number of dimes"))

total = (num_quarters*.25) + (num_dimes*.10) + (num_pennies*.01) + (num_nickels*.05)
if total == 1.0:
    print("Congrats you have won the game")
elif total > 1.0:
    print("Sorry. You have gone over one dollar")
else:
    print("Sorry. You have gone under a dollar")

#6
#This program prompts the user to enter a year and determines if the year is a leap year or not.
year = int(input("Please enter a year"))
if year%100 == 0 and year%400 == 0:
    print("There are 29 days in Febuary")
elif year%100 > 0 and year % 4 == 0:
    print("There are 29 days in Febuary")
else:
    print("There are 28 days in Febuary")

#7
#This program prompts the user for their weight and height and then calculates the bmi and displays whether or not the person has optimal weight, is underweight, or is overweight.
weight = int(input("Please enter your weight in lbs"))
height = float(input("Please enter your height in inches"))
body_mass_index = weight*703/height**2
print(body_mass_index)
if body_mass_index >= 18.5 and body_mass_index < 25:
    print("Your body weight is optimal")
elif body_mass_index < 18.5:
    print("Your body weight is underweight")
elif body_mass_index > 25:
    print("Your body weight is overweight")