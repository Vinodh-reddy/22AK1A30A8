# Create a file with at least 10 lines of characters
filename = "sample.txt"
with open(filename, "w") as file:
    for i in range(1, 11):
        file.write(f"This is line {i}\n")

# Function to read the first n characters and display them in reverse
def read_and_reverse(filename, n):
    with open(filename, "r") as file:
        content = file.read(n)
    print("Original content:", content)
    print("Reversed content:", content[::-1])

# Read the first n characters from the file and display them in reverse
n = int(input("Enter the number of characters to read: "))
read_and_reverse(filename, n)
