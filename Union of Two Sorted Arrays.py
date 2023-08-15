def find_union(arr1, arr2):
    merged = arr1 + arr2
    union = []
    
    for element in merged:
        if element not in union:
            union.append(element)
    
    return union

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [2, 3, 4, 4, 5]
union_result = find_union(array1, array2)
print("Union of the two arrays:", union_result)
