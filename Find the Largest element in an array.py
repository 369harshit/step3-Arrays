def find_largest_element(arr):
    if len(arr) == 0:
        return None

    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element

    return max_element

# Example usage
array = [2,5,1,3,0]
largest = find_largest_element(array)
print("The largest element is:", largest)