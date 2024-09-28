def interchange_first_last_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        # Swap the first and last column elements
        matrix[i][0], matrix[i][cols - 1] = matrix[i][cols - 1], matrix[i][0]
    
    return matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

interchanged_matrix = interchange_first_last_column(matrix)

print("\nMatrix after interchanging first and last columns:")
for row in interchanged_matrix:
    print(row)
