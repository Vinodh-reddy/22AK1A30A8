def classify_number(n):
    # Function to calculate the sum of proper divisors
    def sum_of_divisors(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors)

    # Calculate the sum of proper divisors
    sum_div = sum_of_divisors(n)

    # Classify the number
    if sum_div > n:
        return f"{n} is an abundant number."
    elif sum_div < n:
        return f"{n} is a deficient number."
    else:
        return f"{n} is a perfect number."

# Input from the user
number = int(input("Enter a number: "))
result = classify_number(number)
print(result)
