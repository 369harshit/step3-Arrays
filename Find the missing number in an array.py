def find_missing_number(arr, n):
    for num in range(1, n + 1):
        if num not in arr:
            return num

# Example usage
array = [1, 2, 4, 6, 3, 7, 8]
n = len(array) + 1  # Total numbers including the missing one
missing_number = find_missing_number(array, n)
print("The missing number is:", missing_number)
