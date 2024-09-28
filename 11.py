def read_ten_digit_integer():
    while True:
        number = input("Enter a ten-digit integer: ")
        if number.isdigit() and len(number) == 10:
            return int(number)
        else:
            print("Please enter exactly ten digits.")

# Read two ten-digit integers
print("Enter the first ten-digit integer:")
num1 = read_ten_digit_integer()
print("Enter the second ten-digit integer:")
num2 = read_ten_digit_integer()

# Demonstrate relational operations
print(f"\nRelational operations between {num1} and {num2}:")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} >= {num2}: {num1 >= num2}")
print(f"{num1} <= {num2}: {num1 <= num2}") 

