# Function to add two complex numbers
def add_complex(z1, z2):
    return z1 + z2

# Function to subtract two complex numbers
def subtract_complex(z1, z2):
    return z1 - z2

# Function to multiply two complex numbers
def multiply_complex(z1, z2):
    return z1 * z2

# Function to conjugate a complex number
def conjugate_complex(z):
    return z.conjugate()

# Read two complex numbers from the user
z1 = complex(input("Enter the first complex number (e.g., 2+3j): "))
z2 = complex(input("Enter the second complex number (e.g., 1+2j): "))

# Perform operations
addition = add_complex(z1, z2)
subtraction = subtract_complex(z1, z2)
multiplication = multiply_complex(z1, z2)
conjugation_z1 = conjugate_complex(z1)
conjugation_z2 = conjugate_complex(z2)

# Print results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Conjugation of {z1}: {conjugation_z1}")
print(f"Conjugation of {z2}: {conjugation_z2}")
