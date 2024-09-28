def find_closest_to_zero(arr):
    # Sort the array
    arr.sort()
    left = 0
    right = len(arr) - 1
    min_sum = float('inf')
    closest_pair = (0, 0)

    while left < right:
        current_sum = arr[left] + arr[right]

        # Update the closest pair if the current sum is closer to zero
        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            closest_pair = (arr[left], arr[right])

        # Move the pointers based on the sum
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return closest_pair

# Example usage
array = [1, 60, -10, 70, -80, 85]
pair = find_closest_to_zero(array)
print(f"The pair whose sum is closest to zero is: {pair}")
