# Use this file to code your solution for Task 8: Unit Converter - Improved
# Name:                 UnitConvertorImproved.py
# Author:               Meetkumar Patel
# Date Created:         March 20, 2022
# Date Last Modified:   March 20, 2022

# Purpose:
#
#In this program we were to use the functions and help in the unit conversion of either the weight or length whihc is to be selected by the user.
#This is the welcome screen and will also show the options of the conversion that is weight and length.

#Below are variables that store the unit used in conversion
#Variables for the  unit
unit1 = "kg"
unit2 = "lb"
unit3 = "m"
unit4 = "ft"
## Function

#Function: conversion1
#Description: This function will help convert the value given by user from kg to lb and lb to kg.
#Parameters: 
#          weight: weight(Float)
#          unit : unit (kg or lb)
#Return value:
#           weight, unit
def conversion1(weight, unit):
    if unit == unit1:
        conv1 = weight * 2.20462
        print("{0:,.2f}{1:s}{2:^5s}{3:,.2f}{4:2^s}".format(weight, unit.center(4), "is", conv1, unit2.center(4)))
    elif unit == unit2:
        conv2 = weight * 0.453592
        print("{0:,.2f}{1:s}{2:^5s}{3:,.2f}{4:2^s}".format(weight, unit.center(4), "is", conv2, unit1.center(4)))
    else:
        print("The unit choosen is not found!!")
    return weight, unit


#Function: conversion2
#Description: This function will help convert the value given by user from m to ft and ft to m.
#Parameters: 
#          length: length(number)
#          unit: unit(m of ft)
#Return value:
#           length, unit

def conversion2(length, unit):
    if unit == unit3:
        conv1 = length * 3.28084
        print("{0:,.2f}{1:2^s}{2:^5s}{3:,.2f}{4:2^s}".format(length, unit.center(4), "is", conv1, unit4.center(4)))
    elif unit == unit4:
        conv2 = length * 0.3048
        print("{0:,.2f}{1:2^s}{2:^5s}{3:,.2f}{4:2^s}".format(length, unit.center(4), "is", conv2, unit3.center(4)))
    else:
        print("The unit choosen is not found!!!")
    return length, unit

#Function: userIntegerChecker
#Description: This function check if an  integer was given or not if integer an error is raised.
#Parameters: 
#          word(The user input paramenter)
#Return value:
#           num(Gives back a number 1 or 2 for user selection.)
def userIntergerChecker(word):
    try:
        num = input(word)
        num = int(num)
        if num > 2:
            raise Exception
    except ValueError:
        print("The option must be number selected") 
    except Exception:
        print("The option selected is currently not available.")
        
    return (num)

#Function: floatChecker
#Description: In this function checks the user input 
#Parameters: 
#          word(The user input paramenter)
#Return value:
#           x(Gives a float number)
def floatChecker(word):
    while True:
        try:
            x = float(input(word))
            if x <= 0:
                raise Exception 
            break
        except ValueError:
            print("The value you provide is a non-numeric value!")
        except Exception:
            print("Value is less than zero!")

    
    return x


#Function: userWordChecker
#Description: In this function the  input will check if there is any integer given and error is 
#raised then it will also check if the inout given is in the condition.
#Parameters: 
#          z is input
#          y is the condition to check(1,2)
#Return value:
#           w this is the option selected as per the user.
def userWordChecker(z,y):
    w = input(z)
    try:
        if w.isdecimal():
            raise Exception
    except Exception:
        print("The value should be in letter not numeric!!")
        w = w.lower().strip()
    while w not in y:
        print("The Unit is not found")
        w = input(z)
        try:
            if w.isdecimal():
                raise Exception
        except Exception:
            print("The value should be in letter not numeric!!")
        w = w.lower().strip()

    return(w)

#Here the user is given an option

print("This program will help you in Converssion.")
print("We provide two types of coversion\n\
    1 - Weight Conversion\n\
    2 - Length Conversion")

#Here user will be asked to get user option selection 
userSelection = userIntergerChecker("Please select from the options given: ")
while userSelection not in (1,2):
    userSelection = userIntergerChecker("Please select from the options given: ")

#Here the code checks the user selection and call the functions acordingly
#Firstly if user selects option 1 then function conversion1 is called
if userSelection == 1:
    unit = userWordChecker("Please enter your unit of measurement [Either in kg(Kilogram) or lb(Pounds)] : ",("kg","lb"))
    weight = floatChecker("Please Enter the weight of the object being measured : ")
    conversion1(weight, unit) #calling of function
elif userSelection == 2:
    unit = userWordChecker("Please enter your unit of measurement [Either in m(Meters) or ft(Foot)] : ", ("m","ft"))
    length = floatChecker("Please Enter the Length of the object being measured : ")
    conversion2(length, unit) #calling of function
else:
    print("The Selection done ws not found.")