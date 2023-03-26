# Name:                 UnitConvertor.py
# Author:               Meetkumar Patel
# Date Created:         Februarey 20, 2022
# Date Last Modified:   Februaury 27, 2022

# Purpose:
#
#In this program we were to use the functions and help in the unit conversion of either the weight or length whihc is to be selected by the user.
#This is the welcome screen and will also show the options of the conversion that is weight and length.
print("This program will help you in Coverssion.")
print("We provide two types of coversion\n\
    1 - Weight Conversion\n\
    2 - Length Conversion")
#Here user will be asked to get user option selection 
user_Selection = int(input("Please Select 1 or 2: "))


#Below are variables that store the unit used in conversion
#Variables for the  unit
unit1 = "kg"
unit2 = "lb"
unit3 = "m"
unit4 = "ft"

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

#Here the code checks the user selection and call the functions acordingly
#Firstly if user selects option 1 then function conversion1 is called
if user_Selection == 1:
    weight = float(input("Please Enter the weight of the object being measured : "))
    unit = input("Please enter your unit of measurement [Either in kg(Kilogram) or lb(Pounds)] : ")
    conversion1(weight, unit) #calling of function
elif user_Selection == 2:
    length = float(input("Please Enter the Length of the object being measured : "))
    unit = input("Please enter your unit of measurement [Either in m(Meters) or ft(Foot)] : ")
    conversion2(length, unit) #calling of function
else:
    print("The Selection done ws not found.")