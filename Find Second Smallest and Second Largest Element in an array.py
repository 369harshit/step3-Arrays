def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None

    first_smallest = min(arr[0], arr[1])
    second_smallest = max(arr[0], arr[1])

    first_largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])

    for element in arr[2:]:
        if element < first_smallest:
            second_smallest = first_smallest
            first_smallest = element
        elif element < second_smallest:
            second_smallest = element

        if element > first_largest:
            second_largest = first_largest
            first_largest = element
        elif element > second_largest and element != first_largest:  # Avoid duplicate max
            second_largest = element

    return second_smallest, second_largest

# Given input
array = [1, 2, 4, 7, 7, 5]
second_smallest, second_largest = find_second_smallest_largest(array)
print("Second Smallest:", second_smallest)
print("Second Largest:", second_largest)
