def is_array_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [7, 3, 9, 12, 15]

print("Is array1 sorted?", is_array_sorted(array1))
print("Is array2 sorted?", is_array_sorted(array2))
