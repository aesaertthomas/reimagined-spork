#Ex 02 
#Thomas Aesaert 1CTAI1
# schrijf hier jouw functies/Write here your functions.

def give_average_months(months : list, spending_dictionary : dict) -> float:
    sum = 0.0
    for month in months:
        sum += spending_dictionary[month] #Add the value corresponding to the month to the total sumation amount
    return round((sum / len(months)),2)
        

def give_expensive_months(spending_dictionary : dict, minimum_amount : float) -> list:
    
    expensive_month_list = []
    for month, amount_spent in spending_dictionary.items(): #get keys and corresponding values
        if amount_spent >= minimum_amount: #if the value surpasses or is equal to the minimum amount. The month is added to the list
            expensive_month_list.append(month) 
    
    return expensive_month_list


#ENG - Test your functions
dict_entertainment_expenses = {
    'January': 30.5,
    'February': 25.0,
    'March': 60.5,
    'April': 55.0,
    'May': 45.5,
    'June': 20.0,
    'July': 120.5,
    'August': 65.0,
    'September': 150.5,
    'October': 115.0,
    'November': 60.5,
    'December': 85.0
}
min = float(input("Specify the minimum amount to filter the months:>"))
expensive_months = give_expensive_months(dict_entertainment_expenses, min)
print(f"The months above {min}€ are {expensive_months}")


average_cost = give_average_months(spending_dictionary=dict_entertainment_expenses, months=expensive_months)
print(f"The average cost in these months is: {average_cost}")
