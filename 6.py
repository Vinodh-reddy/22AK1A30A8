# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over digits
    num_str = str(number)
    # Calculate the number of digits
    num_digits = len(num_str)
    # Initialize the sum
    sum_of_powers = 0
    
    # Calculate the sum of each digit raised to the power of the number of digits
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Read a number from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
