def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Input range from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print_primes_in_range(start_range, end_range)
