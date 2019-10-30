
semi_annual_raise = 0.07
annual_rate_of_return = 0.04
portion_down_payment = 0.25
total_cost = 1000000
target_months = 36

target_savings = total_cost * portion_down_payment

annual_salary = float(input("Enter the starting salary: "))
monthly_salary = annual_salary/12.0
current_savings = 0

epsilon = 100
low_rate = 0
high_rate = 100
guess_rate = (high_rate + low_rate)/2
num_months = 0
steps = 0

while(abs(target_savings - current_savings)) >= epsilon:
    current_savings = 0
    monthly_salary = annual_salary/12.0
    for num_months in range(36):
        current_savings *= (1+ (annual_rate_of_return/12))
        monthly_saving = monthly_salary * (guess_rate/100)
        current_savings += monthly_saving
        if((num_months) % 6 == 0) and (num_months >= 6):
                monthly_salary *= (1 + semi_annual_raise)
    steps += 1

    
    if(current_savings > target_savings): 
        high_rate = guess_rate
    elif (current_savings < target_savings): 
        low_rate = guess_rate
    guess_rate = (high_rate + low_rate)/2
    
    if(guess_rate >=100):
        break
    
if(guess_rate >=100):
    print('It is not possible to pay down payment in three years')
else:
    print('Best Saving Rate: ', round(guess_rate,2), '%')
    print('Steps in bisection search: ', steps)

