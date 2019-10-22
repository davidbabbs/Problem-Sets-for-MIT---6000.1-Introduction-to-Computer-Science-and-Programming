# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:09:03 2019

@author: David Babbs
"""

annual_salary = int(input("Enter your annual salary: "))
percentage_saved = int(input("Enter the proportion of your salary you are planning to save (as a percentage): "))
total_cost = int(input("Enter the cost of your dream home: "))
annual_interest_on_savings_as_percentage = float(input("Enter the interest rate you're getting on your savings: "))
current_savings = int(input("Enter your current savings to the nearest pound: "))
semi_annual_raise_as_percentage = float(input("Enter your anticipated semi annual raise (as a percentage): "))

portion_saved=percentage_saved/100
monthly_interest_on_savings = annual_interest_on_savings_as_percentage/100/12
monthly_contrib_to_savings_from_salary = annual_salary/12*portion_saved
monthy_contrib_to_savings_from_interest = current_savings*monthly_interest_on_savings
semi_annual_raise= semi_annual_raise_as_percentage/100

required_down_payment=total_cost*0.25


number_months = 0.0

while current_savings < required_down_payment:
    number_months += 1
    current_savings *=(1+monthly_interest_on_savings)
    current_savings += monthly_contrib_to_savings_from_salary
    if number_months%6==0:
        annual_salary *= (1+semi_annual_raise)
        monthly_contrib_to_savings_from_salary = annual_salary/12*portion_saved

    
number_of_years_required = int(number_months/12)
remainder_months = number_months%12

print()
print()

if number_of_years_required >= 1:
    
    print("It will take you " + str((number_of_years_required)) + " years and " +str(round(remainder_months)) +" months to save your deposit")
else: print("number of months required to save your deposit:   " +str(number_months))
