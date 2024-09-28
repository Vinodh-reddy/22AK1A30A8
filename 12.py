from collections import Counter

def count_characters(s):
    return Counter(s)

# Example usage
input_string = input("Enter a string: ")
character_counts = count_characters(input_string)

print("\nCharacter counts:")
for char, count in character_counts.items():
    print(f"'{char}': {count}")
