def print_even_length_substrings(s):
    # Iterate over all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            # Check if the length of the substring is even
            if len(substring) % 2 == 0:
                print(substring)

# Example usage
input_string = input("Enter a string: ")
print("Even length substrings are:")
print_even_length_substrings(input_string)
