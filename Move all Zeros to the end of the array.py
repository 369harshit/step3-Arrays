def move_zeros_to_end(arr):
    non_zero_count = 0

    # Traverse the array, move non-zero elements to the front, and count them
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_count], arr[i] = arr[i], arr[non_zero_count]
            non_zero_count += 1

# Example usage
array = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
move_zeros_to_end(array)
print("Array after moving zeros to the end:", array)
