import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def fibonacci_position(n):
    if n == 0:
        return 1
    a, b = 0, 1
    position = 1
    while b <= n:
        if b == n:
            return position + 1
        a, b = b, a + b
        position += 1
    return -1

# Input number
num = int(input("Enter an integer: "))

if is_fibonacci(num):
    position = fibonacci_position(num)
    print(f"{num} is a Fibonacci number at position {position}.")
else:
    print(f"{num} is not a Fibonacci number.")
