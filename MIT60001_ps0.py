# -*- coding: utf-8 -*-
"""
Created on Thurs Oct 17 23:34:34 2019

@author: David Babbs
"""
# Write a program that does the following in order: 

#1. Asks the user to enter a number “x” 
#2. Asks the user to enter a number “y”  
#3. Prints out number “x”, raised to the power “y”. 
#4. Prints out the log (base 2) of “x”
import numpy

x = int(input("Hi there! Please enter the value of x: " ))
y = int(input("Thank you! Please now enter value of y: "))
print("x to the power of y is: ", x**y)
print("log base 2 of x is: " +str(numpy.log2(x)))