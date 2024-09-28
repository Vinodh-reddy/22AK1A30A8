def calculate_lucky_number(dob):
    # Split the date of birth into day, month, and year
    day, month, year = map(int, dob.split('/'))
    
    # Calculate the sum of the digits
    total_sum = sum(map(int, str(day) + str(month) + str(year)))
    
    # Reduce the sum to a single digit
    while total_sum > 9:
        total_sum = sum(map(int, str(total_sum)))
    
    return total_sum

# Input date of birth
dob = input("Enter your date of birth (DD/MM/YYYY): ")
lucky_number = calculate_lucky_number(dob)
print(f"Your lucky number is: {lucky_number}")
